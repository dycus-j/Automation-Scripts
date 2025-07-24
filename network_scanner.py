import subprocess
import ipaddress
import sys
import time
import multiprocessing

# === WORKER FUNCTION ===
# The multiprocessing Pool needs a simple, standalone function to give to its workers.
def ping_worker(host):
    """
    Pings a single host to see if it's online. This is the "job" that each
    of our parallel processes will be doing.

    Args:
        host (ipaddress.IPv4Address): The IP address object for a single host.

    Returns:
        tuple: A tuple containing the host and a boolean (True if online, False if offline).
    """
    try:
        # We use subprocess.run() to execute the 'ping' command.
        # 'check=True' automatically raises an error if the ping fails.
        subprocess.run(
            ['ping', '-c', '1', '-W', '1', str(host)],
            capture_output=True, text=True, check=True
        )
        return (host, True)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        # If the ping fails, we catch the error and know the host is offline.
        return (host, False)

# === THE MAIN CONTROLLER ===
# Used a class to organize all the logic into a reusable "scanner" object.
class NetworkScanner:

    def __init__(self, net_addr):
        # This constructor runs automatically when we create a new NetworkScanner object.
        # Its job is to validate the user's input and set up our initial variables.
        try:
            self.ip_net = ipaddress.ip_network(net_addr)
            self.net_hosts = list(self.ip_net.hosts())
        except ValueError:
            print(f"Error: '{net_addr}' is not a valid network address.")
            sys.exit(1)
            
    def scan(self):
        # This is the main public method. It orchestrates the entire scan, 
        # from starting the timer to printing the results.
        print(f'\nScanning {len(self.net_hosts)} devices in {self.ip_net.with_prefixlen}...')
        start_time = time.time()
        
        # We create a 'Pool' of worker processes to use all available CPU cores.
        with multiprocessing.Pool() as pool:
            # pool.map() distributes the work and collects the results.
            results = pool.map(ping_worker, self.net_hosts)

        # We use a list comprehension to create a new list of only the online hosts.
        online_hosts = [host for host, status in results if status]
        
        end_time = time.time()
        duration = end_time - start_time
        
        self._print_results(online_hosts, duration)

    def _print_results(self, online_hosts, duration):
        # Prints a formatted summary of the scan results
        print("\n--- Online Hosts ---")
        if online_hosts:
            for host in online_hosts:
                print(f'✓ - {host} is ONLINE')
        else:
            print("No online hosts found.")
            
        print('\nScan complete.')
        print(f"The scan took {duration:.2f} seconds to complete.") 

# This standard guard ensures that the code inside only runs when the script
# is executed directly from the terminal. It's essential for multiprocessing.
if __name__ == "__main__":
    
    # --- Argument Parsing ---
    if len(sys.argv) < 2:
        print('Error: Please provide a network address as an argument.')
        print('Usage: python3 network_scanner.py 192.168.1.0/24')
        sys.exit(1)
        
    network_to_scan = sys.argv[1]
    
    # --- Execution ---
    scanner = NetworkScanner(network_to_scan)
    scanner.scan()
