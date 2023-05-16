import random
import string

from human import Human


class HumanCreator:
    @staticmethod
    def create(size=10):
        humans = []
        NAMES = ("Alex", "Peter", "Garry", "Alice", "Vladimir",
                 "Olga", "Anna", "Kate", "Victor", "Max")
        SURNAMES = ("Volgavich", "Oreshik", "Bubich", "Strelkini", "Scelitarik",
                    "Durkina", "Arenishko", "Zelelenovich", "Arcusho", "Blabla")
        MAX_AGE = 120
        MIN_AGE = 1

        for _ in range(size):
            human = Human()
            human.name = random.choice(NAMES)
            human.surname = random.choice(SURNAMES)
            human.age = random.randint(MIN_AGE, MAX_AGE)
            human.is_alive = random.choice((True, False))
            humans.append(human)

        return humans
