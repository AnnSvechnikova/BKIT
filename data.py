from library import Library
from book import Book
from bookinlib import BookInLib
#список библиотек
librs = [
    Library(1, 'Алтайская улица, 4'),
    Library(2, 'Цветной бульвар, 2'),
    Library(3, 'Авиамоторная улица, 8'),
]

#список книг
books = [
    Book(1, 'Лунный камень', 1868, 1),
    Book(2, 'Шум и ярость', 1929, 2),
    Book(3, 'Гордость и предубеждение', 1813, 3),
    Book(4, 'Портрет Дориана Грея', 1890, 1),
    Book(5, 'Хлеб по водам', 1981, 3),
]

#список связей многие-ко-многим
bk_in_lbs = [
    BookInLib(1, 1),
    BookInLib(1, 2),
    BookInLib(2, 3),
    BookInLib(3, 1),
    BookInLib(4, 1),
    BookInLib(5, 2),
]
# связь один-ко-многим
one_many = [(l.addr, b.title, b.year)
                for l in librs
                for b in books
                if l.id == b.lib_id]

# свяжем названия книг и id библиотек, в которых они есть,
# на основе элементов списка bk_in_lbs
many_many_temp = [(b.title, e.lib_id)
                  for b in books
                  for e in bk_in_lbs
                  if b.id == e.bk_id]
# теперь вместо id библиотек подставим их адреса
many_many = [(i[0], l.addr)
             for i in many_many_temp
             for l in librs
             if l.id == i[1]]