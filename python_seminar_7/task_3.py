class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f'{self.get_full_name()}\n{str(self.get_total_income())}'

worker_data = Position('Ivan', 'Ivanov', 'Developer', 200000, 50000)
print(worker_data)
