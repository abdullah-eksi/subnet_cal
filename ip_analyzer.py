#!/usr/bin/env python3
"""
IP Analiz Modülü
IP adresleri ve sınıflandırma ile ilgili fonksiyonlar
"""
import ipaddress


class IPAnalyzer:
    """IP adresi analiz sınıfı"""
    
    @staticmethod
    def get_ip_class(ip_address):
        """IP adresinin sınıfını belirle"""
        first_octet = int(str(ip_address).split('.')[0])
        
        if first_octet <= 127:
            return "A (Büyük ağlar)"
        elif first_octet <= 191:
            return "B (Orta ölçekli ağlar)"
        elif first_octet <= 223:
            return "C (Küçük ağlar)"
        elif first_octet <= 239:
            return "D (Multicast)"
        else:
            return "E (Rezerve)"
    
    @staticmethod
    def check_private_network(network):
        """Özel veya ayrılmış ağ kontrolü"""
        ip_str = str(network.network_address)
        
        # Özel IP aralıkları
        if ip_str.startswith('10.'):
            return "Özel Ağ (RFC 1918 - 10.0.0.0/8)"
        elif ip_str.startswith('192.168.'):
            return "Özel Ağ (RFC 1918 - 192.168.0.0/16)"
        elif ip_str.startswith(tuple(f'172.{i}.' for i in range(16, 32))):
            return "Özel Ağ (RFC 1918 - 172.16.0.0/12)"
        elif ip_str == '127.0.0.0':
            return "Loopback Ağı"
        elif ip_str.startswith('169.254.'):
            return "APIPA (Otomatik Özel IP Adresleme)"
        
        return None
    
    @staticmethod
    def validate_and_analyze_ip(ip_str):
        """IP adresi doğrulama ve analiz"""
        try:
            ip_obj = ipaddress.ip_address(ip_str)
            
            result = {
                'ip': str(ip_obj),
                'version': ip_obj.version,
                'is_valid': True
            }
            
            if ip_obj.version == 4:
                result['binary'] = '.'.join(f'{int(octet):08b}' for octet in str(ip_obj).split('.'))
                result['class'] = IPAnalyzer.get_ip_class(ip_obj)
                
                # Özel IP kontrolü için geçici network oluştur
                temp_network = ipaddress.ip_network(f'{ip_str}/32', strict=False)
                result['private_info'] = IPAnalyzer.check_private_network(temp_network)
            
            return result
            
        except ValueError as e:
            return {
                'ip': ip_str,
                'is_valid': False,
                'error': str(e)
            }