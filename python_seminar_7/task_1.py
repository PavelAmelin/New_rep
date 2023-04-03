from time import sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        for k in self.__color:
            print(k)
            sleep(self.__color[k])

light = TrafficLight(color={
    'Red': 7,
    'Yellow': 2,
    'Green': 7})

light.running()

