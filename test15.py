from datetime import date
from functools import reduce


print(date.today())

# 람다
list1 = [9, 1, 2, 4, 3]
def sum(x,y):
    print(f"{x}  {y}")    #format
    return x+y

a = reduce(lambda x,y: sum(x , y), list1)

user = {"id":"id", "pass":"pass","name":""}
names = ["kim", "lee", "park"]
namelist = list(map(lambda x : {"id":"id","pass":"pass","name" : x, "age":30}, names))
print(namelist)

findUser = list(filter(lambda x : x.get("name")=="park", namelist))
print(findUser)
avgAge = reduce(lambda x,y: x+y.get("age"), namelist, 0)
print(avgAge/len(namelist))

# 1 자연수 뒤집어 배열로 만들기
# 2 제일 작은수 제거하기
# 3 두 정수 사이 합
# 4 정수 제곱근 판별