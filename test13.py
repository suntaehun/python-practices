# 계산기 만들기 ~~~~~~~~~~~~

# def add(a,b):
#     return a+b
# def diff(a,b):
#     return a-b

# i = 0
# i = add(i, 10)
# i = diff(i, 5)
# print(i)
# j = 0
# j = add(j, 10)
# j = diff(j, 5)
# print(j)

# class

# class Calculator:
#     def __init__(self) -> None: #초기값 설정
#         self.result = 0

#     def add(self,b):
#         self.result += b

#     def diff(self,b):
#         self.result -= b


# 모듈
# from cal import Calculator

from animal import Animal
from cat import Cat
from dog import Dog
from human import Human
from leg import Leg
from arm import Arm
from user import User

# cal1 = Calculator()
# cal1.add(10)
# cal1.diff(5)
# print(f"cal1\t{cal1.result}")
# cal2 = Calculator()
# cal2.add(10)
# cal2.diff(2)
# print(f"cal2\t{cal2.result}")
# cal3 = Calculator()
# cal3.add(10)
# cal3.diff(2)
# print(f"cal3\t{cal3.result}")

# -------------------------------------------
# user1 = User("bit","123123")
# user1.printUser()
# user1.change_id("kkk")
# user1.printUser()

# -------------------------------------------
# l = Leg("left", "park")
# print(l.side)
# print(l.name)
# l.setName("kim")
# print(l.name)
# -------------------------------------------

# an = Animal()
# print(an.name)
# an.__setattr__("name", "?")
# print(an.name)
# print(an.__dict__)

cat = Cat()
cat.printSound()
print(cat.name)
print(cat.butler)

dog = Dog()
dog.printSound()
print(dog.name)
print(dog.master)

# human = {"name":"park", "age":45, "gender": "남자"}
