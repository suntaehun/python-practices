tmpd = {"name":"re", "age":100}
list = [tmpd]
list1 = list
list2 = list.copy()
list3 = [tmpd.copy()]

print("list")
print(list)
print("list1")
print(list1)
print("list2")
print(list2)
print("list3")
print(list3)
print()

list.append(1)
print("list")
print(list)
print("list1")
print(list1)
print("list2")
print(list2)
print("list3")
print(list3)
print()

tmpd["name"] = "lee"
print("list")
print(list)
print("list1")
print(list1)
print("list2")
print(list2)
print("list3")
print(list3)
print()
print("www1")
print("www2")
print("www3")