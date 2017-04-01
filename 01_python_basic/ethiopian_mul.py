# # 1. 풀이
# # 1-1 유저에게 숫자 입력 받기
# num = int(input("숫자 1을 입력하세요 : "))
# num2 = int(input("숫자 2를 입력하세요 : "))
#
# # 1-2 result 변수 초기화
# result = 0
#
# # 1-3 반복
# while True :
#     if num % 2 : # num이 홀수 일때
#         result += num2
#
#     num = num // 2
#     num2 = num2 * 2
#
#     if num == 0:
#         print(result)
#         break

# 2. 개선 (연산하는 과정을 함수로 뺴기)
# 2-1. user input
num = int(input("숫자 1을 입력하세요 : "))
num2 = int(input("숫자 2를 입력하세요 : "))

#2-2. Define process
def mul(x):
    return x * 2

def div(x):
    return x // 2

def even(x): # 짝수면 True 홀수면 False
    return not x % 2

#2-3. Main process
result = 0
while True:
    if even(num):
        result += num2

    num = div(num)
    num2 = mul(num2)

    if num == 0:
        print(result)
        break

# # 5. 선생님 풀이
#
# # Define process
# def half(x):
#     return x // 2
#
# def double(x):
#     return x * 2
#
# def even(x):
#     return not x % 2 # 2로 나눈 나머지의 반대 값이 출력, 홀수 : 0 or 짝수 : 1
#
# # user input
# numset = str(input('type two number with space: ')).split()
#
# # maiin process
# def ethiopian(first, second):
#     result = 0
#     # 첫번째 수가 0이 될 때까지 반복
#     while first >= 1:
#         # 짝수일때
#         if even(first):
#             print("%4d %7d struck" % (first, second))
#         # 홀수일때
#         else:
#             print("%4d %7d keep" % (first, second))
#             result += second
#
#         first = half(first)
#         second = double(second)
#
#     print("The result is %d" % result)
#
# ethiopian(int(numset[0]), int(numset[1]))
