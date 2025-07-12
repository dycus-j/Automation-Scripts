# Python Network Scanner

## Objective

This script uses Python to perform a ping sweep of a given network range (e.g., 192.168.64.0/24) to discover and list all active hosts.

## Technologies Used

- Python
- subprocess module
- ipaddress module
- Ubuntu Server 24.04 (as a target in a virtual lab)

## How to Use

1.  Ensure you have Python 3 installed.
2.  Run from the command line with the `> scan_results.txt` argument to generate a .txt file with the list of all host addresses and its status:
    `python3 network_scanner.py > scan_results.txt`

## What I Learned

This was my first project in building a home lab and using Python for network automation. It was a great exercise in running system commands from a script, handling program output, and understanding how to work with IP addresses in Python.
