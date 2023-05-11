from computer import Computer
from manager import Manager
from computer_creator import Computer_Creator

ls = Computer_Creator.create()

for computer in ls:
    print(computer)

expensive = Manager.most_expensive(ls)
cheap = Manager.less_expensive(ls)

print(f"Expensive - {expensive}")
print(f"Cheap - {cheap}")
