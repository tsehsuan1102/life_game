import random as rd
import Player.profession as pro



print('##########################################')
print('# a->attack  s->special_attack  d->dodge #')
print('##########################################')

player1 = pro.Magician()
player2 = pro.Priest()

print('Player1 is:',player1.name)
print('Player2 is:',player2.name)


while player1.hp>0 and player2.hp>0 :  
    print('Player1 hp:',player1.hp)
    print('Player2 hp:',player2.hp)
    
    player1.initialize()
    player2.initialize()

    ####round_player1
    print('\n# Now is Player1\'s Round : ')
    player1.draw()
    player1.choice()       


    ####round_player2
    print('\n# Now is Player2\'s Round : ')
    player2.draw()
    player2.choice()
    
    if player1.evade == False:
        player1.hp -= player2.damage

    if player2.evade == False:
        player2.hp -= player1.damage


if player1.hp>0:
    print('--Player1 Win!')
elif player2.hp>0:
    print('--Player2 Win!')
else:
    print('--drew--')



