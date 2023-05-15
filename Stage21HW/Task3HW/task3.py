from computer import Computer
from manager import Manager
from computer_creator import Computer_Creator

ls = Computer_Creator.create()

for computer in ls:
    print(computer)

expensive = Manager.most_expensive(computer.price)
cheap = Manager.less_expensive(computer.price)

print(f"Expensive - {expensive}")
print(f"Cheap - {cheap}")
