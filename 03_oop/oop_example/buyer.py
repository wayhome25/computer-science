from person import Person

class Buyer(Person):
    def __init__(self, name, age, money, product):
        super().__init__(name, age, money)
        self.product = product
    
    def buy(self, other, how_many):
        total = other.price * how_many
        
        self.product += how_many
        other.product -= how_many
        
        self.give_money(other, total)
    
    def __str__(self):
        return super().__str__() + '''
I am a buyer
I have {} products'''.format(self.product)

if __name__ == '__main__' :  # 테스트코드
    from retailer import Retailer

    b1 = Buyer('siwa', 18, 10000, 0)
    r1 = Retailer('sun', 35, 2000, 20)
    print(b1)
    print(r1)
    b1.buy(r1, 3)
    print(b1)
    print(r1)    