from elements import Type
from extended_rules import *
from syntax_method import analyze

INPUT_ROOF = [
    Terminal(Type.DIAGONAL_RIGHT, [0, 0], [10, 10]),
    Terminal(Type.DIAGONAL_LEFT, [10, 10], [20, 0])
]

INPUT_RECT = [
    Terminal(Type.VERTICAL, [0, 0], [0, 10]),
    Terminal(Type.VERTICAL, [10, 0], [10, 10]),
    Terminal(Type.HORIZONTAL, [0, 0], [10, 0]),
    Terminal(Type.HORIZONTAL, [0, 10], [10, 10])
]

ROOF_GRAMMAR = [
    RoofRule()
]

RECT_GRAMMAR = [
    WallsRule(), BaseRule(), RectRule()
]

def main():
    print(analyze(INPUT_ROOF, ROOF_GRAMMAR))
    print(analyze(INPUT_RECT, ROOF_GRAMMAR))
    print(analyze(INPUT_RECT, RECT_GRAMMAR))

if __name__ == '__main__':
    main()
