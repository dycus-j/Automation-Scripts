import subprocess
import ipaddress
import sys
import time

"""
FUNCTIONS
"""
def process_ping_result(host, output):
    """
    Processes the result of a ping command and prints the host's status.

    This function checks the return code from a completed subprocess object.
    It prints whether the host is online or offline based on that code.

    Args:
        host (ipaddress.IPv4Address): The IP address object that was pinged.
        
        output (subprocess.CompletedProcess): The object returned by the 
                                              subprocess.run() command.
    """
    if output.returncode == 0:
        print(f'✓ - {host} is ONLINE')
    else:
        print(f'X - {host} is OFFLINE`')


"""
MAIN SCRIPT
"""
#checks user provided network address argument
if len(sys.argv) < 2:
    print('Error: Please provide a network address and the prefix as an arguement.')
    print('Usage: python3 network_scanner.py 192.168.5.0/24')
    sys.exit(1)

#stores network address argument as net_addr variable
net_addr = sys.argv[1]

#try to create a network object, exit if the address is invalid
try:
    ip_net=ipaddress.ip_network(net_addr)
except ValueError:
    print(f"Error: '{net_addr}' is not a valid network address.")
    sys.exit[1]
    

net_hosts = list(ip_net.hosts())

print(f'\nScanning devices in {net_addr}...')

start_time = time.time()

for host in net_hosts:
    output = subprocess.run(
        ['ping', '-c', '2', '-W', '1', str(host)],
        capture_output=True,
        text=True
    )
    process_ping_result(host,output)
    
end_time = time.time()
duration = end_time - start_time 

print('\nScan complete.')

print(f"The scan took {duration:.2f} seconds to complete.") 