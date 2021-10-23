from operator import itemgetter

class Book:
    #книга
    def __init__(self, id, title, year, lib_id):
        self.id = id #id книги
        self.title = title #название книги
        self.year = year #год издания
        self.lib_id = lib_id #id библиотеки

class Library:
    #библиотека
    def __init__(self, id, addr):
        self.id = id #id библиотеки
        self.addr = addr #адрес библиотеки
        
class BookInLib:
    #'книги в библиотеке' - для связи многие-ко-многим
    def __init__(self, bk_id, lib_id):
        self.bk_id = bk_id
        self.lib_id = lib_id

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

def main():
#основная функция
    #связь один-ко-многим
    one_many = [(l.addr,b.title, b.year)
        for l in librs
        for b in books
        if l.id == b.lib_id]
        
    """Г1 - список всех библиотек, адрес которых начинается с буквы А, и список книг в них"""
    print('Задание Г1')
    #отбираем удовлетворяющие условию библиотеки
    chosen_lbs = list(filter (lambda l: l.addr[0:1] == 'А', librs))
    tsk_1 = {}
    if len(chosen_lbs) > 0: 
        #для каждой выбранной библиотеки формируем список книг, которые в ней есть
        for l in chosen_lbs:
            tsk_1[l.addr] = list((i[1], i[2]) for i in one_many if i[0] == l.addr)
        print(tsk_1)
    else:
        print('нет подходящих под условие библиотек\n')

    """Г2 - список библиотек с максимальным годом издания книги
    в каждой библиотеке, отсортированный по максимальному году"""
    print('\nЗадание Г2')
    tsk_2_unsorted = [] #вспомогательный результирующий список
    for l in librs:
        #список годов издания книг в данной библиотеке
        l_yrs = list(i[2] for i in one_many if i[0] == l.addr)
        if len(l_yrs) > 0 :
            #найдём максимальный год издания
            m_year = max(l_yrs)
            #добавим пару библиотека-год к результирующему списку
            tsk_2_unsorted.append((l.addr, m_year))
    #отсортируем результирующий список
    tsk_2 = sorted(tsk_2_unsorted, key = itemgetter(1), reverse = True)
    print(tsk_2)

    """Г3 - вывести список всех связанных книг и библиотек,
    отсортированный по библиотекам (связь многие-ко-многим)"""
    print('\nЗадание Г3')
     #свяжем названия книг и id библиотек, в которых они есть,
     #на основе элементов списка bk_in_lbs
    many_many_temp = [(b.title, e.lib_id)
        for b in books
        for e in bk_in_lbs
        if b.id == e.bk_id]
    #теперь вместо id библиотек подставим их адреса   
    many_many = [(i[0], l.addr)
        for i in many_many_temp
        for l in librs
        if l.id == i[1]]
    tsk_3 = sorted(many_many, key = itemgetter(1), reverse = True)
    print(tsk_3)

if __name__ == '__main__':
    main()
