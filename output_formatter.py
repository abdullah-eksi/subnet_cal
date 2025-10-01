#!/usr/bin/env python3
"""
Çıktı Formatlama Modülü
Tüm çıktıları formatlamak ve görsel olarak düzenlemek için fonksiyonlar
"""


class OutputFormatter:
    """Çıktı formatlama sınıfı"""
    
    @staticmethod
    def print_header(title, char="=", width=50):
        """Başlık yazdır"""
        print(f"\n{char * width}")
        print(f"🌐 {title}")
        print(f"{char * width}")
    
    @staticmethod
    def print_section(title, char="-", width=50):
        """Bölüm başlığı yazdır"""
        print(f"\n{title}:")
        print(char * width)
    
    @staticmethod
    def print_subnet_details(subnet_info, ip_class, private_info, suggestions):
        """Subnet detaylarını formatla ve yazdır"""
        OutputFormatter.print_header("GELİŞMİŞ SUBNET HESAPLAMA ARACI")
        
        # Temel bilgiler
        print(f"📡 Ağ Bilgileri:")
        print(f"   • Ağ Adresi     : {subnet_info['network_address']}")
        print(f"   • Broadcast     : {subnet_info['broadcast_address']}")
        print(f"   • Subnet Mask   : {subnet_info['netmask']}")
        print(f"   • Wildcard Mask : {subnet_info['hostmask']}")
        print(f"   • Prefix        : /{subnet_info['prefix_length']}")
        
        # IP sayıları
        print(f"\n📊 IP Dağılımı:")
        print(f"   • Toplam IP     : {subnet_info['total_ips']:,}")
        print(f"   • Kullanılabilir: {subnet_info['usable_ips']:,}")
        
        if subnet_info['usable_ips'] > 0:
            print(f"   • Kullanım Aralığı: {subnet_info['ip_range']}")
        
        # Binary gösterim
        print(f"\n🔢 Binary Gösterim:")
        print(f"   • Ağ Adresi     : {subnet_info['network_binary']}")
        print(f"   • Subnet Mask   : {subnet_info['netmask_binary']}")
        
        # CIDR analizi
        print(f"\n📈 CIDR Analizi:")
        print(f"   • Host Bitleri  : {subnet_info['host_bits']}")
        print(f"   • Maks. Host    : {subnet_info['max_hosts']:,}")
        print(f"   • IP Sınıfı     : {ip_class}")
    
        # Özel/Ayrılmış ağ kontrolü
        if private_info:
            print(f"   • Ağ Türü       : {private_info}")
        
        # Alt subnet önerileri
        if suggestions:
            print(f"\n🔧 Alt Subnet Önerileri:")
            for suggestion in suggestions:
                print(f"   • /{suggestion['prefix']}: {suggestion['subnet_count']:,} subnet, "
                      f"{suggestion['host_count']:,} host/subnet")
        
        print("=" * 50)
    
    @staticmethod
    def print_ip_analysis(ip_info):
        """IP analizi sonuçlarını yazdır"""
        print(f"\n🔍 IP Analizi: {ip_info['ip']}")
        print("-" * 30)
        
        if ip_info['is_valid']:
            print(f"IP Adresi    : {ip_info['ip']}")
            print(f"Version      : IPv{ip_info['version']}")
            
            if ip_info['version'] == 4:
                print(f"Binary       : {ip_info['binary']}")
                print(f"Sınıf        : {ip_info['class']}")
                
                if ip_info.get('private_info'):
                    print(f"Özel/Ayrılmış: {ip_info['private_info']}")
            
            print(f"Geçerli IP   : Evet")
        else:
            print(f"❌ Geçersiz IP adresi: {ip_info['error']}")
    
    @staticmethod
    def print_subnet_split(split_info):
        """Subnet bölme sonuçlarını yazdır"""
        if split_info['is_valid']:
            print(f"\n🎯 Subnet Bölme: {split_info['main_subnet']} → /{split_info['new_prefix']}")
            print("-" * 40)
            
            print(f"Oluşturulan {split_info['subnet_count']} alt subnet:")
            for subnet in split_info['subnets']:
                print(f"{subnet['number']:2d}. {subnet['network']} - {subnet['usable_ips']} kullanılabilir IP")
        else:
            print(f"❌ Hata: {split_info['error']}")
    
    @staticmethod
    def print_cidr_info(cidr_info):
        """CIDR bilgilerini yazdır"""
        if cidr_info['is_valid']:
            print(f"\n📋 CIDR /{cidr_info['prefix']} Bilgisi:")
            print("-" * 25)
            print(f"Subnet Mask   : {cidr_info['subnet_mask']}")
            print(f"Host Bitleri  : {cidr_info['host_bits']}")
            print(f"Toplam IP     : {cidr_info['total_ips']:,}")
            print(f"Kullanılabilir: {cidr_info['usable_ips']:,}")
            
            if cidr_info['prefix'] <= 30:
                print(f"Wildcard Mask : {cidr_info['wildcard_mask']}")
        else:
            print(f"❌ {cidr_info['error']}")
    
    @staticmethod
    def print_error(message):
        """Hata mesajını yazdır"""
        print(f"❌ Hata: {message}")
    
    @staticmethod
    def print_tip(message):
        """İpucu mesajını yazdır"""
        print(f"💡 İpucu: {message}")
    
    @staticmethod
    def print_usage_examples():
        """Kullanım örneklerini yazdır"""
        OutputFormatter.print_tip("'python subnetcal.py 192.168.1.0/24' şeklinde deneyebilirsiniz.")
        OutputFormatter.print_tip("Genel komutlar için: 'python subnetcal.py -help general'")
        OutputFormatter.print_tip("IP sınıfları için: 'python subnetcal.py -help ip_type'")
        OutputFormatter.print_tip("Subnet mask rehberi için: 'python subnetcal.py -help subnet_mask'")