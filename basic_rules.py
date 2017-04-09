from elements import Item

class Rule:
    @staticmethod
    def can_apply(items_list):
        raise NotImplementedError()

    @staticmethod
    def generate_for(item):
        raise NotImplementedError()


class LeftRule(Rule):
    @staticmethod
    def can_apply(items_list):
        assert len(items_list) == 2
        return items_list[0].right < items_list[1].left


class UpRule(Rule):
    @staticmethod
    def can_apply(items_list):
        assert len(items_list) == 2
        return items_list[0].bottom > items_list[1].top


class InsideRule(Rule):
    @staticmethod
    def can_apply(items_list):
        assert len(items_list) == 2
        inner = items_list[0]
        outer = items_list[1]
        return inner.top < outer.top \
            and inner.bottom > outer.bottom \
            and inner.left > outer.left \
            and inner.right < outer.right
