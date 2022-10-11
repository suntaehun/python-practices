# 2부터 20까지 짝수 합
# answer = 0
# i = 2
# while i <= 20 :
#     if i % 2 == 0:
#         answer += i
#     i += 1
# print(answer)

# for index in range(2, 21) :
#     if i % 2 == 0:
#         answer += i
# print(answer)
# ----------------------------
# 구구단 만들기
# for i in range(1, 10) :
#     for j in range(1, 10) :
#         print(f"{i} X {j} = {i*j}")
#     print()
# ----------------------------
# 2부터 30까지 소수 뽑기 1
list3 = []
for i in range(2, 31) :
    a = 1
    for j in range(2, i) :
        a *= i % j
    if a != 0 :
        list3.append(i)
print(list3)
# ----------------------------
# 2부터 30까지 소수 뽑기 2
answer = []
for i in range(2, 31) :
    isPrimary = True
    for j in range(2, i) :
        if i%j == 0 :
            isPrimary = False
            break
    if isPrimary :
        answer.append(i)
print(answer)

# 별찍기
# text = "*"
# for  i in range(2, 7) :
#     st = ""
#     for j in range(0, i) :
#         st = (text * j)
#     print(st)