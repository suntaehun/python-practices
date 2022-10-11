from typing import overload


class Calc:
    @staticmethod       #  @ : 어노테이션
    def add(a,b):
        print(a + b)
    @staticmethod
    def diff(s, a, b):
        print("diff  3")

    @staticmethod
    def diff(s, a):
        print("diff  2")