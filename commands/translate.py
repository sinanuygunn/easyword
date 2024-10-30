from colorama import Fore
from components import *
from commands import addWord
from typing import Literal
from googletrans import Translator
import googletrans

_AllLangCodes = googletrans.LANGUAGES.keys()

class getAllLangCodes:
    def __init__(self):
        print("")
        print(f"{Fore.GREEN}All Supported Languages{Fore.RESET}")
        print(f"{Fore.GREEN}------------------------{Fore.RESET}")
        print("")
        for lang, name in googletrans.LANGUAGES.items():
            print(f"{Fore.LIGHTGREEN_EX}{lang} {Fore.GREEN}({name}){Fore.RESET  }")

class translateWord:
    def __init__(self, wordName: str, toLang: str):
        print(f"{Fore.LIGHTBLACK_EX}...{Fore.RESET}")
        wordName = str(wordName).lower()
        toLang = str(toLang).lower()
        if toLang not in _AllLangCodes:
            print(f"{Fore.RED}Language {Fore.LIGHTRED_EX}{toLang}{Fore.RED} not found.{Fore.RESET}")
            return
        translatedWord = str(self.translateWord(wordName, toLang)[1])
        print(f"{Fore.GREEN}{wordName.capitalize()} -> {Fore.LIGHTGREEN_EX}{translatedWord.capitalize()} (Translated to {toLang.upper()}) {Fore.RESET}")
        print()
        answ = input(f"{Fore.LIGHTBLACK_EX}Wanna add this word to your dictionary? ({Fore.LIGHTGREEN_EX}Y{Fore.RESET}/{Fore.LIGHTRED_EX}N{Fore.RESET}{Fore.LIGHTBLACK_EX}){Fore.RESET}")
        if answ.lower() == "y" or answ.lower() == "yes":
            addWord(wordName, translatedWord)
        else:
            print(f"{Fore.LIGHTBLACK_EX}Word {wordName} not added.{Fore.RESET}")

    def translateWord(self, wordName: str, toLang: str) -> list:
        beforeTrans = wordName
        translator = Translator()
        translatedWord = translator.translate(wordName, dest=toLang).text
        return [beforeTrans, translatedWord]
    

