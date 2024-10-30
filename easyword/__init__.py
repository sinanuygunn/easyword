import sys
import os
import argparse
from colorama import Fore

from commands import *
from components import *

parser = argparse.ArgumentParser(
                    prog='easyword',
                    description='Learn words easily with a simple word management tool',
                    epilog='Author: github.com/sinanuygunn'
                    )

parser.add_argument('-aw', '--addword', help="adds a word to the database", nargs=2, metavar=("WORD", "MEANING"))
parser.add_argument('-ew', '--editword', help="edits given word to given value in the database", nargs=2, metavar=("WORD", "MEANING"))
parser.add_argument('-rw', '--removeword', help="removes a word from the database", nargs=1, metavar=("WORD"))  
parser.add_argument('-pr', '--playrandom', help="asks added questions randomly with a special algorythm", action='store', nargs='*')
parser.add_argument('-wa', '--writeallwords', help="writes all words to the terminal", action='store', nargs='*')
parser.add_argument('-tw', '--translateword', help="translates a word to given language", nargs=2, metavar=("WORD", "LANGUAGE"))
parser.add_argument('-wl', '--writelanguages', help="lists all supported languages for translation", action='store', nargs="*")
parser.add_argument('-ra', '--removeallwords', help="removes all words from the database", action='store', nargs='*')

def main():
    parsed_args = parser.parse_args()
    ConfigManager.createConfigIfExists(ConfigManager.checkConfig())
    if parsed_args.addword is not None:
        addWord(parsed_args.addword[0], parsed_args.addword[1])
    if parsed_args.editword is not None:
        editWord(parsed_args.editword[0], parsed_args.editword[1])
    if parsed_args.removeword is not None:
        removeWord(parsed_args.removeword[0])
    if parsed_args.playrandom is not None:
        playRandom()
    if parsed_args.writeallwords is not None:
        writeAllWords()
    if parsed_args.removeallwords is not None:
        removeAllWords()
    if parsed_args.translateword is not None:
        translateWord(parsed_args.translateword[0], parsed_args.translateword[1])
    if parsed_args.writelanguages is not None:
        getAllLangCodes()
    if parsed_args.writeallwords is None and parsed_args.playrandom is None and parsed_args.editword is None and parsed_args.removeword is None and parsed_args.addword is None and parsed_args.removeallwords is None and parsed_args.translateword is None and parsed_args.writelanguages is None:
        parser.print_help()
    return 0


def run():
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(Fore.RESET)
        sys.exit(0)
        pass