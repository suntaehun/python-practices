# 2 제일 작은수 제거하기
# def solution(arr):
#     answer = []
#     if len(arr) == 1 :
#         return [-1]
#     minNum = 10000000
#     for a in arr :
#         if a < minNum :
#             minNum = a
#     for a in arr:
#         if minNum != a:
#             answer.append(a)
#     return answer
# print(solution([10]))
# print(solution([4, 3, 2, 1]))
# # -------------------------------------
# # 1 자연수 뒤집어 배열로 만들기
# def solution(n):
#     answer = list(str(n))
#     answer.reverse()
#     answer = list(map(int,answer))
#     return answer
# print(solution(12345))
# # -------------------------------------
# # 3 두 정수 사이 합
# def solution(a, b):
#     answer = 0
#     if a < b:
#         return sum(range(a, b+1))
#     elif a > b :
#         return sum(range(b, a+1))
#     else :
#         answer = a
#     return answer
# print(solution(3, 5))
# print(solution(3, 3))
# print(solution(5, 3))
# -------------------------------------
# 4 정수 제곱근 판별
# def solution(n):
#     answer = 0
#     for i in range(1,n):
#         if i * i == n :
#             answer = (i+1) * (i+1)
#             break
#         elif i * i > n :
#             break
#     if answer == 0 :
#         return -1
#     return answer
# print(solution(121))
# print(solution(3))
# -------------------------------------
# 피보나치 수
def solution(n:int):
    answer = 1
    first = 0
    second = 1
    for i in range(2, n+1) :
        tmp = second
        answer = first + second
        first = tmp
        second = answer
    return answer % 1234567
print(solution(3))
print(solution(5))
    



