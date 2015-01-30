class Board(object):
	max_width = 3;
	max_height = 3;

	def __init__(self):
		self.board = []
		for x in range(self.max_width):
			self.board = [[0 for y in range(self.max_height)] for x in range(self.max_width)]

	def outBoundary(self, x, y):
		if x<0 or x>=self.max_width or y<0 or y>=self.max_height:
			print "out of boundary: choose from 0-", self.max_width-1
			return True
		return False

	def isValidPos(self, x, y):
		if self.outBoundary(x, y):
			return False
	 	if self.board[x][y] != 0:
	 		print "Occupied"
	 	else:
	 		return True


	# mark player at position(x,y)
	def mark(self, x, y, player):   	
	 	if player is None:
	 		print "invalid player!"
	 		return False;
	 	if self.isValidPos(x, y):
	 		self.board[x][y] = player
	 		return True

	def getMark(self, x, y):
		if not self.outBoundary:
			return board[x][y]


	def isFull(self):
		for x in range(self.max_width):
			for y in range(self.max_height):
				if self.board[x][y] == 0:
					return False
		return True

	def fullRow(self, row):
		p = self.board[row][0]
		ret = p
		if p == 0:
			return 0
		for i in range(self.max_width):
			if p != self.board[row][i]:
				ret = 0
		return ret

	def fullCol(self, col):
		p = self.board[0][col]
		ret = p
		if p == 0:
			return 0
		for i in range(self.max_height):
			if p != self.board[i][col]:
				ret = 0
		return ret

	def fullDiag(self):
		p = self.board[1][1]
		if p==self.board[0][0] and p==self.board[2][2]:
			return p
		elif p==self.board[2][0] and p==self.board[0][2]:
			return p
		else:
			return 0

	def availablePos(self):
		available_pos = []
		for x in range(self.max_width):
			for y in range(self.max_height):
				if self.board[x][y] == 0:
					available_pos.append([x, y])
		return available_pos





