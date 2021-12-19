class BookInLib:
    #'книги в библиотеке' - для связи многие-ко-многим
    def __init__(self, bk_id, lib_id):
        self.bk_id = bk_id
        self.lib_id = lib_id