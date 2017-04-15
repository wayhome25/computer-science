import pickle
import math
from functools import reduce

def average(scores):
    return reduce(lambda a, b: a + b, scores)/len(scores)

def variance(scores, avrg):
    return reduce(lambda a, b: a + b, map(lambda s:(s-avrg)**2, scores))/len(scores)

def evaluateClass(avrg, std_dev):
    if avrg <50 and std_dev >20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > 50 and std_dev >20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < 50 and std_dev <20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > 50 and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

f = open("class_A.bin", "rb")

items = []

while 1:
    try: 
        data = pickle.load(f)
    except EOFError:
        break    
    items.append(data)

print(items)

scores = []

# normal way
'''
for item in items:
    for value in item.values():
        scores.append(value)
'''

#pythonic way??
scores = list(map(lambda x: x[0] , map(lambda item:list(item.values()),items)))

print(scores)

avrg = average(scores)
variance = round(variance(scores, avrg), 1)
standard_deviation = round(math.sqrt(variance), 1)

print("\n")

print('*' * 50)
print("A반 성적 분석 결과")
print('*' * 50)
print("A반의 평균은 {0}점이고 분산은 {1}이며, 따라서 표준편차는 {2}이다".format(avrg, variance, standard_deviation))
print('*' * 50)
print("A반 종합 평가")
print('*' * 50)

print('\n')
evaluateClass(avrg, standard_deviation)

f.close()
