print("Q1.")
a = [1,1,2,3,4,2,1,4,5,6,7,8,10]

setA = set(a)
a = list(setA)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
print()

print("Q2.")
a = {"name": "park", "score": 70}
b = {"name": "kim", "score": 80}
c = {"name": "park", "score": 50}

print("%s는 점수가 80이상이 %s"%( a["name"], a["score"] >= 80))
print("%s는 점수가 80이상이 %s"%( b["name"], b["score"] >= 80))
print("%s는 점수가 80이상이 %s"%( c["name"], c["score"] >= 80))
print()






print("Q3.")
a = {"name": "kim", "money": 50000}
b = {"name": "park", "money": 30000}

print("%s 는 %s 보다 %d 있습니다." %(a["name"], b["name"], a["money"]-b["money"]))
print("%s 는 %s 보다 %d 있습니다." %(b["name"], a["name"], b["money"]-a["money"]))

print("%s 이랑 %s 이랑 합 %d 있습니다." %(a["name"], b["name"], a["money"]+b["money"]))
print("둘의 평균은 %d 입니다." %((a["money"]+b["money"])/2))