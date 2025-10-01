#!/usr/bin/env python3
"""
Yardım ve Rehber Modülü - Yeni Başlayanlar İçin
IP sınıfları, subnet mask rehberi ve genel yardım bilgileri
"""

class HelpGuide:
    """Yardım ve rehber sınıfı - Öğretici ve açıklayıcı"""
    
    @staticmethod
    def show_ip_class_info():
        """IP sınıfları hakkında detaylı bilgi göster - Yeni başlayanlar için"""
        print("\n" + "🎓" + "="*50 + "🎓")
        print("        IP SINIFLARI - YENİ BAŞLAYANLAR İÇİN REHBER")
        print("🎓" + "="*50 + "🎓")
        
        print("\n🤔 NEDİR BU IP SINIFLARI?")
        print("   IP adresleri, internet üzerindeki cihazların kimlik kartları gibidir.")
        print("   Farklı büyüklükteki ağlar için farklı sınıflar oluşturulmuştur.")
        
        print("\n📚 TEMEL IP SINIFLARI:")
        print("-" * 55)
        
        print("\n🅰 1. A SINIFI - DEVLER İÇİN")
        print("   📍 Hangi IP'ler? : 1.0.0.0 - 127.255.255.255")
        print("   🏢 Kim kullanır?  : ÇOK büyük şirketler, internet servis sağlayıcıları")
        print("   👥 Kapasite       : Her ağda 16 MİLYON'dan fazla cihaz")
        print("   💡 Gerçek hayattan: 10.0.0.0/8 (Şirket içi özel ağlar)")
        print("   🎯 Örnek kullanım: python subnetcal.py 10.0.0.0/8")
        
        print("\n🅱 2. B SINIFI - ORTA ÖLÇEKLİLER İÇİN")
        print("   📍 Hangi IP'ler? : 128.0.0.0 - 191.255.255.255")
        print("   🏢 Kim kullanır?  : Üniversiteler, orta büyüklükte şirketler")
        print("   👥 Kapasite       : Her ağda 65,000'den fazla cihaz")
        print("   💡 Gerçek hayattan: 172.16.0.0/12 (Şirket içi özel ağlar)")
        print("   🎯 Örnek kullanım: python subnetcal.py 172.16.0.0/16")
        
        print("\n🅲 3. C SINIFI - EV VE KÜÇÜK OFİSLER İÇİN")
        print("   📍 Hangi IP'ler? : 192.0.0.0 - 223.255.255.255")
        print("   🏢 Kim kullanır?  : Ev kullanıcıları, küçük işletmeler")
        print("   👥 Kapasite       : Her ağda 254 cihaz")
        print("   💡 Gerçek hayattan: 192.168.1.0/24 (Ev WiFi ağınız!)")
        print("   🎯 Örnek kullanım: python subnetcal.py 192.168.1.0/24")
        
        print("\n📢 4. D SINIFI - GRUP MESAJLAŞMASI İÇİN")
        print("   📍 Hangi IP'ler? : 224.0.0.0 - 239.255.255.255")
        print("   🎯 Ne işe yarar? : Aynı anda birden fazla cihaza veri göndermek")
        print("   💡 Gerçek hayattan: Canlı video yayını, online oyunlar")
        
        print("\n🔬 5. E SINIFI - GELECEK İÇİN")
        print("   📍 Hangi IP'ler? : 240.0.0.0 - 255.255.255.255")
        print("   🎯 Durumu        : Şu an kullanılmıyor, gelecek teknolojiler için")
        
        print("\n🔐 EVİNİZDEKİ ÖZEL ADRESLER:")
        print("-" * 35)
        print("   🏠 10.0.0.0 - 10.255.255.255")
        print("   🏢 172.16.0.0 - 172.31.255.255")
        print("   📱 192.168.0.0 - 192.168.255.255")
        print("   💡 Bunlar sadece yerel ağınızda çalışır, internete çıkamaz!")
        
        print("\n🎯 PRATİK BİLGİLER:")
        print("-" * 20)
        print("   • Ev router'ınız: Genellikle 192.168.1.1 veya 192.168.0.1")
        print("   • Bilgisayarınız : 192.168.1.100 gibi bir adres")
        print("   • Telefonunuz    : 192.168.1.101 gibi bir adres")

    @staticmethod
    def show_subnet_mask_guide():
        """Subnet mask rehberi - Yeni başlayanlar için basit anlatım"""
        print("\n" + "📊" + "="*50 + "📊")
        print("      SUBNET MASK - ANLAŞILIR REHBER")
        print("📊" + "="*50 + "📊")
        
        print("\n🤔 SUBNET MASK NEDİR?")
        print("   Bir ev adresi gibi düşünün:")
        print("   • IP adresi    : Sokak ve kapı numarası")
        print("   • Subnet Mask  : Hangi kısmın sokak, hangi kısmın kapı no olduğunu gösterir")
        
        print("\n🎯 EN ÇOK KULLANILAN SUBNET MASK'LAR:")
        print("-" * 45)
        print(" CIDR | Subnet Mask     | Açıklama")
        print("-" * 45)
        
        print("\n🏠 EV VE KÜÇÜK OFİSLER:")
        print(" /24 | 255.255.255.0  | 254 cihaz - Standart ev ağı")
        print(" /25 | 255.255.255.128| 126 cihaz - Orta büyüklükte")
        print(" /26 | 255.255.255.192| 62 cihaz  - Küçük ofis")
        
        print("\n🏢 BÜYÜK OFİSLER:")
        print(" /16 | 255.255.0.0    | 65,534 cihaz - Büyük şirket")
        print(" /20 | 255.255.240.0  | 4,094 cihaz  - Orta şirket")
        
        print("\n🌐 DEVLER:")
        print(" /8  | 255.0.0.0      | 16 Milyon+   - Çok büyük ağlar")
        
        print("\n🔌 ÖZEL DURUMLAR:")
        print(" /30 | 255.255.255.252| 2 cihaz - Router bağlantıları")
        print(" /32 | 255.255.255.255| 1 cihaz - Sadece kendisi")
        
        print("\n💡 PRATİK HESAPLAMA YÖNTEMİ:")
        print("-" * 30)
        print("1. Son rakamı bul: 256 - Subnet Mask son okteti")
        print("2. Örnek: /26 → Mask: 255.255.255.192")
        print("3. 256 - 192 = 64 → Her bölüm 64 IP")
        print("4. Ağlar: .0, .64, .128, .192 şeklinde bölünür")
        
        print("\n🎯 GERÇEK HAYAT ÖRNEKLERİ:")
        print("-" * 25)
        print("🏠 EV AĞI:")
        print("   Ağ: 192.168.1.0/24")
        print("   Router: 192.168.1.1")
        print("   Bilgisayar: 192.168.1.100")
        print("   Telefon: 192.168.1.101")
        
        print("\n🏢 ŞİRKET AĞI:")
        print("   Ağ: 10.0.0.0/16")
        print("   Bölümler: 10.0.1.0/24, 10.0.2.0/24, ...")
        print("   Her bölüm kendi içinde 254 cihaz")

    @staticmethod
    def show_general_help():
        """Genel komutlar ve kullanım rehberi - Yeni başlayanlar için"""
        print("\n" + "🆘" + "="*50 + "🆘")
        print("     SUBNET HESAPLAYICI - BAŞLANGIÇ REHBERİ")
        print("🆘" + "="*50 + "🆘")
        
        print("\n🎯 BU PROGRAM NE İŞE YARAR?")
        print("   • Ağınızdaki kaç cihaz bağlanabilir?")
        print("   • IP adresiniz hangi ağa ait?")
        print("   • Büyük ağı küçük parçalara nasıl bölersiniz?")
        
        print("\n🚀 HEMEN DENEYİN - TEMEL KOMUTLAR:")
        print("-" * 35)
        
        print("\n1. 🔍 EV AĞINIZI ANALİZ EDİN:")
        print("   python subnetcal.py 192.168.1.0/24")
        print("   ⚡ Ne yapar?: Ev WiFi ağınızın tüm detaylarını gösterir")
        
        print("\n2. 📱 IP ADRESİNİZİ KONTROL EDİN:")
        print("   python subnetcal.py 192.168.1.100 --check")
        print("   ⚡ Ne yapar?: IP adresinizin hangi ağa ait olduğunu söyler")
        
        print("\n3. 🏢 BÜYÜK AĞI BÖLÜN:")
        print("   python subnetcal.py 192.168.1.0/24 --split 26")
        print("   ⚡ Ne yapar?: 254 cihazlık ağı 4 parçaya böler")
        
        print("\n4. 📚 CIDR ÖĞRENİN:")
        print("   python subnetcal.py --cidr 24")
        print("   ⚡ Ne yapar?: /24'ün ne anlama geldiğini açıklar")
        
        print("\n📖 ÖĞRENME KOMUTLARI:")
        print("-" * 20)
        print("🔹 IP sınıflarını öğren:")
        print("   python subnetcal.py --learn ip_classes")
        
        print("\n🔹 Subnet mask'ı öğren:")
        print("   python subnetcal.py --learn subnet_mask")
        
        print("\n🔹 Tüm yardımı gör:")
        print("   python subnetcal.py --learn all")
        
        print("\n💡 BAŞLANGIÇ İPUÇLARI:")
        print("-" * 20)
        print("🎯 EV AĞLARI İÇİN:")
        print("   • /24 → 254 cihaz (En yaygın)")
        print("   • /25 → 126 cihaz")
        print("   • /26 → 62 cihaz")
        
        print("\n🔧 OFİS AĞLARI İÇİN:")
        print("   • /23 → 510 cihaz")
        print("   • /22 → 1022 cihaz")
        
        print("\n🌐 GERÇEK HAYAT ÖRNEKLERİ:")
        print("-" * 25)
        print("🏠 EV:")
        print("   Ağ: 192.168.1.0/24")
        print("   Router: 192.168.1.1")
        print("   Cihazlar: 192.168.1.2 - 192.168.1.254")
        
        print("\n🏢 KÜÇÜK OFİS:")
        print("   Ağ: 192.168.0.0/23")
        print("   Bölüm 1: 192.168.0.0/24 (254 cihaz)")
        print("   Bölüm 2: 192.168.1.0/24 (254 cihaz)")
        
        print("\n❌ SIK YAPILAN HATALAR:")
        print("-" * 25)
        print("✅ DOĞRU: 192.168.1.0/24")
        print("❌ YANLIŞ: 192.168.1.0 (CIDR eksik)")
        print("")
        print("✅ DOĞRU: python subnetcal.py 10.0.0.0/8")
        print("❌ YANLIŞ: python subnetcal.py 10.0.0.0")

    @staticmethod
    def show_quick_start():
        """Hızlı başlangıç rehberi"""
        print("\n" + "🚀" + "="*50 + "🚀")
        print("        HIZLI BAŞLANGIÇ - 5 DAKİKADA ÖĞRENİN")
        print("🚀" + "="*50 + "🚀")
        
        print("\n🎯 ADIM 1: EV AĞINIZI KEŞFEDİN")
        print("   Komut: python subnetcal.py 192.168.1.0/24")
        print("   Ne öğreneceksiniz?: Kaç cihaz bağlanabilir, hangi IP'ler kullanılabilir")
        
        print("\n🎯 ADIM 2: KENDİ IP'NİZİ KONTROL EDİN") 
        print("   Komut: python subnetcal.py 192.168.1.100 --check")
        print("   Ne öğreneceksiniz?: IP'nizin hangi ağa ait olduğu")
        
        print("\n🎯 ADIM 3: AĞ BÖLMEYİ ÖĞRENİN")
        print("   Komut: python subnetcal.py 192.168.1.0/24 --split 26")
        print("   Ne öğreneceksiniz?: Büyük ağı küçük parçalara bölmek")
        
        print("\n🎯 ADIM 4: FARKLI AĞLARI DENEYİN")
        print("   Komut: python subnetcal.py 10.0.0.0/8")
        print("   Ne öğreneceksiniz?: Çok büyük ağların nasıl çalıştığı")

    @staticmethod
    def show_basics():
        """Temel subnet kavramları - Hiç bilmeyenler için"""
        print("\n" + "🌟" + "="*50 + "🌟")
        print("        SUBNET - SIFIRDAN BAŞLANGIÇ REHBERİ")
        print("🌟" + "="*50 + "🌟")
        
        print("\n🤔 SUBNET NEDİR?")
        print("   Bir apartman düşünün:")
        print("   • Bina        → Büyük ağ (Internet)")
        print("   • Daire       → Alt ağ (Subnet)")
        print("   • Sakinler    → Cihazlar (Bilgisayar, telefon)")
        
        print("\n📍 IP ADRESİ NEDİR?")
        print("   Ev adresiniz gibi:")
        print("   🏠 Örnek: İstanbul, Çekmeköy, A Cad. No:1 Daire:5")
        print("   💻 IP  : 192.168.1.100")
        print("   • 192.168.1   → Sokak adı")
        print("   • 100         → Daire numarası")
        
        print("\n🔢 TEMEL IP KURALLARI:")
        print("   ✅ Her cihazın kendine özel numarası var")
        print("   ✅ Aynı ağdaki cihazlar birbirleriyle konuşabilir")
        print("   ✅ Farklı ağlardaki cihazlar router ile konuşur")
        
        print("\n🏠 EV AĞINIZ NASIL ÇALIŞIR?")
        print("   🌐 İnternet Sağlayıcısı → Ev Router'ınız → Cihazlarınız")
        print("   📡 Router IP'si        : 192.168.1.1")
        print("   💻 Bilgisayarınız      : 192.168.1.100")
        print("   📱 Telefonunuz         : 192.168.1.101")
        print("   📺 Akıllı TV'niz       : 192.168.1.102")
        
        print("\n🔍 HEMEN DENEYİN:")
        print("   1. Windows'ta: Win+R → cmd → ipconfig")
        print("   2. Mac/Linux'ta: ifconfig veya ip addr")
        print("   3. Bu programla: python subnetcal.py 192.168.1.0/24")
        
        print("\n🎯 İLK DENEMELER:")
        print("   🔹 Kendi ağınızı analiz edin:")
        print("      python subnetcal.py 192.168.1.0/24")
        print("   🔹 IP'nizi kontrol edin:")
        print("      python subnetcal.py 192.168.1.100 --check")
        
        print("\n💡 ÖNEMLİ NOKTALAR:")
        print("   • /24 → 254 cihaz bağlanabilir")
        print("   • .1 → Genellikle router")
        print("   • .2-254 → Cihazlarınız için")
        print("   • .0 ve .255 → Özel, cihazlara verilmez")
        
        print("\n📚 DEVAMI İÇİN:")
        print("   python subnetcal.py --learn ip_classes")
        print("   python subnetcal.py --learn subnet_mask")

    @staticmethod
    def show_learning_path():
        """Öğrenme yol haritası"""
        print("\n" + "📚" + "="*50 + "📚")
        print("        ÖĞRENME YOL HARİTASI - ADIM ADIM")
        print("📚" + "="*50 + "📚")
        
        print("\n🔰 SEVİYE 1: TEMEL KAVRAMLAR")
        print("   ✅ IP adresi nedir?")
        print("   ✅ Subnet mask ne işe yarar?") 
        print("   ✅ Ev ağınız nasıl çalışır?")
        print("   🎯 Komut: python subnetcal.py --learn basics")
        
        print("\n🔰 SEVİYE 2: AĞ ANALİZİ")
        print("   ✅ Kendi ağınızı analiz edin")
        print("   ✅ Farklı büyüklükteki ağları karşılaştırın")
        print("   ✅ Kullanılabilir IP aralıklarını anlayın")
        print("   🎯 Komut: python subnetcal.py 192.168.1.0/24")
        
        print("\n🔰 SEVİYE 3: AĞ TASARIMI")
        print("   ✅ Büyük ağları bölmeyi öğrenin")
        print("   ✅ Farklı departmanlar için alt ağlar oluşturun")
        print("   ✅ Optimizasyon yapmayı öğrenin")
        print("   🎯 Komut: python subnetcal.py 10.0.0.0/8 --split 16")

def show_complete_help():
    """Tüm yardım bilgilerini göster"""
    guide = HelpGuide()
    
    print("\n🌐 SUBNET HESAPLAYICI - TAM YARDIM REHBERİ")
    print("="*55)
    
    guide.show_quick_start()
    guide.show_learning_path() 
    guide.show_general_help()
    
    print("\n" + "💎" + "="*50 + "💎")
    print("        ÖNEMLİ TERİMLER - SÖZLÜK")
    print("💎" + "="*50 + "💎")
    
    print("\n🔤 TEMEL TERİMLER:")
    print("   • IP Adresi    : İnternetteki cihazın adresi (ev adresi gibi)")
    print("   • Subnet Mask  : Hangi kısmın ağ, hangi kısmın cihaz olduğunu gösterir")
    print("   • CIDR         : Subnet mask'ın kısa gösterimi (/24 gibi)")
    print("   • Ağ Adresi    : Ağın başlangıç adresi (sokak adı gibi)")
    print("   • Broadcast    : Ağdaki tüm cihazlara mesaj gönderme adresi")
    
    print("\n🎯 DEVAM ETMEK İÇİN:")
    print("   'python subnetcal.py --learn basics' komutunu deneyin!")