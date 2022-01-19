import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(traffic_light.__color)
        if self.__color == 'red':
            time.sleep(7)
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            time.sleep(2)
            self.__color = 'green'
        else:
            time.sleep(5)
            self.__color = 'red'


traffic_light = TrafficLight('yellow')

while True:
    traffic_light.running()
