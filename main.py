import random
import os
import webbrowser
import time
import json
from functools import wraps

import romanNumToArabNum
import arabNumToRomanNum
from custom_errors import *

__author__ = "ElBretzel_"
__version__ = "v1.0"


os.chdir(os.path.abspath(os.path.dirname(__file__)))

TXT_FILE = "list.txt"
JSON_FILE = "ratio.json"

arabConverter = lambda i: romanNumToArabNum.roman_to_arab(i)
romanConverter = lambda i: arabNumToRomanNum.arab_to_roman(i)

def writting_data(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        print("Trying to write data...\nDo not close the program.")
        func(*args, **kwargs)
        t2 = time.time()
        print(f"Done in {round(t2-t1, 3)} seconds!")

    return wrapper

def get_result(gess: str, number: object):
    if gess == "roman":
        print("Gess the roman number of", number)
        return romanConverter(number)
    print("Gess the arab number of", romanConverter(number))
    return number

@writting_data
def write_json(new_score: dict) -> None:
    with open(f"{JSON_FILE}", 'w') as file:
        json.dump(new_score, file)

@writting_data
def write_text():
    with open(TXT_FILE, 'w') as f:
        f.write('\n'.join(f"{i} - {romanConverter(i)}" for i in range(1,4000)))

def read_json():

    if not os.path.exists(JSON_FILE):
        write_json({"win":0,"loss":0})

    with open(f"{JSON_FILE}", 'r') as r:
        return json.load(r)

class Main:
    
    text_menu = ["1 - Arabic numeral --> Roman numeral.", "2 - Roman numeral --> Arabic numeral.", "3 - Random roman numeral.",
             "4 - Write roman numeral from 1 to 3999.", "5 - Gess the arabic numeral.", "6 - Guess the roman numeral.",
             "7 - Ratio Correct/Wrong answer.", "8 - My other projects (Github).", "\n9 - Leave."]
    main_title = "Arab / Roman number tool."
    
    def __init__(self):
        self._answer = None
        self.ratio = None
        self.init_main_menu
        
    @property
    def answer(self):
        return self._answer
    
    @answer.setter
    def answer(self, value):
        if not value.isdigit():
            raise MenuNotInteger(value)
        elif int(value) not in range(1, len(self.text_menu)+1):
            raise MenuOutOfRange(value)
        self._answer = int(value)
        
    @property
    def reset_main_menu(self):
        self._show_main_menu
        self.answer = input("> ")
        os.system("cls")
        self.ratio = read_json()
        
    @property
    def _show_main_menu(self):
        print("{:^100}".format(self.main_title), end="\n\n")
        print("\n".join(self.text_menu))
    
    def gessgame(self, gess: str, *args):
        
        def user_failed(gess, *args):
            if gess == "roman":
                print(f"In arabic numeral, you have found {arabConverter(answer)}.")
            else:
                print(f"In roman numeral, you have found {romanConverter(answer)}.")
            
        
        rand = random.randint(1,3999)
        conversion = str(get_result(gess, rand)) # ? Get the expected answer
        t1 = time.time()
        answer = input("> ")
        t2 = time.time()
        if answer == conversion:
            self.ratio["win"] += 1
            print(f"[{round(t2-t1, 3)}s] Good job, the answer was {conversion}.")
        else:
            self.ratio["loss"] += 1
            print(f"[{round(t2-t1, 3)}s] You failed, the right answer was {conversion}.")
            user_failed(gess, answer) # ? Print what the user found 
        write_json(self.ratio) # ? Change the ratio
             
    @property
    def init_main_menu(self):
        
        while True:
            self.reset_main_menu
            
            if self.answer == 1:
                print("Output:", arabNumToRomanNum.arab_to_roman())
            elif self.answer == 2:
                print("Output:", romanNumToArabNum.roman_to_arab())
            elif self.answer == 3:
                rand = random.randint(1,3999)
                print(f"Output: {rand} - {romanConverter(rand)}")
            elif self.answer == 4:
                write_text()
            elif self.answer == 5:
                self.gessgame("arab")
            elif self.answer == 6:
                self.gessgame("roman")
            elif self.answer == 7:
                if self.ratio['win'] == self.ratio['loss'] == 0:
                    print("You have no saved scores...")
                else:
                    print(f"Ratio Correct/Wrong answer: {round(self.ratio['win']/(self.ratio['loss']+self.ratio['win']), 2)}/{round(self.ratio['loss']/(self.ratio['win']+self.ratio['loss']), 2)}")
            elif self.answer == 8: webbrowser.open(r"https://github.com/ElBretzel/")
            elif self.answer == 9: break
            
            
if __name__ == "__main__":
    main = Main()