from Wordle import Wordle
from Solver import Solver


def main():
    wordle = Wordle()
    solver = Solver()

    while not wordle.won():
        solver.update()
        a = wordle.guess(solver.pick_guess())
        solver.add_guess(a)


if __name__ == "__main__":
    main()

