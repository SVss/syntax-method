from enum import Enum


class Type(Enum):
    # Terminals
    VERTICAL = 'v-line'
    HORIZONTAL = 'h-line'
    DIAGONAL_LEFT = 'dl-line'
    DIAGONAL_RIGHT = 'dr-line'

    # NonTerminals
    HOUSE = 'house'
    BASE = 'base'
    RECT = 'rect'
    WALLS = 'walls'
    ROOF = 'roof'

    @staticmethod
    def get_type(start, stop):
        if start[0] == stop[0]:
            result = Type.VERTICAL
        elif start[1] == stop[1]:
            result = Type.HORIZONTAL
        else:
            left = min([start, stop], key=lambda x: x[0])
            top = max([start, stop], key=lambda x: x[1])
            if top == left:
                result = Type.DIAGONAL_LEFT
            else:
                result = Type.DIAGONAL_RIGHT
        return result


class Terminal:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.left = min([start[0], stop[0]])
        self.right = max([start[0], stop[0]])
        self.top = max([start[1], stop[1]])
        self.bottom = min([start[1], stop[1]])
        self.type = Type.getType(start, stop)


class NonTerminal:
    items = []
    left = None
    right = None
    top = None
    bottom = None

    def __init__(self, element_type, items=[]):
        self.type = element_type
        self.items = items
        if len(items) > 0:
            self.left = min(i.left for i in items)
            self.right = max(i.right for i in items)
            self.top = max(i.top for i in items)
            self.bottom = min(i.bottom for i in items)
