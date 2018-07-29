import sys

import os
import Model.main as model
import View.main as view

def main(argv):
    
    #os.system('start "" python main.py')
    gamemodel = model.GameEngine()
    #graphics = view.Viewer(gamemodel)

    #####start game
    gamemodel.run()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))





