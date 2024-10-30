from components import *
from colorama import Fore

class removeAllWords:
    def __init__(self):
        config = ConfigManager.getConfig("all")
        config_words = config["words"]
        config_words = {}
        while True:
            print(Fore.RED + "--- WARNING ---")
            print(Fore.RESET)
            print(Fore.YELLOW + "Are you sure you want to remove all words? (Y/N)" + Fore.RESET)
            print(Fore.RESET)
            print(Fore.RED + "--- WARNING ---")
            print(Fore.LIGHTBLACK_EX)
            answer = str(input())
            print(Fore.RESET)
            if answer.lower() == "y" or answer.lower() == "yes":
                ConfigManager.writeConfig("words", config_words)
                print(Fore.GREEN + "All words removed." + Fore.RESET)
                print("")
                break
            elif answer.lower() == "n" or answer.lower() == "no":
                print(Fore.GREEN + "All words not removed." + Fore.RESET)
                print("")
                break
            else:
                print(Fore.RED + "Invalid input. Please try again." + Fore.RESET)
                print("")