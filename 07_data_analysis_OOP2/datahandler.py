from evaluate import Evaluate
from functools import reduce
import pickle
import math

# 이런 류의 클래스에는 Handler, Manager, Controlloer 라는 말을 자주 사용한다. 
class DataHandler:
    evaluator = Evaluate() # 클래스 변수 : 클래스의 모든 인스턴스들이 공유하는 변수 (연산기)
                           # 객체합성 (선생님의 캡슐화 범위)
        
    
    # class method : 전역함수처럼 사용
    @classmethod # 인스턴스 메소드로 정의해도 문제는 없다
    def GetRawdataInDic(cls, filename):
        rawdata = {}
        with open(filename, 'rb') as f:
            while 1:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                rawdata.update(data)
                
        return rawdata
    
    def __init__(self, filename, clsname):
        self.rawdata = DataHandler.GetRawdataInDic(filename)
        self.clsname = clsname
        self.cache = {}         # 연산한 값을 저장해 두는 저장소 
                                #(필요할 때 연산하되 이미 연산된 값이면 연산 없이 저장된 값을 반환)
    
    def get_scores(self): # cache기법 사용
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())
        
        return self.cache.get('scores')
    
    def get_average(self): # cache 사용
        if 'average' not in self.cache:
            self.cache['average'] = self.evaluator.average(self.get_scores())

        return self.cache.get('average')
    
    def get_variance(self): # cache 사용
        if 'variance' not in self.cache:
            vari = round(self.evaluator.variance(self.get_scores(), self.get_average()), 1)
            self.cache['variance'] = vari
            
        return self.cache.get('variance')
    
    def get_standard_deviation(self):
        if 'standard_deviation' not in self.cache:
            std_dev = round(math.sqrt(self.get_variance()), 1) 
            self.cache['standard_deviation'] = std_dev
        
        return self.cache.get('standard_deviation')
    
    def GetEvaluation(self):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print("{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".\
              format(self.clsname, self.get_average(), self.get_variance()\
                     , self.get_standard_deviation()))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluateClass()

    def evaluateClass(self):
        avrg = self.get_average()
        std_dev = self.get_standard_deviation()
        
        if avrg <50 and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > 50 and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < 50 and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > 50 and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

    
#     def who_is_highest(self):
#         h_score= max(list(self.rawdata.values()))
#         for k, v in self.rawdata.items():
#             if v == h_score:
#                 return k
#     def get_highest_score(self):
#         return max(list(self.rawdata.values()))


# 선생님 코드
    def who_ist_highest(self):
        if 'highest' not in self.cache:
            self.cache['highest'] = reduce(lambda a, b: a if self.rawdata.get(a) > self.rawdata.get(b) else b, self.rawdata.keys())
        return self.cache.get('highest')
    
    def get_highest_score(self):
        return self.rawdata[self.who_ist_highest()]
    
    def who_is_lowest(self):
        if 'lowest' not in self.cache:
            self.cache['lowest'] = reduce(lambda a, b: a if self.rawdata.get(a) < self.rawdata.get(b) else b, self.rawdata.keys())
        return self.cache.get('lowest')
    
    def get_lowest_score(self):
        return self.rawdata[self.who_is_lowest()]