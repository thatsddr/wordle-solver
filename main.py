import random
import os
from enum import Enum


class Status(Enum):
    CORRECT = 2
    MISPLACED = 1
    WRONG = 0


class Display:
    def __init__(self):
        self.colors = {
            "white": "\u001b[37;1m",
            "black": "\u001b[30;1m",
            "green": "\u001b[32;1m",
            "reset_text": "\u001b[0m"
        }
        self.bg_colors = {
            "yellow": "\u001b[43;1m",
            "green": "\u001b[42;1m",
            "black": "\u001b[40;1m",
            "gray": "\u001b[48;5;8;1m",
            "reset": "\u001b[0m"
        }

    @staticmethod
    def clear():
        os.system('clear')

    def show(self, word: list[tuple[str, Status]]):
        output = ""
        for l in word:
            if l[1] == Status.CORRECT:
                bg = self.bg_colors['green']
            elif l[1] == Status.MISPLACED:
                bg = self.bg_colors['yellow']
            else:
                bg = self.bg_colors['gray']
            output += f"{bg} {l[0].upper()} "
        print(f"{output}{self.bg_colors['reset']}")


class Wordle:

    def __init__(self):
        with open("data/words.txt") as f:
            self.words = set(f.read().upper().splitlines())
            self.word = random.choice(tuple(self.words)).upper()
            self.guesses = []

    def show(self):
        print(self.word)

    def check_correct(self, guess):
        res = []
        word = [[letter, False] for letter in self.word]

        for i in range(len(word)):
            status = Status.WRONG

            if word[i][0] == guess[i]:
                status = Status.CORRECT
                word[i][1] = True

            elif guess[i] in self.word:
                index = self.word.index(guess[i])
                if self.word[index] != guess[index]:
                    for j in range(len(word)):
                        if guess[i] == word[j][0] and not word[j][1]:
                            status = Status.MISPLACED
                            word[j][1] = True

            res.append((guess[i], status))
        return res

    def won(self):
        if len(self.guesses) > 0:
            if self.word.upper() == self.guesses[-1].upper():
                return True
        return False

    def play(self):
        self.show()
        while not self.won() and len(self.guesses) < 6:
            d = Display()
            d.clear()
            for g in self.guesses:
                d.show(self.check_correct(g))
            new_guess = input("Type your guess: ")
            self.guesses.append(new_guess.upper())


def main():
    wordle = Wordle()
    wordle.play()


if __name__ == "__main__":
    main()

