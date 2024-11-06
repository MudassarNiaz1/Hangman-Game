import random

from words_list import words


class HangmanGame:
    hangman_art = { 0: ["   ",
                   "   ",
                   "   "],
                1: [" o ",
                   "   ",
                   "   "],
                2: [" o ",
                    " | ",
                    "   "],
                3: [" o ",
                    "/| ",
                    "   "],
                4: [" o ",
                    "/|\\",  # use single back slash that is an escape sequence
                    "   "],
                5: [" o ",
                    "/|\\",
                    "/  "],
                6: [" o ",
                    "/|\\",
                    "/ \\"]}
    def __init__(self):
       self.answer = random.choice(words)
       self.hint = ['_'] * len(self.answer)
       self.wrong_guess = 0
       self.guessed_letters = []
       self.is_running = True
       

    def display_man(self):
        print("****Welcome to the Game****")
        for i in HangmanGame.hangman_art [self.wrong_guess]:
            print(i)
        print("*********")

    def display_hint(self):
        print(" ".join(self.hint))

    def display_answer(self):
        print(" ".join(self.answer))
