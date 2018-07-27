import random as rd
import Player.const as const

class profession():
    def __init__(self, name='Beginner', hp=const.Beginner_hp, attack=const.Beginner_attack, sp_mag=const.Beginner_sp_mag ):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.sp_mag = sp_mag
        self.deck = list(const.init_deck)
        self.gar = []
        rd.shuffle(self.deck)
        self.hand = []
        for i in range(2):
            self.hand.append(self.deck[-1])
            self.deck.pop()
        ####every round#####
        self.damage = 0
        self.evade = False
        self.dodge_limit = const.Dodge_limit
        self.sp_limit = const.Sp_limit
        self.recovery = 0
        self.Max_hp = hp
    def initialize(self):
        self.damage = 0
        self.evade = False
        
        if self.hp < self.Max_hp:
            self.hp = min(self.hp + self.recovery, self.Max_hp)

    def draw(self):
        if len(self.deck)==0 :
            print('shuffle')
            while len(self.gar) > 0:
                self.deck.append(self.gar[-1])
                self.gar.pop()
                rd.shuffle(self.deck)
        self.hand.append(self.deck[-1])
        self.deck.pop()
        print('my card:',end=' ')
        print(self.hand)
    
    def choice(self):
        op = input('chooce your card:')
        while op not in self.hand :
            op=input('you don\'t have that card!\nchooce your card:')
        self.hand.remove(op)
        self.gar.append(op)
        
        if op == 'a':
            self.normal_attack()
        if op == 's':
            self.special()
        if op == 'd':
            self.dodge()

    def normal_attack(self):
        self.damage = self.attack

    def special(self):
        one = rd.randint(1,6)
        two = rd.randint(1,6)
        print('your dice number is:',one,two)
        sum = one+two
        if sum >= self.sp_limit:
            self.damage = self.attack * self.sp_mag
            print('attack successfully')
        else:
            self.damage = 0
            print('QQ')

    def dodge(self):
        one = rd.randint(1,6)
        two = rd.randint(1,6)
        print('your dice number is:',one,two)
        sum = one+two
        if sum <= self.dodge_limit:
            self.evade = True
            print('dodge successfully')
        else :
            self.evade = False
            print('QQ')


#### Beginner
class Beginner(profession):
    def __init__(self):
        super().__init__()
#################################################################
#### Fighter
class Fighter(profession):
    def __init__(self):
        super().__init__('Fighter', const.Fighter_hp, const.Fighter_attack, const.Fighter_sp_mag)

#### Magician
class Magician(profession):
    def __init__(self):
        super().__init__('Magician', const.Magician_hp, const.Magician_attack, const.Magician_sp_mag)
        self.sp_limit = const.Magician_sp_limit

#### Priest
class Priest(profession):
    def __init__(self):
        super().__init__('Priest', const.Priest_hp, const.Priest_attack, const.Priest_sp_mag)
        self.sp_limit = const.Priest_sp_limit
        self.recovery = const.Priest_recovery

#### Archer
class Archer(profession):
    def __init__(self):
        super().__init__('Archer', const.Archer_hp, const.Archer_attack, const.Archer_sp_mag)
        self.dodge_limit = const.Archer_dodge_limit

#### Assassin
class Assassin(profession):
    def __init__(self):
        super().__init__('Assassin', const.Assassin_hp, const.Assassin_attack, const.Assassin_sp_mag)
 
#### Pirate
class Pirate(profession):
    def __init__(self):
        super().__init__('Pirate', const.Pirate_hp, const.Pirate_attack, const.Pirate_sp_mag)



