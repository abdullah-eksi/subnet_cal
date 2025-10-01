# 🌐 Subnet Hesaplayıcı & IP Analiz Aracı

Modern, öğretici ve tamamen standart Python kütüphaneleriyle yazılmış; hem yeni başlayanların öğrenmesine hem de temel ağ planlama ihtiyaçlarına yardımcı olan bir komut satırı aracı.

---
## 📌 Proje Özeti
Bu araç ile:
- Verilen bir subnet adresinin (örn: `192.168.1.0/24`) tüm teknik detaylarını görebilir
- Kullanılabilir IP aralığını, ağ & broadcast adreslerini inceleyebilir
- CIDR (Classless Inter-Domain Routing) / prefix değerlerinin ne anlama geldiğini öğrenebilir
- Büyük bir ağı daha küçük alt ağlara bölebilir (subnetting)
- Tekil bir IP adresini analiz edebilir (geçerlilik, sınıf, özel ağ bilgisi)
- Eğitim amaçlı zengin rehberler ile IP sınıfları ve subnet mask kavramlarını öğrenebilirsiniz

> Öğretici çıktı formatı ve anlaşılır ikonlarla yeni başlayanlar için uygundur.

---
## 🚀 Hızlı Başlangıç
Python 3.8+ (önerilen 3.11+) yüklü olduğundan emin olun.

```bash
# Subnet analizi
python subnetcal.py 192.168.1.0/24

# IP adresini analiz et
python subnetcal.py 192.168.1.100 --check

# Ağı daha küçük parçalara böl (/24 → /26)
python subnetcal.py 192.168.1.0/24 --split 26

# CIDR bilgisi görüntüle
python subnetcal.py --cidr 24

# Öğrenme modları
python subnetcal.py --learn basics
python subnetcal.py --learn ip_classes
python subnetcal.py --learn subnet_mask
python subnetcal.py --learn all
```

Windows için `.bat` kısayolu: `subnetcal.bat` dosyasını çift tıklayarak temel kullanımı görebilirsiniz (isteğe göre güncellenebilir). Bat Dosyasını Ortam Degıskenlerıne Ekleyip .py Yazmadanda Terminalde Kullanabilirsiniz.

---
## 🧠 Özellikler
| Kategori | Açıklama |
|----------|----------|
| Subnet Analizi | Ağ adresi, broadcast, subnet mask, wildcard, kullanılabilir IP sayıları |
| IP Aralığı | Kullanılabilir IP aralığını otomatik üretir (büyük ağlarda optimize) |
| IP Analizi | IPv4 geçerlilik, sınıf (A/B/C/D/E), özel/loopback/APIPA tespiti |
| CIDR Bilgisi | /8 - /32 arası mask, host sayıları ve wildcard hesaplaması |
| Subnet Bölme | Verilen ağı `--split` ile alt subnetlere ayırma |
| Öneriler | Daha küçük alt subnet önerileri (/28'e kadar) |
| Öğrenme Rehberi | IP sınıfları, subnet mask, temel kavramlar, öğrenme yol haritası |
| Anlaşılır Çıktı | Emoji ve başlıklarla segmentlere ayrılmış okunabilir çıktılar |

---
## 📂 Proje Yapısı
```
subnet/
├── subnetcal.py            # Ana CLI uygulaması
├── subnet_calculator.py    # Subnet hesaplama fonksiyonları
├── ip_analyzer.py          # IP sınıfı ve geçerlilik analizleri
├── output_formatter.py     # Çıktı formatlama & yazdırma yardımcıları
├── help_guide.py           # Öğretici rehber & öğrenme içerikleri
├── subnetcal.bat           # Windows kısayolu (opsiyonel)
└── README.md               # Proje dökümantasyonu
```
Tamamen modüler tasarım → Her dosya tek bir sorumluluk üstlenir.

---
## 🛠 Kurulum
Harici bağımlılık YOK. Sadece Python'un standart kütüphanelerini kullanır (`ipaddress`, `argparse`).

```bash
# Depoyu kopyalayın (örnek)
git clone <[repo-url](https://github.com/abdullah-eksi/subnet_cal)>
cd subnet
python subnetcal.py 192.168.1.0/24

## 🧪 Örnek Çıktı
Komut:
```bash
python subnetcal.py 192.168.1.0/24
```
Örnek çıktı (kısaltılmış):
```
==================================================
🌐 GELİŞMİŞ SUBNET HESAPLAMA ARACI
==================================================
📡 Ağ Bilgileri:
   • Ağ Adresi     : 192.168.1.0
   • Broadcast     : 192.168.1.255
   • Subnet Mask   : 255.255.255.0
   • Wildcard Mask : 0.0.0.255
   • Prefix        : /24

📊 IP Dağılımı:
   • Toplam IP     : 256
   • Kullanılabilir: 254
   • Kullanım Aralığı: 192.168.1.1 - 192.168.1.254

🔢 Binary Gösterim:
   • Ağ Adresi     : 11000000.10101000.00000001.00000000
   • Subnet Mask   : 11111111.11111111.11111111.00000000

📈 CIDR Analizi:
   • Host Bitleri  : 8
   • Maks. Host    : 254
   • IP Sınıfı     : C (Küçük ağlar)
   • Ağ Türü       : Özel Ağ (RFC 1918 - 192.168.0.0/16)
...
```

---
## 🔍 Argümanlar ve Kullanım
| Argüman | Örnek | Açıklama |
|---------|-------|----------|
| `subnet` | `192.168.1.0/24` | Analiz edilecek subnet veya IP |
| `--check` | `--check` | Tekil IP analizi (geçerlilik, sınıf) |
| `--split <prefix>` | `--split 26` | Verilen ağı küçük subnetlere böler |
| `--cidr <n>` | `--cidr 24` | /n için CIDR & mask bilgisi |
| `--learn <mod>` | `--learn basics` | Eğitim modu (ip_classes, subnet_mask, basics, all) |
| `--info <konu>` | `--info ip_type` | Kısa yardım (ip_type, subnet_mask, general) |
| `-help <konu>` | `-help general` | Alternatif yardım sözdizimi |

---
## 🧩 İç Modüller
| Modül | Sorumluluk |
|-------|------------|
| `SubnetApp` | Giriş noktası, argüman yönetimi, akış kontrolü |
| `SubnetCalculator` | Subnet parsing, IP aralığı, bölme, CIDR matematiği |
| `IPAnalyzer` | IP sınıfı, özel/loopback tanımlama, doğrulama |
| `OutputFormatter` | Estetik ve tutarlı çıktı üretimi |
| `HelpGuide` | Öğretici içerik ve öğrenme yolculuğu |

---
## 🧠 Öğrenme Yol Haritası (Kısa)
1. `--learn basics` → Kavramlara giriş
2. `--learn ip_classes` → Adres sınıfları
3. `--learn subnet_mask` → Mask mantığı
4. Gerçek analiz: `192.168.1.0/24`
5. Tasarım: `10.0.0.0/8 --split 16`

---
## 🛡 Hatalar ve İpuçları
| Durum | İpucu |
|-------|-------|
| Geçersiz subnet | CIDR eklemeyi unutmayın: `192.168.1.0/24` |
| Çok küçük bölme | `/31` ve `/32` ağlarında kullanılabilir host yok (özel durumlar hariç) |
| Yanlış prefix | `--split` değeri mevcut prefix'ten büyük olmalı |


---
## 🧪 Test Önerileri (Elle)
| Amaç | Komut |
|------|-------|
| Büyük ağ | `python subnetcal.py 10.0.0.0/8` |
| Bölme işlemi | `python subnetcal.py 192.168.0.0/23 --split 24` |
| Küçük ağ | `python subnetcal.py 192.168.1.0/30` |
| IP kontrol | `python subnetcal.py 127.0.0.1 --check` |
| CIDR bilgi | `python subnetcal.py --cidr 20` |

---
## ❓ SSS
**S: Neden bazı ağlarda kullanılabilir IP sayısı 2 eksik?**  
C: Ağ adresi (.0) ve broadcast adresi (.255) cihazlara atanamaz (istisna bazı özel /31 ve /32 senaryoları).


**S: Program neden emoji kullanıyor?**  
C: Eğitim ve okunabilirlik için; isterseniz `OutputFormatter` içinde düzenleyebilirsiniz.

---
## 🔧 Uyumluluk
- Python: 3.8+
- Platform: Windows / Linux / macOS
- Bağımlılık: Yok (standart kütüphane)



---
## 🙌 Teşekkürler
Bu araç, ağ temellerini öğrenmek isteyenler için hafif ve anlaşılır bir başlangıç noktası sunar. Kendi ihtiyaçlarınıza göre genişletebilirsiniz.

> İyi analizler! 🔍
