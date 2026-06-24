import requests
from concurrent.futures import ThreadPoolExecutor
import argparse
print("""                                                             
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
v1.0      
""")
print("\n========[Dir Finder]========\n")
print("[*] Version: 1.0\n")
print("[*] Created By: Kirito340866")
print("\n============================\n")
parser = argparse.ArgumentParser(description="Hidden paths Finder (or) Dir finder")
parser.add_argument('-u','--url',required=True,help="Target Url (e.g: http://127.0.0.1:3000)")
parser.add_argument('-w','--wordlist',help="File path for wordlist(e.g: /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt)",default="/usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt")
parser.add_argument('-t','--thread',help="Number Of Thread, Deafult: 2", default=2)
flited = parser.parse_args()
word_list = flited.wordlist
target = flited.url
fake_response_length = None
def fake_response_finder():
        global fake_response_length
        try:
                fake_url = f"{target}/alkdfiaoijeoijlkfja;lkdfoiejfjajdoj--=3=+d==dlkd?kdlfka?jdkfa=ld"
                fake_result = requests.get(fake_url)
                fake_response_length = len(fake_result.text)
                print(f"[/] Fake Response is Detected:           Size: {len(fake_result.text)} Bytes\n")
        except Exception as e:
                return None
def finder(doors):
        global fake_response_length
        try:
                clean_door = doors.strip()
                combine_url = f"{target}/{clean_door}"
                result = requests.get(combine_url,timeout=5)
                if result.status_code in [200,300,301,500]:
                        if len(result.text) == fake_response_length:
                                pass
                        else:
                                print(f"[+] {combine_url}                       Status Code: {result.status_code}")
                else:
                        pass
        except Exception as e:
                return None
def main():
        print(f"[*] Target:     {flited.url}")
        print(f"[*] Wordlist:   {flited.wordlist}")
        print(f"[*] Thread:     {flited.thread}\n")
        print(f"[/] Start Finding...\n\n")
        fake_response_finder()
        try:
                with open(word_list,'r') as d_file:
                        file_end = False
                        while not file_end:
                                door_list = []
                                for u in range(500):
                                        line = d_file.readline()
                                        if not line:
                                                file_end = True
                                                break
                                        if line.strip():
                                                door_list.append(line.strip())
                                with ThreadPoolExecutor(max_workers=int(flited.thread)) as executor:
                                        executor.map(finder,door_list)
        except KeyboardInterrupt:
                print("[-] Exiting...")
                exit()
        except Exception as e:
                print(f"[-] Error: {e}")
main()
