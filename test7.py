# 제어문
# a = 5
# b = 2
# if a > b :
#     print(f"{a}는 {b}보다 크다.")
# elif a < b :
#     print(f"{a}는 {b}보다 작다.")
# else :
#     print(f"{a}는 {b}와 같다.")

# x = {"company": "카카오", "isPartTime": True}
# if x.get("company") == "카카오" or x.get("company") == "네이버":
#     if x.get("isPartTime") :
#         print("대기업 비정규직원입니다.")
#     else :
#         print("대기업 정규직원입니다.")
# else :
#     print("중견기업 직원입니다.")

# match x.get("company") :
#     case "카카오" :
#         print("대기업 직원입니다.")
#     case "네이버" :
#         print("대기업 직원입니다.")
#     case _ :
#         print("중견기업 직원입니다.")

# phone = {"name": "갤럭시", "version": "플립"}
# phone이 애플이면 와우
# 갤럭시면 version보고 플립이면 접히네요 아니면 좋네요
phone = {"name": "갤럭시", "version": "플립"}
if phone.get("name") == "아이폰" :
    print("와우")
elif phone.get("name") == "갤럭시":
    if phone.get("version") == "플립":
        print("접히네요.")
    else :
        print("좋네요.")