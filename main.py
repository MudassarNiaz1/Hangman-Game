import random

from functions import HangmanGame


def main():
  game = HangmanGame()
  while game.is_running:
      game.display_man()
      game.display_hint()
 #  game.display_answer()
      guess_word = input("Enter a letter: ").lower()

      if len(guess_word) != 1 or not guess_word.isalpha():
       print("Please enter a single letter.")
       continue

      if guess_word in game.guessed_letters:
       print(f"{guess_word} has already been guessed.")
       continue

      game.guessed_letters.append(guess_word)

      if guess_word in game.answer:
        for i in range(len(game.answer)):
          if game.answer[i] == guess_word:
            game.hint[i] = guess_word
      else:
         game.wrong_guess += 1

      if "_" not in game.hint:
                game.display_man()
                game.display_answer()
                print("Congratulations, you won!")
                game.is_running = False
      elif game.wrong_guess >= len(game.hangman_art) - 1:
         game.display_man()
         game.display_answer()
         print(f"Game Over, you lost! The word was '{game.answer}'.")
         game.is_running = False


if __name__ == '__main__':
    main()
