from utils import Status
import string


class Solver:

    def __init__(self):
        with open("data/words.txt") as f:
            self.words = set(f.read().upper().splitlines())
            self.guesses: list[list[touple[string, Status]]] = []
            self.correct_letters = {}
            self.misplaced_letters = []
            self.wrong_letters = []
            self.letter_frequency = dict.fromkeys(string.ascii_uppercase, 0)
            self.words_score = {}

    def add_guess(self, guess: list[tuple[str, Status]]):
        if guess:
            self.guesses.append(guess)
            self.misplaced_letters = []
            for i in range(len(guess)):
                if guess[i][1] == Status.CORRECT:
                    self.correct_letters[i] = guess[i][0]
                elif guess[i][1] == Status.MISPLACED:
                    self.misplaced_letters.append(guess[i][0])
                else:
                    self.wrong_letters.append(guess[i][0])
            self.update_word_list()
            self.calculate_frequency()
            self.calculate_words_score()

    def is_correct_letter(self, letter):
        for l in self.correct_letters:
            if self.correct_letters[l] == letter:
                return True
        return False

    def is_misplaced_letter(self, letter):
        return letter in self.misplaced_letters

    def update_word_list(self):
        for guess in self.guesses:
            for i in range(len(guess)):

                l, s = guess[i]
                if s == Status.WRONG:
                    for w in self.words.copy():
                        # if the letter is in the word, it's not a correct letter, and is not misplaced, remove the word
                        if l in w and not self.is_correct_letter(l) and not self.is_misplaced_letter(l):
                            self.words.remove(w)
                        # otherwise only remove words where the letter is at the current index
                        elif l in w and not self.is_misplaced_letter(l) and w[i] == l:
                            self.words.remove(w)

                elif s == Status.MISPLACED:
                    for w in self.words.copy():
                        # remove words where the letter is in that position and in words that don't contain it
                        if w[i] == l or l not in w:
                            self.words.remove(w)

                elif s == Status.CORRECT:
                    for w in self.words.copy():
                        # remove all words that don't have letters in correct position
                        if w[i] != l:
                            self.words.remove(w)
        print(sorted(list(self.words)), len(self.words))

    def calculate_frequency(self):
        self.letter_frequency = dict.fromkeys(string.ascii_uppercase, 0)
        for word in self.words:
            for letter in word:
                self.letter_frequency[letter] += 1

    def calculate_words_score(self):
        self.words_score = dict.fromkeys(self.words, 0)
        for word in self.words:
            letters_counted = []
            for letter in word:
                if letter not in letters_counted:
                    self.words_score[word] += self.letter_frequency[letter]
                    letters_counted.append(letter)
        self.words_score = dict(sorted(self.words_score.items(), key=lambda item: -item[1]))
        # print(list(self.words_score.keys())[0:10])

    def pick_word(self):
        return
