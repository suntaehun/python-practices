# 제어문
a = 10
b = 10
# print(f"a > b {a > b}")
str1 = ""
if a > b:
    str1 = "크다."
    # print(f"a > b 크다")
elif a < b:
    str1 = "작다."
    # print(f"a < b 작다")
else:
    str1 = "같다."
print(f"a 가 b {str1}")

c = [1, 2, 3, 4, 5]
if len(c) > 3:
    print(c[0])
if len(c) > 2:
    print(c[0])