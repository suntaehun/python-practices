# 함수
# define 정의 / return 반환
# 파이썬 : 절차지향
# 자바   : 객체지향
# isPrimaryKey = True / cammel case
# is_primary_key = True / snake case

# def sum(a,b) :      # a,b 매개변수
#     return a + b
    
# print(sum(1,2))     # a,b 인수
# # argument 매개변수
# def sum1(*args) :
#     print(args)
#     pppp = 0
#     for arg in args :
#         pppp += arg
#     return pppp
# print(sum1(1, 1, 1, 1, 1, 1))
# #-----------------------------------------
# def printFunc(**kwargs) :
#     print(kwargs)
# printFunc(a = 1, b = 1)
# #-----------------------------------------
# def makeHuman(name, age) :
#     return {"name" : name, "age" : age}
# human1 = makeHuman("kim", 30)
# human2 = makeHuman("park", 34)
# print(human1)
# print(human2)
#-----------------------------------------
def isPrimaryNumber(*nums) :
    for num in nums :
        isPrimary = True
        for j in range(2, num) :
            if num % j == 0 :
                isPrimary = False
                break
        if isPrimary :
            print(f"{num}은 소수입니다.")
        else :
            print(f"{num}은 소수가 아닙니다.")

isPrimaryNumber(7, 14, 19, 77)
#-----------------------------------------
name = "park"   # 전역변수
name1 = "lee"      # 전역변수
def setName1(name) :
    print(f"2. {name}")
    name1 = name
    name = name     # 지역변수
    print(f"3. {name}")
print(f"1. name1 : {name1}")
print(f"1. {name}")
setName1("kim")
print(f"4. {name}")
print(f"2. name1 : {name1}")
# -----------------------------------------
