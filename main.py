from elements import *
from syntax_method import analyze

INPUT = [
    Terminal(Type.DIAGONAL_RIGHT, [0, 0], [10, 10]),
    Terminal(Type.DIAGONAL_LEFT, [10, 10], [20, 0])
]

def main():
    print(analyze(INPUT))

if __name__ == '__main__':
    main()
