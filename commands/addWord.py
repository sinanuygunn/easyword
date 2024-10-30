from components import *
from colorama import Fore
class addWord:
    def __init__(self, wordName: str, value):
        wordName = wordName.lower()
        config = ConfigManager.getConfig("all")
        config_words = config["words"]
        if wordName in config_words:
            print(f"{Fore.RED}Word {Fore.LIGHTRED_EX}{wordName}{Fore.RED} already exists.{Fore.RESET}")
            return
        else:
            config_words[wordName] = str(value)
            ConfigManager.writeConfig("words", config_words)
            print(f"{Fore.GREEN}Word {Fore.LIGHTGREEN_EX}{wordName} {Fore.GREEN}added. {Fore.GREEN}({wordName}: {value}){Fore.RESET}")