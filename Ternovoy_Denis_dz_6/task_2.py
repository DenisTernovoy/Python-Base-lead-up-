class Road:
    mass_i = 5
    width_i = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        result = self._length * self._width * Road.mass_i * Road.width_i // 1000
        print(result, 'т')


road_1 = Road(length=4000, width=8)
road_1.asphalt()
