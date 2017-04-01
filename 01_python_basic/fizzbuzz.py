# Fizzbuzz

try:
	num = int(input("type a number! : "))
except ValueError:
	print("숫자를 입력하세요")

for i in range(1, num+1):
	if i == 15:
		print("Fizzbuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("buzz")
	else:
		print(i)
