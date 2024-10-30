from components import *
from colorama import Fore

class editWord:
    def __init__(self, wordName: str, value):
        wordName = wordName.lower()
        config = ConfigManager.getConfig("all")
        config_words = config["words"]
        if wordName in config_words:
            oldvalue = config_words[wordName]
            config_words[wordName] = str(value)
            ConfigManager.writeConfig("words", config_words)
            print(f"{Fore.GREEN}Word {Fore.LIGHTGREEN_EX}{wordName}{Fore.GREEN} edited. ({wordName}: {oldvalue} -> {value}){Fore.RESET}")
        else:
            print(f"{Fore.RED}Word {Fore.LIGHTRED_EX}{wordName}{Fore.RED} not found.{Fore.RESET}")