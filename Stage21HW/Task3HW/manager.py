from computer import Computer


class Manager:
    @staticmethod
    def find_most_expensive(computers):
        if isinstance(computers, (list, tuple)):
            count = 0

            for computer in computers:
                if isinstance(computer, Computer) and computer.price.max:
                    count += 1

            return count

    @staticmethod
    def find_less_expensive(computers):
        total = len(computers)
        total -= Manager.count_adult(com)
        return total