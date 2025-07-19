# Python Network Scanner - v1.2

## Objective
A command-line tool that uses Python to perform a high-speed, parallel ping sweep of a given network range to discover and list all active hosts.

## Features
* **High-Speed Parallel Scanning:** Utilizes the `multiprocessing` library to scan all hosts simultaneously, dramatically reducing scan time.
* **Performance Benchmarking:** Includes a timer to measure and display the total scan time.
* **Graceful Exit:** The script can be stopped at any time with `Control + C` without a messy error message by handling the `KeyboardInterrupt` exception.
* **Robust Input Handling:** Accepts the network address as a command-line argument and includes validation for missing or invalid input.
* **Clear Output:** Reports a clean list of online hosts and provides a "No hosts found" message if the network is empty.

## Technologies Used
* Python
* `multiprocessing`, `subprocess`, `ipaddress`, `sys`, `time` modules

## How to Use
1.  Ensure you have Python 3 installed.
2.  Run the script from the command line, providing the network address you wish to scan as an argument.

    ```
    python3 network_scanner.py 192.168.64.0/24
    ```

## Version History
* **v1.2 (Current):** Refactored the core scanning logic to use the `multiprocessing` library for parallel execution. Added `try/except` block to handle keyboard interrupts.
* **v1.1:** Converted the script into a flexible command-line tool with argument parsing, error handling, and a performance timer.
* **v1.0:** Initial basic, sequential network scanner.
