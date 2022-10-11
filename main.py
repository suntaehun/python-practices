# main 내가 실행시킬 것
# java는 무조건 main -> start

# package 묶음
from User.age import showAge
from User.name import showName
from calculator.add import add
from calculator.cal import Calc
from calculator.diff import diff
from calculator.person import Person

from test4.input import testInput



def main():
    # count = 0
    # count = add(count, 4)
    # count = diff(count, 10)
    # print(count)
    # text = testInput()
    # print(text)
    # showName("park")
    # showAge(21)

    # a = Person()
    # b = Person()
    c = Person()
    # print(a.count)
    # print(b.count)
    print(c.count)
    c.printCount()
    c.printCount2()
    

main()