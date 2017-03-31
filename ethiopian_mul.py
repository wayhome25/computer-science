num = int(input("숫자 1을 입력하세요 : "))
num2 = int(input("숫자 2를 입력하세요 : "))

result = 0
while True :
    if num % 2 : # num이 홀수 일때
        result += num2
    num = num // 2
    num2 = num2 * 2
    if num == 0:
        print(result)
        break

# nums = list(input("숫자 2개를 입력하세요"))
# print(sum([i for i in nums]))
