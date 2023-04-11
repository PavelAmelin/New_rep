class OnlyInt:

    def __set__(self, instance, value):
        if type(value) is not int:
            raise ValueError('данные атрибуты могут быть только числами')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class OnlyStr:

    def __set__(self, instance, value):
        if type(value) is not str:
            raise ValueError('данные атрибуты могут иметь только строковый тип данных')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Worker:
    name = OnlyStr()
    surname = OnlyStr()
    position = OnlyStr()
    wage = OnlyInt()
    bonus = OnlyInt()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus

    def total_wage(self):
        return self.wage + self.bonus

obj = Worker('Ivan', 'Ivanov', 'Developer', 200000, 50000)
print(obj.total_wage())

class DictKeyVal:

    def __set__(self, instance, value):
        for k in value:
            if type(k) is not str or type(value[k]) is not int:
                raise ValueError('ключи атрибута могут быть только строками, а значения только числами')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

from time import sleep

class TrafficLight:
    __color = DictKeyVal()
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