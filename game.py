from board import Board 
from copy import deepcopy

class Game(object):
	def __init__(self):
		self.board = Board()
		self.__turn = self.firstTurn() 

	def firstTurn(self):
		return 1 	#human

	def print_board(self):
		for x in range(self.board.max_width):
			print " --- --- ---"
			print "| %s | %s | %s |" % \
            (self.showMark(self.board.board[x][0]), self.showMark(self.board.board[x][1]), self.showMark(self.board.board[x][2]))
		print " --- --- ---"

	def showMark(self,m):
		if m == 1:
			return 'O'
		elif m == 2:
			return 'X'
		else:
			return ' '

	def play(self):
		while not self.gameOver():
			self.print_board()
			self.update()
			

	def update(self):
		move = self.getMove(self.__turn)
		x = move[0]
		y = move[1]
		self.board.mark(x, y, self.__turn)
		self.__turn = self.nextPlayer()


	def nextPlayer(self):
		if self.__turn == 1:
			self.__turn = 2
		elif self.__turn == 2:
			self.__turn = 1
		return self.__turn

	def gameOver(self):
		if self.getWinner()==0 and self.board.isFull()==False:
			return False
		elif self.getWinner() == 1:
			print "You win!"
		elif self.getWinner() == 2:
			print "Sorry, you lose..."
		else:
			print "Tie"
		self.print_board()
		return True


	def getWinner(self):
		for i in range(self.board.max_width):
			if self.board.fullRow(i) != 0:
				return self.board.fullRow(i)
			if self.board.fullCol(i) != 0:
				return self.board.fullCol(i)
		if self.board.fullDiag() != 0:
			return self.board.fullDiag()
		return 0

	def getMove(self, player):
		if player == 1:
			return self.humanMove()
		elif player == 2:
			return self.computerMove()

	def humanMove(self):
		move = []
		x = int(raw_input("Now is your turn. Enter X coord (0-2): "))
		y = int(raw_input("                  Enter Y coord (0-2): "))

		while not self.board.isValidPos(x, y):
			print "try again:"
			x = int(raw_input("Enter X coord (0-2): "))
			y = int(raw_input("Enter Y coord (0-2): "))
		move.append(x)
		move.append(y)
		return move

	def computerMove(self):
		print "computer's move"
		possible_move = self.board.availablePos()
		for m in possible_move:
			if self.evaluateNext(m[0], m[1], player=2)==1:
				move = m
				return m
		for m in possible_move:
			if self.evaluateNext(m[0], m[1], player=1)==1:
				move = m
				return m
		return possible_move[0]

	def evaluateNext(self, x, y, player):
		currentBoard = self.copyBoard(self.board)
		self.board.mark(x, y, player)
		if self.getWinner() == player:
			ret = 1
		else:
			ret = 0
		self.board = self.copyBoard(currentBoard)
		return ret

	def copyBoard(self, inputBoard):
		newBoard = deepcopy(inputBoard)
		return newBoard








