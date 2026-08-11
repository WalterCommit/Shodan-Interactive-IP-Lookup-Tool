#!/usr/bin/env python3
"""
Shodan Interactive IP Lookup Tool (Free Tier Safe)
Çalıştırıldığında kullanıcıdan interaktif olarak hedef IP/aralık/CIDR ister.
"""

import os
import sys
import time

try:
    import shodan
except ImportError:
    print("❌ 'shodan' kütüphanesi eksik. Kurulum: pip install shodan")
    sys.exit(1)

try:
    from netaddr import IPNetwork, IPRange, AddrFormatError
except ImportError:
    print("❌ 'netaddr' kütüphanesi eksik. Kurulum: pip install netaddr")
    sys.exit(1)

# --- AYARLAR ---
FREE_TIER_LIMIT = 100
REQUEST_DELAY = 1.5
QUERY_COUNT = 0


def get_api_key():
    key = os.environ.get('SHODAN_API_KEY', '').strip()
    if not key:
        print("\n❌ SHODAN_API_KEY ortam değişkeni bulunamadı!")
        print("   Linux/Mac: export SHODAN_API_KEY='anahtariniz'")
        print("   Windows:   set SHODAN_API_KEY=anahtariniz")
        print("   🔑 Ücretsiz anahtar: https://account.shodan.io/\n")
        sys.exit(1)
    return key


def lookup_ip(api, ip):
    global QUERY_COUNT
    if QUERY_COUNT >= FREE_TIER_LIMIT:
        print(f"\n⚠️  Free tier limiti ({FREE_TIER_LIMIT}/ay) doldu. Çıkılıyor...")
        sys.exit(0)

    print(f"\n🔍 Sorgulanıyor: {ip}")
    print("-" * 40)
    try:
        host = api.host(ip)
        QUERY_COUNT += 1
        print(f"  OS:        {host.get('os', 'Bilinmiyor')}")
        print(f"  Hostnames: {', '.join(host.get('hostnames', [])) or 'Yok'}")
        print(f"  Ports:     {', '.join(str(p) for p in sorted(host.get('ports', []))) or 'Yok'}")
        print(f"  Vulns:     {', '.join(host.get('vulns', [])) or 'Tespit edilmedi'}")
        print(f"  [Sorgu: {QUERY_COUNT}/{FREE_TIER_LIMIT}]")
    except shodan.APIError as e:
        err = str(e).lower()
        if 'usage limit' in err or '429' in err:
            print(f"⚠️  API limitine ulaşıldı: {e}")
            sys.exit(0)
        elif 'no information' in err:
            print("  ℹ️  Bu IP için Shodan kaydı bulunamadı.")
            QUERY_COUNT += 1
        else:
            print(f"  ❌ API Hatası: {e}")
    
    time.sleep(REQUEST_DELAY)


def interactive_menu(api):
    """Kullanıcıdan interaktif girdi alır ve taramayı başlatır."""
    print("\n" + "=" * 50)
    print("       SHODAN INTERACTIVE IP LOOKUP TOOL")
    print("=" * 50)
    print("  1) Tek IP Adresi")
    print("  2) IP Aralığı (Start - End)")
    print("  3) CIDR Notasyonu (örn: 192.168.1.0/24)")
    print("  0) Çıkış")
    print("=" * 50)

    choice = input("\nSeçiminiz (0-3): ").strip()
    ips = []

    try:
        if choice == "1":
            ip = input("IP adresini girin: ").strip()
            ips.append(ip)
        elif choice == "2":
            start = input("Başlangıç IP: ").strip()
            end = input("Bitiş IP: ").strip()
            ip_range = IPRange(start, end)
            ips = [str(ip) for ip in ip_range]
        elif choice == "3":
            cidr = input("CIDR bloğunu girin: ").strip()
            network = IPNetwork(cidr)
            ips = [str(ip) for ip in network]
        elif choice == "0":
            print("👋 Görüşmek üzere!")
            sys.exit(0)
        else:
            print("❌ Geçersiz seçim. Lütfen tekrar deneyin.")
            return
    except AddrFormatError as e:
        print(f"\n❌ Hatalı adres formatı: {e}")
        return
    except KeyboardInterrupt:
        print("\n\n🛑 İşlem iptal edildi.")
        sys.exit(0)

    # Free tier koruması
    unique_ips = sorted(set(ips), key=lambda x: [int(p) for p in x.split('.')])
    if len(unique_ips) > FREE_TIER_LIMIT:
        print(f"\n⚠️  {len(unique_ips)} IP bulundu. Free tier limiti nedeniyle sadece ilk {FREE_TIER_LIMIT} IP sorgulanacak.")
        confirm = input("Devam etmek istiyor musunuz? (E/h): ").strip().lower()
        if confirm != 'e':
            print("İptal edildi.")
            return
        unique_ips = unique_ips[:FREE_TIER_LIMIT]

    print(f"\n📋 Toplam {len(unique_ips)} IP sorgulanacak...")
    for ip in unique_ips:
        lookup_ip(api, ip)

    print(f"\n✅ Tarama tamamlandı! Kullanılan sorgu: {QUERY_COUNT}/{FREE_TIER_LIMIT}")


def main():
    api_key = get_api_key()
    api = shodan.Shodan(api_key)
    
    while True:
        interactive_menu(api)
        again = input("\n🔄 Yeni bir sorgu yapmak ister misiniz? (E/h): ").strip().lower()
        if again != 'e':
            print("👋 Programdan çıkılıyor...")
            break


if __name__ == '__main__':
    main()
