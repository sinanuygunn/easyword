from components import *
from colorama import Fore

class removeWord:
    def __init__(self, wordName: str):
        wordName = wordName.lower()
        config = ConfigManager.getConfig("all")
        config_words = config["words"]
        if wordName in config_words:
            oldvalue = config_words[wordName]
            del config_words[wordName]
            ConfigManager.writeConfig("words", config_words)
            print(f"{Fore.GREEN}Word {Fore.LIGHTGREEN_EX}{wordName}{Fore.GREEN} removed. ({wordName}: {oldvalue}){Fore.RESET}")
        else:
            print(f"{Fore.RED}Word {Fore.LIGHTRED_EX}{wordName}{Fore.RED} not found.{Fore.RESET}")