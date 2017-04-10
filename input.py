from elements import *

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

INPUT_HOUSE = [
    Terminal(Type.DIAGONAL_RIGHT, [0, 10], [5, 15]),
    Terminal(Type.DIAGONAL_LEFT, [5, 15], [10, 10]),

    Terminal(Type.HORIZONTAL, [0, 10], [10, 10]),
    Terminal(Type.VERTICAL, [0, 0], [0, 10]),
    Terminal(Type.VERTICAL, [10, 0], [10, 10]),
    Terminal(Type.HORIZONTAL, [0, 0], [10, 0])
]
