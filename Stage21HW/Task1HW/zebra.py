from animal import Animal


class Zebra(Animal):
    def __init__(self, name="no name"):
        super().__init__(name)
        self.__state = True
        # tRUE - black
        # False - white

    def get_stripe(self):
        msg = "black line" if self.__state else "white line"
        msg += f" from {self.name} zebra"
        self.__state = not self.__state

        return msg

    def __str__(self):
        return (super().__str__()
                + f" State of Zebra - "
                + ("black line." if self.__state else "white line."))