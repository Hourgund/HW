from computer import Computer


class Manager:
    @staticmethod
    def most_expensive(computer):
        Max = max(computer.price, 1000000)

        return Max

    @staticmethod
    def less_expensive(computer):
        Min = min(computer.price, 1)

        return Min
