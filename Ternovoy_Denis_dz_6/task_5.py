class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):

    def draw(self):
        print('Выбрана ручка!')


class Pencil(Stationery):

    def draw(self):
        print('Выбран карандаш!')


class Handle(Stationery):

    def draw(self):
        print('Выбран маркер!')


pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()