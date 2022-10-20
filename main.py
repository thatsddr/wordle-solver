from Wordle import Wordle
from Solver import Solver


def main():
    wordle = Wordle()
    solver = Solver()

    wordle.show()
    while not wordle.won():
        a = wordle.guess(input("guess: "))
        solver.add_guess(a)
    #wordle.play()


if __name__ == "__main__":
    main()

