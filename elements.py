TERMINALS = ['v-line', 'h-line', 'dl-line', 'dr-line']
NON_TERMINALS = ['house', 'base', 'walls', 'roof']


class Item:
    left = None
    right = None
    top = None
    bottom = None


class Terminal:
    def __init__(self, element_type, start, stop):
        self.type = element_type
        self.start = start
        self.stop = stop
        self.left = min([start[0], stop[0]])
        self.right = max([start[0], stop[0]])
        self.top = max([start[1], stop[1]])
        self.bottom = min([start[1], stop[1]])


class NonTerminal:
    items = []
    left = None
    right = None
    top = None
    bottom = None

    def __init__(self, element_type):
        self.type = element_type

    def add_item(self, item):
        self.items.append(item)
        if self.left is None or item.left < self.left:
            self.left = item.left
        if self.right is None or item.right < self.right:
            self.right = item.right
        if self.top is None or item.top < self.top:
            self.top = item.top
        if self.bottom is None or item.bottom < self.bottom:
            self.bottom = item.bottom
