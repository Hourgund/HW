import random
import string

from computer import Computer


class ComputerCreator:
    @staticmethod
    def create(size=10):
        computers = []
        BRAND = ()
        MODEL = ()
        MAX_PRICE = 1000000
        MIN_PRICE = 1

        for _ in range(size):
            computer = Computer()
            computer.brand = random.choice(BRAND)
            computer.model = random.choice(MODEL)
            computer.age = random.randint(MIN_PRICE, MAX_PRICE)
            computers.append(computer)

        return computers