# 🔎 Shodan Interactive IP Lookup Tool

**TR 🇹🇷 | EN 🇬🇧**

---

## 🇹🇷 Türkçe

Shodan API kullanarak IP adresleri üzerinde interaktif bilgi sorgulaması yapmanızı sağlayan hafif ve kullanımı kolay bir Python aracıdır.

Tek bir IP adresini, IP aralığını veya CIDR bloğunu sorgulayabilir ve Shodan tarafından sağlanan mevcut bilgileri terminal üzerinden görüntüleyebilirsiniz.

> ⚠️ **Uyarı:** Bu araç yalnızca sahibi olduğunuz veya test etmek için açıkça yetkilendirildiğiniz sistemlerde kullanılmalıdır.

### ✨ Özellikler

* 🔍 Tek IP adresi sorgulama
* 📡 IP aralığı sorgulama
* 🌐 CIDR bloğu sorgulama
* 💻 İşletim sistemi bilgisi
* 🌍 Hostname bilgileri
* 🔌 Açık port bilgileri
* ⚠️ Shodan tarafından bildirilen zafiyetler
* 🛡️ Free Tier sorgu limiti koruması
* ⏱️ Sorgular arasında otomatik bekleme
* 🔑 API anahtarını ortam değişkeninden alma
* 🖥️ Windows, Linux ve macOS desteği

### 📋 Gereksinimler

* Python 3.8 veya üzeri
* Shodan API Key
* `shodan`
* `netaddr`

### 🚀 Kurulum

Repoyu klonlayın:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

### 🔑 Shodan API Key

Program API anahtarını `SHODAN_API_KEY` ortam değişkeninden alır.

**Windows CMD:**

```cmd
set SHODAN_API_KEY=YOUR_API_KEY
```

**Windows PowerShell:**

```powershell
$env:SHODAN_API_KEY="YOUR_API_KEY"
```

**Linux / macOS:**

```bash
export SHODAN_API_KEY="YOUR_API_KEY"
```

> 🔒 API anahtarınızı kaynak koduna eklemeyin veya GitHub'a yüklemeyin.

### ▶️ Kullanım

Programı çalıştırın:

```bash
python "shodan_ip for 2026.py"
```

Program aşağıdaki seçenekleri sunar:

```text
1) Tek IP Adresi
2) IP Aralığı (Start - End)
3) CIDR Notasyonu
0) Çıkış
```

### 📊 Görüntülenen Bilgiler

Shodan'da mevcut olması halinde:

```text
OS
Hostnames
Ports
Vulnerabilities
```

bilgileri görüntülenir.

### 🛡️ Free Tier Koruması

Araç, API kullanımını sınırlandırmak için dahili bir sorgu limiti içerir.

Varsayılan limit:

```text
100 sorgu
```

100'den fazla IP içeren bir IP aralığı veya CIDR bloğu girildiğinde program kullanıcıdan onay ister ve sorguları sınırlar.

### ⏱️ Sorgu Aralığı

Sorgular arasında varsayılan olarak **1.5 saniye** beklenir.

Bu değer kaynak kodundaki `REQUEST_DELAY` değişkeninden değiştirilebilir.

### 🔒 Güvenlik

API anahtarınızı:

* Kaynak koduna yazmayın
* README dosyasına eklemeyin
* GitHub'a commit etmeyin
* Herkese açık şekilde paylaşmayın

API anahtarını `SHODAN_API_KEY` ortam değişkeni üzerinden kullanmanız önerilir.

### ⚠️ Yasal Uyarı

Bu yazılım eğitim, araştırma ve yetkili güvenlik testleri amacıyla hazırlanmıştır.

Yetkisiz sistemleri veya IP adreslerini taramak, analiz etmek ya da araştırmak yasalara, hizmet şartlarına veya kurum politikalarına aykırı olabilir.

Yazılımın yanlış veya kötüye kullanımından geliştirici sorumlu değildir.

---

## 🇬🇧 English

A lightweight and easy-to-use Python tool for interactively querying IP addresses using the Shodan API.

The tool allows you to query a single IP address, an IP range, or a CIDR block and display available information provided by Shodan directly in the terminal.

> ⚠️ **Warning:** This tool should only be used on systems you own or have explicit authorization to test.

### ✨ Features

* 🔍 Single IP address lookup
* 📡 IP range lookup
* 🌐 CIDR block lookup
* 💻 Operating system information
* 🌍 Hostname information
* 🔌 Open port information
* ⚠️ Vulnerabilities reported by Shodan
* 🛡️ Free Tier query limit protection
* ⏱️ Automatic delay between requests
* 🔑 API key through environment variables
* 🖥️ Windows, Linux, and macOS support

### 📋 Requirements

* Python 3.8 or newer
* Shodan API Key
* `shodan`
* `netaddr`

### 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 🔑 Shodan API Key

The application reads the API key from the `SHODAN_API_KEY` environment variable.

**Windows CMD:**

```cmd
set SHODAN_API_KEY=YOUR_API_KEY
```

**Windows PowerShell:**

```powershell
$env:SHODAN_API_KEY="YOUR_API_KEY"
```

**Linux / macOS:**

```bash
export SHODAN_API_KEY="YOUR_API_KEY"
```

> 🔒 Never hard-code your API key into the source code or upload it to GitHub.

### ▶️ Usage

Run the application:

```bash
python "shodan_ip for 2026.py"
```

The program provides:

```text
1) Single IP Address
2) IP Range (Start - End)
3) CIDR Notation
0) Exit
```

### 📊 Information Displayed

When available in Shodan, the tool displays:

```text
OS
Hostnames
Ports
Vulnerabilities
```

### 🛡️ Free Tier Protection

The tool includes a built-in query limit to help prevent excessive API usage.

Default limit:

```text
100 queries
```

If an IP range or CIDR block contains more than 100 addresses, the program asks for confirmation and limits the number of queries.

### ⏱️ Request Delay

A **1.5-second delay** is applied between requests by default.

This value can be changed using the `REQUEST_DELAY` variable in the source code.

### 🔒 Security

Never:

* Hard-code your API key into the source code
* Add your API key to the README
* Commit your API key to GitHub
* Share your API key publicly

Using the `SHODAN_API_KEY` environment variable is recommended.

### ⚠️ Legal Disclaimer

This software is intended for educational purposes, research, and authorized security testing.

Scanning, analyzing, or investigating systems or IP addresses without proper authorization may violate applicable laws, terms of service, or organizational policies.

The developer is not responsible for misuse of this software or any consequences resulting from its use.

---

## 📁 Project Structure / Proje Yapısı

```text
.
├── shodan_ip for 2026.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## 📄 License / Lisans

**MIT License**

See the `LICENSE` file for the complete license text.

Tam lisans metni için `LICENSE` dosyasına bakınız.

## ⭐ Support / Destek

If you find this project useful, consider giving it a ⭐ on GitHub.

Projeyi faydalı bulduysanız GitHub üzerinde ⭐ bırakabilirsiniz.

For bug reports and feature requests, please use GitHub Issues.

Hata bildirimleri ve özellik önerileri için GitHub Issues bölümünü kullanabilirsiniz.
