from computer import Computer
from computer_creator import Computer_Creator


class Manager:
    @staticmethod
    def most_expensive(computer):
        Max = max(computer.price, 100000)

        return Max

    @staticmethod
    def less_expensive(computer):
        Min = min(computer.price, 0)

        return Min
