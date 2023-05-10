from computer import Computer
from manager import Manager
from computer_creator import ComputerCreator

ls = ComputerCreator.create()

for computer in ls:
    print(computer)