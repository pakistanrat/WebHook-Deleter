import requests, os, logging, time
from colorama import Fore

os.system('title WebHook Deleter Author: clayze#9999')
logging.basicConfig(level=logging.INFO, format=f"{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} %(message)s{Fore.RESET}", datefmt=f"%H:%M:%S")

webhook = input("Enter webhook url -> ")

requests.delete(webhook)
print('webhook deleted')
time.sleep(10)
