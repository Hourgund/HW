from human import Human
from manager import Manager
from creat_human import HumanCreator

ls = HumanCreator.create()

for human in ls:
    print(human)

adult = Manager.count_adult(ls)
underage = Manager.count_underage(ls)

print(f"Adult - {adult}")
print(f"Underage - {underage}")
