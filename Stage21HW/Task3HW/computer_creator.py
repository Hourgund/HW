import random
import string

from computer import Computer


class Computer_Creator:
    @staticmethod
    def create(size=10):
        computers = []
        BRAND = ("Apple", "Lenovo", "MSI", "Acer", "ASUS", "HP")
        MODEL = ("6", "18", "2000", "20", "7", "10")
        MAX_PRICE = 1000000
        MIN_PRICE = 1

        for _ in range(size):
            computer = Computer()
            computer.model = random.choice(MODEL)
            computer.brand = random.choice(BRAND)
            computer.price = random.randint(MIN_PRICE, MAX_PRICE)
            computers.append(computer)

        return computers
