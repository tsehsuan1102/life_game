import sys

import Model.main as model
import View.main as view

def main(argv):
	gamemodel = model.GameEngine(argv[1:3])
	#graphics = view.Viewer(gamemodel)
	
	#####start game
	gamemodel.run()
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))





