from game import Game

print "=================================="
print "  Welcome! Tic Tac Toe"
print "=================================="
print
start = 'y'
while start=='y':
	newgame = Game()
	newgame.play()
	start = raw_input("Game ended. New game? [y/n]")



