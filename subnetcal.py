#!/usr/bin/env python3
"""
Ana Subnet Hesaplayıcı Uygulaması
Modüler yapı ile subnet analizi ve IP hesaplama aracı
"""
import argparse
import ipaddress
from ip_analyzer import IPAnalyzer
from subnet_calculator import SubnetCalculator
from output_formatter import OutputFormatter
from help_guide import HelpGuide


class SubnetApp:
    """Ana uygulama sınıfı"""

    def __init__(self):
        self.ip_analyzer = IPAnalyzer()
        self.subnet_calculator = SubnetCalculator()
        self.output_formatter = OutputFormatter()
        self.help_guide = HelpGuide()

    def analyze_subnet(self, subnet_str):
        """Subnet analizi yap ve sonuçları göster"""
        # Subnet hesaplamaları
        subnet_info = self.subnet_calculator.calculate_subnet_details(subnet_str)

        if not subnet_info["is_valid"]:
            self.output_formatter.print_error(
                f"Geçersiz subnet formatı! ({subnet_info['error']})"
            )
            self.output_formatter.print_tip(
                "Örnek kullanım: 192.168.1.0/24 veya 10.0.0.0/8"
            )
            return

        # IP sınıfı analizi
        network = ipaddress.ip_network(subnet_str, strict=False)
        ip_class = self.ip_analyzer.get_ip_class(network.network_address)
        private_info = self.ip_analyzer.check_private_network(network)

        # Alt subnet önerileri
        suggestions = []
        if network.prefixlen <= 28:
            suggestions = self.subnet_calculator.suggest_subnets(network)

        # Sonuçları göster
        self.output_formatter.print_subnet_details(
            subnet_info, ip_class, private_info, suggestions
        )

    def check_ip(self, ip_str):
        """IP adresi kontrolü yap"""
        ip_info = self.ip_analyzer.validate_and_analyze_ip(ip_str)
        self.output_formatter.print_ip_analysis(ip_info)

    def split_subnet(self, subnet_str, new_prefix):
        """Subnet bölme işlemi"""
        split_info = self.subnet_calculator.split_subnet(subnet_str, new_prefix)
        self.output_formatter.print_subnet_split(split_info)

    def show_cidr_info(self, prefix):
        """CIDR bilgilerini göster"""
        cidr_info = self.subnet_calculator.get_cidr_info(prefix)
        self.output_formatter.print_cidr_info(cidr_info)

    def run(self):
        """Ana uygulama çalıştırma fonksiyonu"""
        parser = self.create_argument_parser()
        args = parser.parse_args()

        # Yardım komutları kontrolü
        if self.handle_help_commands(args):
            return

        # Ana işlemler
        if args.cidr:
            self.show_cidr_info(args.cidr)
        elif args.split and args.subnet:
            self.split_subnet(args.subnet, args.split)
        elif args.check and args.subnet:
            self.check_ip(args.subnet)
        elif args.subnet:
            self.analyze_subnet(args.subnet)
        else:
            parser.print_help()
            print()
            self.output_formatter.print_usage_examples()

    def create_argument_parser(self):
        """Argüman parser'ı oluştur"""
        parser = argparse.ArgumentParser(
            description="🌐 Subnet Hesaplama ve IP Analiz Aracı - Yeni Başlayanlar İçin",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
    🎯 ÖRNEK KULLANIMLAR - BAŞLANGIÇ SEVİYESİ:

    🔍 Ev ağınızı analiz edin:
        python subnetcal.py 192.168.1.0/24

    📱 IP adresinizi kontrol edin:  
        python subnetcal.py 192.168.1.100 --check

    🏢 Ağ bölmeyi öğrenin:
        python subnetcal.py 192.168.1.0/24 --split 26

    📚 Öğrenme modu:
        python subnetcal.py --learn ip_classes
        python subnetcal.py --learn subnet_mask
        python subnetcal.py --learn all

    💡 İPUCU: Hiçbir şey bilmiyorsanız 'python subnetcal.py --learn basics' komutunu deneyin!
            """,
        )

        parser.add_argument(
            "subnet", nargs="?", help="Analiz edilecek subnet (örn: 192.168.1.0/24)"
        )
        parser.add_argument(
            "--split", type=int, help="Subnet'i bölmek için yeni prefix uzunluğu"
        )
        parser.add_argument(
            "--check", action="store_true", help="IP adresi kontrolü ve analizi"
        )
        parser.add_argument(
            "--cidr", type=int, help="CIDR prefix bilgisi göster (/8 - /32)"
        )
        parser.add_argument(
            "--info", help="Bilgi konusu (ip_type, subnet_mask, general)"
        )
        parser.add_argument(
            "-help",
            dest="help_topic",
            help="Yardım konusu (ip_type, subnet_mask, general)",
        )
        parser.add_argument(
            "--learn",
            choices=["ip_classes", "subnet_mask", "basics", "all"],
            help="Öğrenme modu: ip_classes, subnet_mask, basics, all",
        )
        return parser

    def handle_help_commands(self, args):
        """Yardım komutlarını işle"""
        help_topics = {
            "ip_type": self.help_guide.show_ip_class_info,
            "subnet_mask": self.help_guide.show_subnet_mask_guide,
            "general": self.help_guide.show_general_help,
        }

        # --learn argümenti kontrolü
        if hasattr(args, "learn") and args.learn:
            if args.learn == "ip_classes":
                self.help_guide.show_ip_class_info()
                return True
            elif args.learn == "subnet_mask":
                self.help_guide.show_subnet_mask_guide()
                return True
            elif args.learn == "basics":
                self.help_guide.show_basics()
                return True
            elif args.learn == "all":
                from help_guide import show_complete_help
                show_complete_help()
                return True

        # --info argümenti kontrolü
        if args.info in help_topics:
            help_topics[args.info]()
            return True

        # -help argümenti kontrolü
        if hasattr(args, "help_topic") and args.help_topic in help_topics:
            help_topics[args.help_topic]()
            return True

        return False


def main():
    """Ana fonksiyon"""
    app = SubnetApp()
    app.run()


if __name__ == "__main__":
    main()
