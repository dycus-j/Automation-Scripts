import subprocess
import ipaddress
import sys
import time
import multiprocessing

def ping_worker(host):
    try:
        subprocess.run(
            ['ping', '-c', '1', '-W', '1', str(host)],
            capture_output=True, text=True, check=True
        )
        return (host, True)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return (host, False)
    
class NetworkScanner:
    def __init__(self, net_addr):
        try:
            self.ip_net = ipaddress.ip_network(net_addr) 
            self.net_hosts = list(self.ip_net.hosts())
        except ValueError:
            print(f"Error: '{net_addr}' is not a valid network address.")
            sys.exit(1)
            
    def _ping_host(self, host):
        try:
            subprocess.run(
                ['ping', '-c', '2', '-W', '1', str(host)],
                capture_output=True, 
                text=True, 
                check=True
            )
            print(f'✓ - {host} is ONLINE')
            self.online_hosts_count += 1
        except subprocess.CalledProcessError:
            pass
        
    def scan(self):
        print(f'\nScanning devices in {self.ip_net.with_prefixlen}...')
        start_time = time.time()
        
        with multiprocessing.Pool() as pool:
            results = pool.map(ping_worker, self.net_hosts)
            
        online_hosts = [host for host, status in results if status]
        
        end_time = time.time()
        duration = end_time - start_time
        
        if online_hosts:
            for host in online_hosts:
                print(f'\n✓ - {host} is ONLINE')
        else:
            print("\nNo online hosts found.")
                
            
        end_time = time.time()
        duration = end_time - start_time
        

            
        print('\nScan complete.')
        print(f"The scan took {duration:.2f} seconds to complete.") 
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Error: Please provide a network address as an argument.')
        print('Usage: python3 network_scanner.py 192.168.1.0/24')
        sys.exit(1)
        
    network_to_scan = sys.argv[1]
    scanner = NetworkScanner(network_to_scan)
    scanner.scan()