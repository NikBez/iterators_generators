class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list.copy()

    def __iter__(self):
        return self

    def __next__(self):
        while self.list_of_lists:
            current_item = self.list_of_lists.pop(0)
            if isinstance(current_item, list):
                self.list_of_lists = current_item + self.list_of_lists
            else:
                return current_item
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(FlatIterator(list_of_lists_1),
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
