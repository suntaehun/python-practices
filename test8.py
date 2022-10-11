# 반복문
# while / for

# for i in range(0, 3) :
#     print(i)

# list1 = ["a", "b", "c"]
# for i in range(0, len(list1)) :
#     print(list1[i])

# for element in list1 :
#     print(element)

# index = 0
# while index < len(list1) :
#     print(list[index])
#     index += 1

# break / continue
# list1 = [9, 4, 2, 1, 6, 7, 5, 4, 3, 7]
# 홀수면 2배 짝수면 그냥
# 합이 20 넘으면 끝
# list1 = [9, 4, 2, 1, 6, 7, 5, 4, 3, 7]
# list2 = []
# sum1 = 0
# for el in list1 :
#     sum1 += el
    
#     if (el % 2 == 1) :
#         list2.append(el * 2)
#     else :
#         list2.append(el)
#     if sum1 > 20 :
#         break
# print(list2)

# list1 = ["안", "녕", "하", "세", "요"]
# index = 0
# hi = ""
# # while index < len(list1) :
# #     hi += list1[index]
# #     index += 1
# # print(hi)

# # for i in range(0, len(list1)) :
# #     hi += list1[i]
# # print(hi)

# for element in list1 :
#     hi += element
# print(hi)

st = "안녕하세요"
print(st[0])
for element in st :
    print(element)