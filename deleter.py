import os
import requests
from TextColor import ColorText


os.system("title WebHook deleter Author: clayze#9999")


def Webhook():
    webhook_link = input("Insert webhook url: ")

    response = requests.delete(webhook_link)

    if response.status_code >= 200 or response <= 299:
        print(ColorText.green + "Success" + ColorText.reset)
    else:
        print(ColorText.red + "Error" + ColorText.reset)


if __name__ == "__main__":
    Webhook()
