from person import Person

# Retailer 클래스
class Retailer(Person):
    price = 1000 # 클래스 멤버 : 인스턴스가 모두 공유하는 데이터 
    
    def __init__(self, name, age, money, product): # 초기화 함수 
        super().__init__(name, age, money)
        self.product = product 
        
    def sell(self, other, how_many):
        total = self.price * how_many
        
        self.product -= how_many
        other.product += how_many
        
        other.give_money(self, total)
        
    def __str__(self):
        return super().__str__() + '''
I am a retailer
I have {} products'''.format(self.product)
        

if __name__ == '__main__' : # 테스트코드
    from buyer import Buyer 
    
    r1 = Retailer('yang', 20, 5000, 20)
    b1 = Buyer('kim', 13, 10000, 0)
    print(r1)
    print(b1)
    r1.sell(b1, 3)
    print(r1)
    print(b1)