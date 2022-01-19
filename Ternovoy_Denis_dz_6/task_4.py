class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed == 0:
            self.speed = 70

        print(f'Машина {self.name} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'Машина {self.name} остановилась')
        self.speed = 0

    def turn(self, side):
        print(f' Машина {self.name} повернула на{side}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости! ({self.speed})')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости! ({self.speed})')
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


car_1 = Car(speed=90, color ='red', name='car_1', is_police=False)
car_1.go()
car_1.show_speed()
car_1.stop()
car_1.show_speed()
car_1.go()