import subprocess
import ipaddress
import sys
import time

def get_network_address():
    """Gets the network address string from the command line."""
    if len(sys.argv) < 2:
        print('Error: Please provide a network address as an argument.')
        print('Usage: python3 network_scanner.py 192.168.1.0/24')
        sys.exit(1)
    return sys.argv[1]

def validate_network_address(net_addr):
    """Validates the network address string and returns a network object."""
    try:
        ip_net = ipaddress.ip_network(net_addr)
        return ip_net
    except ValueError:
        print(f"Error: '{net_addr}' is not a valid network address.")
        sys.exit(1)

def process_ping_result(host, output):
    """Processes the result of a ping command and prints the host's status."""
    if output.returncode == 0:
        print(f'✓ - {host} is ONLINE')
        return True
    else:
        return False

def main():
    """Main driving function for network scanner."""
    # Get the user's input string
    net_addr = get_network_address()
    
    # Pass the string to the validation function to get a network object
    ip_net = validate_network_address(net_addr)
    
    # Prepare for the scan
    net_hosts = list(ip_net.hosts())
    online_hosts_count = 0

    print(f'\nScanning devices in {ip_net.with_prefixlen}...')
    start_time = time.time()

    for host in net_hosts:
        output = subprocess.run(
            ['ping', '-c', '2', '-W', '1', str(host)],
            capture_output=True,
            text=True
        )
        if process_ping_result(host, output):
            online_hosts_count += 1
    
    end_time = time.time()
    duration = end_time - start_time 

    if online_hosts_count == 0:
        print("\nNo online hosts found.")

    print('\nScan complete.')
    print(f"The scan took {duration:.2f} seconds to complete.") 
    
if __name__ == "__main__":
    main()