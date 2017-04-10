from elements import *
from basic_rules import *


class RoofRule(Rule):
    def can_apply(self, items_list):
        assert len(items_list) == 2
        if items_list[0].type != Type.DIAGONAL_RIGHT:
            list.reverse(items_list)
        return items_list[0].type == Type.DIAGONAL_RIGHT \
            and items_list[1].type == Type.DIAGONAL_LEFT \
            and LeftRule().can_apply(items_list)

    def apply(self, items_list):
        if self.can_apply(items_list):
            return NonTerminal(Type.ROOF, items_list)
        else:
            return False


class WallsRule(Rule):
    def can_apply(self, items_list):
        assert len(items_list) == 2
        result = items_list[0].type == Type.VERTICAL \
            and items_list[1].type == Type.VERTICAL
        if not result:
            return False
        result = LeftRule().can_apply(items_list)
        if not result:
            list.reverse(items_list)
            result = LeftRule().can_apply(items_list)
        return result

    def apply(self, items_list):
        if self.can_apply(items_list):
            return NonTerminal(Type.WALLS, items_list)
        else:
            return False


class BaseRule(Rule):
    def can_apply(self, items_list):
        assert len(items_list) == 2
        if items_list[0].type != Type.WALLS:
            list.reverse(items_list)
        return items_list[0].type == Type.WALLS \
            and items_list[1].type == Type.HORIZONTAL \
            and AboveRule().can_apply(items_list)

    def apply(self, items_list):
        if self.can_apply(items_list):
            return NonTerminal(Type.BASE, items_list)
        else:
            return False


class RectRule(Rule):
    def can_apply(self, items_list):
        assert len(items_list) == 2
        if items_list[0].type != Type.HORIZONTAL:
            list.reverse(items_list)
        return items_list[0].type == Type.HORIZONTAL \
            and items_list[1].type == Type.BASE \
            and AboveRule().can_apply(items_list)

    def apply(self, items_list):
        if self.can_apply(items_list):
            return NonTerminal(Type.RECT, items_list)
        else:
            return False


class HouseRule(Rule):
    def can_apply(self, items_list):
        assert len(items_list) == 2
        if items_list[0].type != Type.ROOF:
            list.reverse(items_list)
        return items_list[0].type == Type.ROOF \
            and items_list[1].type == Type.RECT \
            and AboveRule().can_apply(items_list)

    def apply(self, items_list):
        if self.can_apply(items_list):
            return NonTerminal(Type.HOUSE, items_list)
        else:
            return False
