from colorama import Fore

from components import *
class writeAllWords:
    def __init__(self):
        config = ConfigManager.getConfig("all")
        config_words = config["words"]
        printedMain = False
        print("")
        head = "All Registered Words:"
        print(head)
        print("-" * len(head))
        print("")
        for word in config_words:
            if not printedMain:
                print(f"{Fore.LIGHTBLACK_EX}Word: {Fore.LIGHTBLACK_EX}Definition{Fore.RESET}")
                printedMain = True
            print(f"{Fore.CYAN}{word}{Fore.RESET}: {Fore.GREEN}{config_words[word]}{Fore.RESET}")
        print("")