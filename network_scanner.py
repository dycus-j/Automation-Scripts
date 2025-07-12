import subprocess
import ipaddress
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


net_addr = '192.168.64.0/24'
ip_net = ipaddress.ip_network(net_addr)
net_hosts = list(ip_net.hosts())

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