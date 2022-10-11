# 코딩테스크 (1.백준 2.프로그래머스)

# def solution(num):
#     answer = ''
#     if num % 2 == 0 :
#         answer = 'Even'
#     else :
#         answer = 'Odd'
#     return answer
# print(solution(3))
# print(solution(4))
#---------------------------------
# def sum(a, b) :
#     try :
#         if type(a) == int and type(b) == int :
#             return a + b
#         else :
#             return int(a) + int(b)
#     except :
#         return f"{a} , {b} 중 숫자가 아닌게 있습니다."

# a = input("a 입력하세요 :")
# b = input("b 입력하세요 :")
# print(sum(a, b))
# #-----------------------------------------
# while True :
#     a = input("a 입력하세요 :")
#     if a == "end" :
#         break
#     b = input("b 입력하세요 :")
#     if b == "end" :
#         break
    
#     print(sum(a, b))
#     #-----------------------------------------
# 3.6.9게임
# def game() :
#     i = 0
#     while True : 
#         i += 1
#         myInput = input(f"현재 값 {i} ")
#         answer = str(i + 1)
#         for c in str(i + 1) :
#             if c == '3' or c == '6' or c == '9' :
#                 answer = 'c'
#         if myInput == answer :
#             print("맞았다.")
#         else :
#             print("gmae over")
#             break
# game()
#     #-----------------------------------------
# def game(cur, myInput) :
#         answer = str(cur)
#         for c in str(cur) :
#             if c == '3' or c == '6' or c == '9' :
#                 answer = 'c'
#         if myInput == answer :
#             print("맞았다.")
#             return True
#         else :
#             print("gmae over")
#             return False
# i = 0
# while True :
#     i += 1
#     myInput = input(f"현재 값 {i} ")
#     isWin = game(i+1, myInput)
#     if (not isWin):
#         break
#     #-----------------------------------------
# 뒤 4자리 빼고 핸드폰 번호 가리기 
# input 으로 받아서
# def solution(phone_number):
#     answer = ''
#     for i in range(0, len(phone_number)) :
#         if i < len(phone_number) - 4 :
#             if phone_number[i] == "-" :
#                 answer += "-"
#             else :
#                 answer += '*'
#         else :
#             answer += phone_number[i]
#     return answer

# number = input("번호 입력 :")
# print(solution(number))
#     #-----------------------------------------
# 파일 입출력
# 상대경로(내 위치에서 -> 하고싶은곳)
# . 현재위치 c/test
# ..c
# . 현재위치 c/test/test1
# ..test12.py
# 절대경로

# f = open("./123.txt",'w')
# f.write("""파이썬
# 빅데이터
# AI""")
# f.close()

# f = open("./test.txt",'r')
# lines = f.readlines()
# for line in lines :
#     print(line)
# f.close()


# fr = open("./888.txt",'r', encoding="UTF-8")
# lines = fr.readlines()
# # for line in lines :
# #     print(line)
# fr.close()

# fw = open("./888.txt",'w',encoding="UTF-8")
# for line in lines :
#     line = line.strip()
#     if line == "한글":
#         fw.write("ML")
#     elif line =="쓰기":
#         fw.write("글쓰기")
#     else:
#         fw.write(f"{line}")
#     fw.write("\n")
# fw.close()
#------------------------------------------
fr = open("./888.txt",'r', encoding="UTF-8")
lines = fr.readlines()
fr.close()

fww = open("./888.txt",'w',encoding="UTF-8")
for line in lines : 
    update_text = input(f" 전 문장 : {line}\n 바꿀문장(취소는 c) :\t")
    if update_text == 'c' :
        fww.write(line.strip())
    else:
        fww.write(update_text)
    fww.write("\n")
fww.close()