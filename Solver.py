from utils import Status


class Solver:

    def __init__(self):
        with open("data/words.txt") as f:
            self.words = set(f.read().upper().splitlines())
            self.guesses: list[list[touple[string, Status]]] = []
            self.correct_letters = {}

    def add_guess(self, guess: list[tuple[str, Status]]):
        if guess:
            self.guesses.append(guess)
            for i in range(len(guess)):
                if guess[i][1] == Status.CORRECT:
                    self.correct_letters[i] = guess[i][0]
            self.update_word_list()

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
                        # if it's not a correct letter and it is in the word, remove the word
                        if not self.is_correct_letter(guess[i][0]) and guess[i][0] in w:
                            self.words.remove(w)
                        # otherwise only remove if it's in a non-correct position
                        elif guess[i][0] in w:
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

                print(len(self.words))

