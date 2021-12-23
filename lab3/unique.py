# Итератор для удаления дубликатов
import numbers


class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.items = items
        if isinstance(self.items, list):
            self.items_len = len(items)
        else:
            self.items_len = 0;
        self.ignore_case = kwargs.get('ignore_case', False)
        self.set = set()
        self.index = 0

    def __next__(self):
        elem = None
        while True:
            if isinstance(self.items, list):
                if self.index < self.items_len:
                    elem = self.items[self.index]
                    if isinstance(elem, numbers.Number):
                        self.ignore_case = True
                    self.index += 1
                    if self.ignore_case and elem not in self.set:
                        self.set.add(elem)
                        return elem
                    elif not self.ignore_case and elem.lower() not in self.set:
                        self.set.add(elem.lower())
                        return elem
                else:
                    raise StopIteration
            else:
                elem = next(self.items)
                if self.ignore_case and elem not in self.set:
                    self.set.add(elem)
                    return elem
                elif not self.ignore_case and elem.lower() not in self.set:
                    self.set.add(elem.lower())
                    return elem

    def __iter__(self):
        return self


if __name__ == "__main__":
    lst1 = ['a', 'b', 'A', 'B']
    lst2 = [1, 2, 1, 2, 3]
    for i in Unique(lst1):
        print(i)
    for i in Unique(lst2):
        print(i)