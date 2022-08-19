import requests, os, time
from colorama import Fore

os.system('title WebHook Deleter Author: clayze#9999')

webhook = input("Enter webhook url -> ")

requests.delete(webhook)
print('webhook deleted')
time.sleep(10)
