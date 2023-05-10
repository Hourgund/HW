class Human:
    def __init__(self, name='no name', surname='no surname', age='0', alive=True):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__alive = alive

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def name(self, surname):
        if isinstance(surname, str):
            self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age=1):
        if 0 <= 120:
            self.__age = age

    @property
    def is_alive(self):
        return "Yes" if self.__alive else "No"

    @is_alive.setter
    def is_alive(self, alive):
        if isinstance(alive, bool):
            self.__alive = alive

    def __str__(self):
        return f"{self.__name} {self.__surname}: age = {self.__age}. " \
               f"Is alive? - {self.is_alive}"
