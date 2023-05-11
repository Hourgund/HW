import random
import string

from computer import Computer


class Computer_Creator:
    @staticmethod
    def create(size=6):
        computers = []
        BRAND = ("Apple", "Lenovo", "MSI", "Acer", "ASUS", "HP")
        # MODEL = ("1", "2", "3", "4", "5", "6")
        MAX_PRICE = 1000000
        MIN_PRICE = 1

        for _ in range(size):
            computer = Computer()
            computer.brand = random.choice(BRAND)
            # computer.model = random.choice(MODEL)
            computer.price = random.randint(MIN_PRICE, MAX_PRICE)
            computers.append(computer)

        return computers
