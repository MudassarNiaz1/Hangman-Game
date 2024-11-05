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


    def main(self):
        while self.is_running:
            self.display_man()
            self.display_hint()
            guess_word = input("Enter a letter: ").lower()

            if len(guess_word) != 1 or not guess_word.isalpha():
                print("Please enter a single letter.")
                continue

            if guess_word in self.guessed_letters:
                print(f"{guess_word} has already been guessed.")
                continue

            self.guessed_letters.append(guess_word)

            if guess_word in self.answer:
                for i in range(len(self.answer)):
                    if self.answer[i] == guess_word:
                        self.hint[i] = guess_word
            else:
                self.wrong_guess += 1

            if "_" not in self.hint:
                self.display_man()
                self.display_answer()
                print("Congratulations, you won!")
                self.is_running = False
            elif self.wrong_guess >= len(self.hangman_art) - 1:
                self.display_man()
                self.display_answer()
                print(f"Game Over, you lost! The word was '{self.answer}'.")
                self.is_running = False


    def display_man(self):
        print("****Welcome to the Game****")
        for i in HangmanGame.hangman_art [self.wrong_guess]:
            print(i)
        print("*********")

    def display_hint(self):
        print(" ".join(self.hint))

    def display_answer(self):
        print(" ".join(self.answer))