import requests
from colorama import Fore, init
import socket
import ctypes
from threading import Thread

ctypes.windll.kernel32.SetConsoleTitleW("Nitro Fucker - Discord Nitro Checker | By ManiacX0")
init(autoreset=True)
name = socket.gethostname()

print(Fore.CYAN + """
                                )                                                              
                             ( /(         )              (       )               )             
                             )\()) (   ( /( (            )\   ( /(    (       ( /(    (   (    
                            ((_)\  )\  )\()))(    (    (((_)  )\())  ))\  (   )\())  ))\  )(   
                             _((_)((_)(_))/(()\   )\   )\___ ((_)\  /((_) )\ ((_)\  /((_)(()\  
                            | \| | (_)| |_  ((_) ((_) ((/ __|| |(_)(_))  ((_)| |(_)(_))   ((_) 
                            | .` | | ||  _|| '_|/ _ \  | (__ | ' \ / -_)/ _| | / / / -_) | '_| 
                            |_|\_| |_| \__||_|  \___/   \___||_||_|\___|\__| |_\_\ \___| |_|           
                                            (((((((((((((((((((((((((((((((((((
                                            (((((((((((((((((((((((((((((((((((
                                            (((((((((((((((((((((((((((((((((((
                                            (((((((((((((((((((((((((((((((((((
                                            ((((((((                    (((((((
                                            (((((((                      ((((((
                                            ((((((                        (((((
                                            (((((      (((((    ((((*      ((((
                                            (((((       (((,    /(((       ((((
                                            (((((                          ((((
                                            ((((((.      (((/../(((      *(((((
                                            (((((((((((((((((((((((((((((((((((
                                            (((((((((((((((((((((((((((((((((((
                                            (((((((((((((((((((((((((((((((((((                         
""")
print(Fore.LIGHTCYAN_EX + "\t\t\t\tBy ManiacX0 - Cracked.to: ManiacX0 | Discord.gg/yxc3KqNf6e")

print(Fore.MAGENTA + "\nWelcome " + Fore.CYAN + f"{name} !\n")

print(Fore.LIGHTCYAN_EX + "Threads amount: ")
threads = int(input("\n> "))
print(Fore.LIGHTCYAN_EX + "\n> Starting threads...\n")

proxys = open("proxies.txt", "r")
proxys = proxys.readlines()


nitro = open("nitro.txt", "r")
nitrosplit = nitro.readlines()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip,deflate,br',
            'accept-language': 'fr,en-US;q=0.9,en;q=0.8'
            }

def Spamming(req, proxys):
    while True:
        ncodes = 0
        for proxy in proxys:
            ReqSess = requests.Session()
            try:
                req = ReqSess.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitrosplit[ncodes]}?with_application=false&with_subscription_plan=true", proxies = {'https': 'socks4://' + proxy}, timeout=5, headers = headers)
                if req.status_code == 404:
                    print(Fore.LIGHTGREEN_EX + "[V] >>", nitrosplit[ncodes])
                    with open("Nitro Hit.txt", "a") as results:
                        results.write(nitrosplit[ncodes])
                        del nitrosplit[ncodes]
                    ncodes = ncodes + 1

                elif req.status_code == 200:
                    print(Fore.LIGHTRED_EX + "[X] >>", nitrosplit[ncodes])
                    del nitrosplit[ncodes]
                    ncodes = ncodes + 1

                elif req.status_code == 429:
                    continue

            except Exception as e:
                continue

req = ""

for i in range(threads):
    t = Thread(target=Spamming, args=(req, proxys))
    t.start()
    t.join(0.3)
