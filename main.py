import sys

import Model.main as model

def main(argv):
	gamemodel = model.GameEngine(argv[1:3])
	
	gamemodel.run()
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
