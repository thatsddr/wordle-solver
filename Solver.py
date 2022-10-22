from utils import Status
import string


class Solver:

    def __init__(self):
        with open("data/words.txt") as f:
            self.words = set(f.read().upper().splitlines())
            self.guesses: list[list[touple[string, Status]]] = []
            self.correct_letters = {}
            self.misplaced_letters = []
            self.letter_frequency = dict.fromkeys(string.ascii_uppercase, 0)
            self.words_score = {}

    def add_guess(self, guess: list[tuple[str, Status]]):
        if guess:
            self.guesses.append(guess)
            self.misplaced_letters = []
            for i in range(len(guess)):
                if guess[i][1] == Status.CORRECT:
                    self.correct_letters[i] = guess[i][0]
                if guess[i][1] == Status.MISPLACED:
                    self.misplaced_letters.append(guess[i][1])
            self.update_word_list()
            self.calculate_frequency()
            self.calculate_words_score()

    def is_correct_letter(self, letter):
        for l in self.correct_letters:
            if self.correct_letters[l] == letter:
                return True
        return False

    def update_word_list(self):
        for guess in self.guesses:

            for i in range(len(guess)):
                if guess[i][1] == Status.WRONG:
                    for w in self.words.copy():
                        # if it's not a correct letter and it is in the word, and is not misplaced, remove the word
                        if not self.is_correct_letter(guess[i][0]) and guess[i][0] in w and guess[i][0] and guess[i][0] not in self.misplaced_letters:
                            self.words.remove(w)
                        # otherwise only remove if it's in a non-correct position and it is not a misplaced letter
                        elif guess[i][0] in w and guess[i][0] not in self.misplaced_letters:
                            correct_indexes = []
                            for j in self.correct_letters:
                                if self.correct_letters[j] == guess[i][0]:
                                    correct_indexes.append(j)
                            if w.index(guess[i][0]) not in correct_indexes:
                                self.words.remove(w)

                elif guess[i][1] == Status.MISPLACED:
                    for w in self.words.copy():
                        if w[i] == guess[i][0]:
                            self.words.remove(w)

                else:
                    for w in self.words.copy():
                        if w[i] != guess[i][0]:
                            self.words.remove(w)

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
        print(list(self.words_score.keys())[0:10])

    def pick_word(self):
        return
