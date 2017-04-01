# year = int(input("년도를 입력하세요 :"))
#
# def year_check(a):
#     if (a % 100) == 0:
#         return "평년"
#     elif (a % 4) == 0 or (a % 400) == 0:
#         return "윤년"
#
#
# year_check(year)

def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
         leap = True
    return leap

year = int(input("년도를 입력하세요 :"))
print(is_leap(year))
