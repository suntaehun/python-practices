# 반복문
a = ["a", "b", "c", "d", "e"]

# 0 <= i < len(a)
# for i in range(0, len(a)) :
#     print(i)
#     print(a[i])

# for i in a:
#     print(i)

# re = 0
# while re < 5:
#     print(a[re])
#     re += 1

b = [1, 2, 3, 4, 5]
re = 0
while True:
    print("True")
    if (b[re] % 2 == 0):
        break
    re += 1
    
for i in a:
    if i =="c":
        break
    print(i)