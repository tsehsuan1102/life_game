import random as rd
import Model.profession as pro
import View.main as view
import colorama
from colorama import Fore

class GameEngine(object):
    '''
    Tracks the game state.
    '''
    ####init at the start of the battle
    def __init__(self):
        self.running = False
        self.player_names = ["", ""]
        
        self.player1 = None
        self.player2 = None

        print("\033[3;31;47m\n")
        print('          ##########################################              ')
        print('          # a->attack  s->special_attack  d->dodge #              ')
        print('          ##########################################              ')
        print('          ##########################################              ')
        print('          #            Profession List             #              ')
        print('          #                Beginner                #              ')
        print('          #                Fighter                 #              ')
        print('          #                Magician                #              ')
        print('          #                Priest                  #              ')
        print('          #                Archer                  #              ')
        print('          #                Assassin                #              ')
        print('          #                Pirate                  #              ')
        print('          ##########################################              ')


        self.init_player_list()
        #self.viewer = view.Viewer(self)
        #self.viewer.Update()

    #####initialize every round
    def initialize(self):
        self.player1.initialize()
        self.player2.initialize()      

    def init_player_list(self):
        #player1
        print("\033[1;36;40m\n")
        while self.player1 is None:
            self.player_names[0] = input('Player1\'s profession: ')
            self.player1 = (self.ask(self.player_names[0]) )
        
        #player2
        print("\033[1;35;40m\n")
        while self.player2 is None:
            self.player_names[1] = input('Player2\'s profession: ')
            self.player2 = (self.ask(self.player_names[1]) )
         
    def round(self):
        self.initialize()

        print("\033[1;37;44m\n")
        print('######################## Player1(', self.player1.name , ')', ' hp:',self.player1.hp,'########################')
        print('######################## Player2(', self.player2.name , ')', ' hp:',self.player2.hp,'########################')
       
        ####round_player1
        print("\033[1;36;40m\n")
        print('\n# Now is Player1\'s Round : ')
        self.player1.draw()
        self.player1.choice()
  
        ####round_player2
        print("\033[1;35;40m\n")
        print('\n# Now is Player2\'s Round : ')
        self.player2.draw()
        self.player2.choice()   
       
        
        #### Archer skill ####
        if self.player1.name == 'Archer' and self.player1.evade == True and self.player2.damage > 0:
            self.player1.success_dodge = True

        if self.player2.name == 'Archer' and self.player2.evade == True and self.player1.damage > 0:
            self.player2.success_dodge = True

        ##cause damage
        if self.player1.evade == False:
            self.player1.hp -= self.player2.damage
            
        if self.player2.evade == False:
            self.player2.hp -= self.player1.damage

        ##Game Over
        if self.player1.hp<=0 or self.player2.hp<=0:
            self.running = False
            print("\033[1;30;47m\n")

    def run(self):
        self.running = True
        while self.running == True:
            self.round()
        if self.player1.hp>0:
            print('--------------------Player1 Win!---------------------------')
        elif self.player2.hp>0:
            print('--------------------Player2 Win!---------------------------')
        else:
            print('--------------------   Drew!!   ---------------------------')

    def ask(self, name):
        if name == 'Beginner':
            return pro.Beginner()
        elif name == 'Fighter':
            return pro.Fighter()
        elif name == 'Magician':
            return pro.Magician()
        elif name == 'Priest':
            return pro.Priest()
        elif name == 'Archer':
            return pro.Archer()
        elif name == 'Assassin':
            return pro.Assassin()
        elif name == 'Pirate':
            return pro.Pirate()
        else:
            return None








