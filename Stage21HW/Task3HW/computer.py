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

    @property
    def model(self):
        return self.__model

    @model.setter
    def brand(self, model):
        if isinstance(model, str):
            self.__model = model

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price=1):
        if 0 <= 1000000:
            self.__price = price

    def __str__(self):
        return f"{self.__brand}, model: {self.__model} and has price {self.__price}."

    @model.setter
    def model(self, value):
        self._model = value
