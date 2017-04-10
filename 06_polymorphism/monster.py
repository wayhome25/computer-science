from character import Character


class IceMonster(Character):
    def get_damage(self, attack_power, attack_kind):
        if attack_kind == 'ICE':
            self.hp += attack_power
        else:
            self.hp -= attack_power

    def __str__(self):
        return "Ice Monster's HP : {}".format(self.hp)
    
class FireMonster(Character):
    def get_damage(self, attack_power, attack_kind):
        if attack_kind == 'FIRE':
            self.hp += attack_power
        else:
            self.hp -= attack_power
            
    def __str__(self):
        return "Fire Monster's HP : {}".format(self.hp)
    