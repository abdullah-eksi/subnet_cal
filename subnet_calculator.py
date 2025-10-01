#!/usr/bin/env python3
"""
Subnet Hesaplama Modülü
Subnet ile ilgili hesaplama ve analiz fonksiyonları
"""
import ipaddress


class SubnetCalculator:
    """Subnet hesaplama sınıfı"""
    
    @staticmethod
    def calculate_subnet_details(subnet_str):
        """Subnet detaylarını hesapla"""
        try:
            network = ipaddress.ip_network(subnet_str, strict=False)
            
            # Temel hesaplamalar
            total_ips = network.num_addresses
            usable_ips = total_ips - 2 if total_ips > 2 else total_ips
            host_bits = 32 - network.prefixlen
            
            # IP aralığı
            if usable_ips > 0:
                if network.num_addresses <= 256:
                    hosts_list = list(network.hosts())
                    ip_range = f"{hosts_list[0]} - {hosts_list[-1]}" if hosts_list else "Yok"
                else:
                    ip_range = f"{network.network_address + 1} - {network.broadcast_address - 1}"
            else:
                ip_range = "Yok"
            
            return {
                'network_address': str(network.network_address),
                'broadcast_address': str(network.broadcast_address),
                'netmask': str(network.netmask),
                'hostmask': str(network.hostmask),
                'prefix_length': network.prefixlen,
                'total_ips': total_ips,
                'usable_ips': usable_ips,
                'host_bits': host_bits,
                'max_hosts': 2**host_bits - 2 if host_bits >= 2 else 0,
                'ip_range': ip_range,
                'network_binary': '.'.join(f'{int(octet):08b}' for octet in str(network.network_address).split('.')),
                'netmask_binary': '.'.join(f'{int(octet):08b}' for octet in str(network.netmask).split('.')),
                'is_valid': True
            }
            
        except ValueError as e:
            return {
                'is_valid': False,
                'error': str(e)
            }
    
    @staticmethod
    def split_subnet(main_subnet_str, new_prefix):
        """Subnet bölme işlemi"""
        try:
            main_network = ipaddress.ip_network(main_subnet_str, strict=False)
            new_prefix = int(new_prefix)
            
            if new_prefix <= main_network.prefixlen:
                return {
                    'is_valid': False,
                    'error': 'Yeni prefix, mevcut prefix\'ten büyük olmalıdır!'
                }
            
            subnets = list(main_network.subnets(new_prefix=new_prefix))
            
            subnet_list = []
            for i, subnet in enumerate(subnets, 1):
                usable = subnet.num_addresses - 2 if subnet.num_addresses > 2 else subnet.num_addresses
                subnet_list.append({
                    'number': i,
                    'network': str(subnet),
                    'usable_ips': usable
                })
            
            return {
                'is_valid': True,
                'main_subnet': main_subnet_str,
                'new_prefix': new_prefix,
                'subnet_count': len(subnets),
                'subnets': subnet_list
            }
            
        except ValueError as e:
            return {
                'is_valid': False,
                'error': str(e)
            }
    
    @staticmethod
    def suggest_subnets(network):
        """Alt subnet bölme önerileri"""
        current_prefix = network.prefixlen
        suggestions = []
        
        if current_prefix <= 24:
            for new_prefix in [current_prefix + 2, current_prefix + 4, current_prefix + 8]:
                if new_prefix <= 30:
                    subnet_count = 2 ** (new_prefix - current_prefix)
                    host_count = 2 ** (32 - new_prefix) - 2
                    if host_count > 0:
                        suggestions.append({
                            'prefix': new_prefix,
                            'subnet_count': subnet_count,
                            'host_count': host_count
                        })
        
        return suggestions
    
    @staticmethod
    def get_cidr_info(prefix):
        """CIDR prefix bilgilerini al"""
        if not 8 <= prefix <= 32:
            return {
                'is_valid': False,
                'error': 'CIDR prefix 8-32 arasında olmalıdır!'
            }
        
        host_bits = 32 - prefix
        total_ips = 2 ** host_bits
        usable_ips = total_ips - 2 if total_ips > 2 else total_ips
        
        # Subnet mask hesapla
        mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
        subnet_mask = f"{(mask >> 24) & 0xFF}.{(mask >> 16) & 0xFF}.{(mask >> 8) & 0xFF}.{mask & 0xFF}"
        
        # Wildcard mask hesapla
        wildcard_mask = '.'.join(str(255 - int(x)) for x in subnet_mask.split('.'))
        
        return {
            'is_valid': True,
            'prefix': prefix,
            'subnet_mask': subnet_mask,
            'wildcard_mask': wildcard_mask,
            'host_bits': host_bits,
            'total_ips': total_ips,
            'usable_ips': usable_ips
        }