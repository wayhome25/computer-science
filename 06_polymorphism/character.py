# abstract_class : 객체를 만들 수 없는 클래스 (기본클래스, 부모클래스의 역할)

from abc import * #abstract base class 

class Character(metaclass = ABCMeta): 
    def __init__(self):
        self.hp = 100
        self.attack_power = 20
    
    def attack(self, other, attack_kind):
        other.get_damage(self.attack_power, attack_kind)
        
    
    # 나를 상속받는 모든 클래스는 get_damage라는 함수를 오버라이딩으로 구현해야 너는 인스턴스를 만들 수 있다. 
    @abstractmethod 
    def get_damage(self, attack_power, attack_kind):
        pass
    
if __name__ == '__main__':
    ch1 = Character()