from elements import Item

class Operator:
    def can_apply(self, items_list):
        raise NotImplementedError()

    def generate_for(self, item):
        raise NotImplementedError()


class Left(Operator):
    def can_apply(self, items_list):
        assert len(items_list) == 2
        return items_list[0].right <= items_list[1].left


class Above(Operator):
    def can_apply(self, items_list):
        assert len(items_list) == 2
        return items_list[0].bottom >= items_list[1].top


class Inside(Operator):
    def can_apply(self, items_list):
        assert len(items_list) == 2
        inner = items_list[0]
        outer = items_list[1]
        return inner.top < outer.top \
            and inner.bottom > outer.bottom \
            and inner.left > outer.left \
            and inner.right < outer.right
