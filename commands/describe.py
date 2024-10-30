from components import *
from colorama import Fore
import requests

dictApiUrl = "https://api.dictionaryapi.dev/api/v2/entries/en/"

class describe:
    def __init__(self, wordName: str):
        print(f"{Fore.LIGHTBLACK_EX}...{Fore.RESET}")
        wordName = wordName.lower()
        url = dictApiUrl + wordName
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json()[0]["meanings"][0]["definitions"][0]["definition"])
            print(f"{Fore.LIGHTBLACK_EX}...{Fore.RESET}")
        else:
            print(f"{Fore.RED}Word {Fore.LIGHTRED_EX}{wordName}{Fore.RED} not found.{Fore.RESET}")