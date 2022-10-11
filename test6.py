# list = [1, 2, 3, 4, 5 ,6 ,2 ,3 ,5 ,1]
# 짝수 홀수 찾기
# list1 = [1, 2, 3, 4, 5 ,6 ,2 ,3 ,5 ,1]
# for el in list1:
#     if (el % 2 == 0):
#         print(f"{el}는 짝수입니다.")
#     else:
#         print(f"{el}는 홀수입니다.")

# i = 0
# print()
# while i < len(list1):
#     if (list1[i] % 2 == 0):
#         print(f"{list1[i]}는 짝수입니다.")
#     else:
#         print(f"{list1[i]}는 홀수입니다.")
#     i += 1
# print()
# for el in list1:
#     match el % 2:
#         case 1:
#             print(f"{el}는 홀수입니다.")
#         case 0:
#             print(f"{el}는 홀수입니다.")

# 람다 버전3.6부터
# 예제) list1의 요소 2배
# list1 = [1, 2, 3, 4, 5 ,6 ,2 ,3 ,5 ,1]
# list2 = []
# for el in list1:
#     list2.append(el * 2)
# print(list2)
# # map : 새로운 리스트 만든다.(반환한다.)
# list3 = list(map(lambda el: el * 2, list1))
# print(list3)

# tmpd = {"name": "re", "age": 100}
# list4 = [tmpd, tmpd, tmpd]
# list5 = list(map(lambda el: el.copy(), list4))
# list6 = list4.copy()
# print(list4)
# print(list5)
# print(list6)
# list4.append(1)
# print()
# print(list4)
# print(list5)
# print(list6)
# tmpd["age"] = 10
# print()
# print(list4)
# print(list5)
# print(list6)



# list1 요소의 합
# from functools import reduce


# list1 = [1, 2, 3, 4, 5 ,6 ,2 ,3 ,5 ,1]
# sum = 0
# for el in list1:
#     sum += el
# print(sum)
# # 합계구할때
# sum2 = reduce(lambda x,y: x + y, list1)
# print(sum2)

# 4이상
list1 = [1, 2, 3, 4, 5 ,6 ,2 ,3 ,5 ,1]
list0 = []
for el in list1:
    if el >= 4:
        list0.append(el)
print(list0)

list01 = list(filter(lambda x: x >= 4, list1))
print(list01)