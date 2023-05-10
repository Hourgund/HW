class Computer:
    def __init__(self, brand='no brand', model='no model', price='0'):
        self.__brand = brand
        self.__model = model
        self.__price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand

