import random
from components import *
import os
from colorama import Fore, Style

class playRandom:
    def __init__(self):
        config = ConfigManager.getConfig("all")
        words = list(config["words"].items())
        wrong_answers = []  
        ask_count = 0       
        next_wrong_question = random.randint(0, 5)
        rounds = len(words) 

        # Messages written by ChatGpt
        correct_messages = [
            "Great job!", "Excellent!", "You're on fire!", "Keep it up!", 
            "Well done!", "That's perfect!", "Amazing!", "Spot on!", 
            "You're getting better!", "Impressive!", "You nailed it!", 
            "Outstanding!", "Bravo!", "Fantastic!", "Superb!", 
            "Marvelous!", "Spectacular!", "You're a genius!", "Nice work!", 
            "Keep going!"
        ]
        incorrect_messages = [
            "Try again.", "Try again next time.", "Don't give up!", 
            "Close, but not quite.", "Better luck next time.", 
            "Keep practicing!", "It's okay, you'll get it!", 
            "No worries, try again!", "Not quite, but you're improving!", 
            "Almost there, keep at it!", "Don't worry, mistakes happen!", 
            "It's all part of the learning process.", "You'll get it next time!",
            "Not quite, but keep going!", "Oops, wrong one!", "You can do better!",
            "Not this time, but keep pushing!", "Keep trying!", "That's okay, keep practicing!", 
            "You'll nail it next time!"
        ]

        while rounds > 0 or wrong_answers:  
            if ask_count >= next_wrong_question and wrong_answers:
                word, correct_answer = wrong_answers.pop(0)
                next_wrong_question = random.randint(0, 5) 
            else:
                if rounds > 0:
                    word, correct_answer = random.choice(words)
                    words.remove((word, correct_answer)) 
                    rounds -= 1
                else:
                    word, correct_answer = wrong_answers.pop(0) 

            ask_count += 1
            os.system("cls")
            print(f"What is the translation of: {Fore.CYAN}{word}{Fore.RESET}?")
            user_answer = input("Your answer: " + Fore.MAGENTA).lower()
            print(Fore.RESET)

            if user_answer == correct_answer:
                print(Fore.LIGHTGREEN_EX + random.choice(correct_messages) + Fore.RESET) 
                print(Fore.GREEN + "The correct answer is: " + Fore.GREEN + correct_answer + Fore.RESET)
                print("")
                input(Fore.LIGHTBLACK_EX + "Press enter to learn another word..." + Fore.RESET)  
            else:
                print(f"{Fore.RED}Oops, wrong answer. The correct answer is: {Fore.GREEN}{correct_answer}{Fore.RED}.{Fore.RESET}")
                print(Fore.LIGHTBLACK_EX + random.choice(incorrect_messages)) 
                print(Fore.RESET)
                wrong_answers.append((word, correct_answer))
                input(Fore.LIGHTBLACK_EX + "Press enter to learn another word..." + Fore.RESET)  
