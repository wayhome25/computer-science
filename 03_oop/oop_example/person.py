# 공통 속성을 뽑아서 부모 클래스
class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money 
        
    def give_money(self, other, how_much):
        if self.money > how_much:
            self.money -= how_much
            other.money += how_much
        else: 
            print('돈이 없어서 못줘')
        
    def __str__(self):
        return '''
My name is {}
I am {} years old
I have {} won'''.format(self.name, self.age, self.money)

    
    
if __name__=='__main__': # 너가 메인 실행 파일이라면 아래 명령을 실행한다. 
    p1 = Person('greg', 18, 5000)
    p2 = Person('kim', 22, 1000)
    print(p1)
    print(p2)
    p1.give_money(p2, 500)
    print(p1)
    print(p2)