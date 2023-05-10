from computer import Computer
from manager import Manager
from computer_creator import ComputerCreator

ls = ComputerCreator.create()

for computer in ls:
    print(computer)

adult = Manager.count_adult(ls)
underage = Manager.count_underage(ls)

print(f"Adult - {adult}")
print(f"Underage - {underage}")