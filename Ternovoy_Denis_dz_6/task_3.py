class Worker:
    wage = 0
    bonus = 0

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход: {self.wage + self.bonus}')


scientist = Position(name='Сергей', surname='Белов', wage=30000, bonus=10000, position='Учитель')
scientist.get_full_name()
scientist.get_total_income()