import random as rd
import Model.profession as pro
import View.main as view


class GameEngine(object):
    '''
    Tracks the game state.
    '''
    ####init at the start of the battle
    def __init__(self, player_names):
        self.running = False
        self.player_names = player_names
        self.player1 = None
        self.player2 = None
        print('##########################################')
        print('# a->attack  s->special_attack  d->dodge #')
        print('##########################################')
        self.init_player_list()

        #self.viewer = view.Viewer(self)
        #self.viewer.Update()

    #####initialize every round
    def initialize(self):
        self.player1.initialize()
        self.player2.initialize()      

    def init_player_list(self):
        #player1
        self.player1 = (self.ask(self.player_names[0]) )
        #player2
        self.player2 = (self.ask(self.player_names[1]) )

    def round(self):
        self.initialize()
        print('Player1 hp:',self.player1.hp)
        print('Player2 hp:',self.player2.hp)
        
        ####round_player1
        print('\n# Now is Player1\'s Round : ')
        self.player1.draw()
        self.player1.choice()


        ######Update Screen
        #self.viewer.Update()
        ######Update Screen

        
        ####round_player2
        print('\n# Now is Player2\'s Round : ')
        self.player2.draw()
        self.player2.choice()   

        ######Update Screen
        #self.viewer.Update()
        ######Update Screen
        
        
        ##cause damage
        if self.player1.evade == False:
            self.player1.hp -= self.player2.damage

        if self.player2.evade == False:
            self.player2.hp -= self.player1.damage

        ######Update Screen
        #self.viewer.Update()
        ######Update Screen

        ##Game Over
        if self.player1.hp<=0 or self.player2.hp<=0:
            self.running = False 

    def run(self):
        self.running = True
        while self.running == True:
            self.round()
        if self.player1.hp>0:
            print('--Player1 Win!')
        elif self.player2.hp>0:
            print('--Player2 Win!')
        else:
            print('--drew--')

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








