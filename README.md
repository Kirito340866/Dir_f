# Dir_f

Welcome to Dir_r, a powerful, clean, and highly optimized command-line utility designed for automated security testing and target reconnaissance.

Developed and maintained by Kirito340866.

---

## Tools Included

### 1. MK1 Directory Finder (v1.0)
A fast, memory-efficient multi-threaded web content discovery tool written in Python. It scans targets for hidden directories and endpoints while actively filtering out wildcard/fake responses.

#### Key Features:
* Multi-Threaded Performance: Dynamically adjust your speed using Python's ThreadPoolExecutor.
* Wildcard/Fake Response Filtering: Automatically detects and isolates fake 200/404 pages by calculating the base response size dynamically.
* Memory-Safe Batching: Streams large wordlists in 500-line segments to maintain an incredibly low RAM footprint.
* Clean CLI Output: Gracefully handles keyboard interrupts and silences background thread connection errors.

---

## Requirements & Installation

Make sure you are on your Kali Linux machine (or any system running Python 3) and install the required dependencies:

```bash
pip install requests
```
## How to Install

Follow these steps to install and set up the tool on your Linux system (Kali Linux recommended):

```bash
# 1. Clone the repository from GitHub
git clone [https://github.com/Kirito340866/MK1.git](https://github.com/Kirito340866/MK1.git)

# 2. Navigate into the project directory
cd MK1

# 3. Install the required Python dependencies
pip install requests
```
Note for Kali Linux users: If you get an error regarding "externally-managed-environment" while running pip, you can install the requests library using apt:
```bash
sudo apt install python3-requests
```
How To Use (Directory Finder)

Run the script by passing your target flags. If you do not supply optional flags, the tool automatically pulls from your system's default SecLists path.
Bash

python3 dir_finder.py -u <TARGET_URL> [options]

Available Arguments:
Short Flag	Long Flag	Description	Required / Default
-u	--url	Target Website URL (e.g., http://localhost:3000)	Required
-w	--wordlist	Custom wordlist file path	Optional / /usr/share/seclists/...
-t	--thread	Number of concurrent threads to use	Optional / 2
Execution Examples:

    Basic Scan (Uses Default Wordlist & 2 Threads):

Bash

python3 dir_finder.py -u [http://127.0.0.1:3000](http://127.0.0.1:3000)

    High-Speed Custom Scan (30 Threads + Specific Wordlist):

Bash

python3 dir_finder.py -u [http://127.0.0.1:3000](http://127.0.0.1:3000) -w custom_paths.txt -t 2

Terminal Preview Output
```Plaintext
                                                             
                           ▒▓▒▒▒▒▒▒▒▒▒▒▒▓▓                           
                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▓▒▒▒▒▒▒▒▒▒▒▓▒                 
                ▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▒            
            ▓▒▒▓▓▓▓▓████▓▒▒░             ░░▒▓▓██████▓▓▓▓▓▓▓▓▓        
         ▒▓▓▓▓▓▓████▓▓▒░                      ░▒▓██████▓▓▓▓▓▓        
       ▓▓▓▓▓▓█████▓▒░        ░ ░ ░░   ░          ░▒▓█████            
      ▓▓▓▓▓████▓▒░         ░  ░░▒▒▒▒▒░░░            ░▒█████          
      ▓▓██████▓░           ░░░▓██████▓▒░░░░░          ░▒█████        
        █████▒             ░▒▓█████████▓▒▒░░           ▒█████        
        █████▒░            ░▒███████████▓▒▒░░        ░▒▓███          
          █████▒░       ░░░░░▓█████████▓▒▒▒░░      ░▒▓█████          
      ▓▓▓▓▓▓█████▓▒░       ░░░▒▓▓███▓▓▓▒▒░░░░   ░▒▓██████▓▓▓         
       ▓▓▓▓▓▓▓██████▓░░░  ░░░░░░░▒▒▒▒▒░▒▒░░░░░▒▒▓██████▓▓▓▓▓▓        
          ▓▓▓▓▓▓▓██████▓▓▒░░░▒░░▒░▒▒▒▒▒▒▒▒▒▒▓███████▓▓▓▓▓▓▓          
              ▓▓▓▓▓▓█████████▓▓▓▓▓▓▓▓▓▓██████████▓▓▓▒▓▓              
                   ▓▒▒▓▓▓████████████████████▓▓▓▓                    
                          ▓▓▓▓████████████                                                                                     


========[Dir Finder]========

[*] Version: 1.0

[*] Created By: Kirito340866

============================

[*] Target:     http://localhost:3000
[*] Wordlist:   custom_paths.txt
[*] Thread:     2

[/] Start Finding...


[/] Fake Response is Detected:           Size: 9903 Bytes

[+] http://localhost:3000/profile                       Status Code: 500
[+] http://localhost:3000/api                   Status Code: 500

```
Educational Disclaimer

This suite is developed and distributed strictly for educational purposes, authorized penetration testing, and home lab vulnerability research. Do not execute these tools against any production network or environment without explicit, written, and legal authorization from the owner. The developer accepts no liability for misuse, legal ramifications, or collateral damage.
