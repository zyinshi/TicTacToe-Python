from unittest import TestCase, main
from game import Game

class TestBoard(TestCase):
	def setUp(self):
		self.game = Game()

	def test_isFull(self):
		self.assertFalse(self.game.board.isFull())
		self.game.board.board = [[1,0,1],[2,2,1],[1,1,1]]
		self.assertFalse(self.game.board.isFull())
		self.game.board.board = [[1,1,1],[2,2,1],[1,1,1]]
		self.assertTrue(self.game.board.isFull())

	def test_getWinner(self):
		self.game.board.board = [[1,1,1],[0,0,0],[0,0,0]]
		self.assertEqual(1, self.game.getWinner())
		self.game.board.board = [[1,0,0],[0,1,0],[0,0,1]]
		self.assertEqual(1, self.game.getWinner())
		self.game.board.board = [[1,2,1],[2,0,2],[0,2,0]]
		self.assertEqual(0, self.game.getWinner())
		self.game.board.board = [[1,2,1],[1,2,0],[1,0,0]]
		self.assertEqual(1, self.game.getWinner())
		self.game.board.board = [[2,2,2],[1,1,0],[1,0,0]]
		self.assertEqual(2, self.game.getWinner())

	def test_gameOver(self):
		self.game.board.board = [[1,0,1],[0,0,0],[0,0,0]]
		self.assertFalse(self.game.gameOver())
		self.game.board.board = [[1,1,1],[0,0,0],[0,0,0]]
		self.assertTrue(self.game.gameOver())
		self.game.board.board = [[1,1,1],[2,2,1],[1,1,1]]
		self.assertTrue(self.game.gameOver())


	def test_isValidPos(self):
		self.assertTrue(self.game.board.isValidPos(0, 0))
		self.assertTrue(self.game.board.mark(0, 0, 1))
		self.assertFalse(self.game.board.isValidPos(0, 0))

	def test_nextPlayer(self):
		self.game.firstTurn()
		self.assertEqual(2, self.game.nextPlayer())
		self.assertEqual(1, self.game.nextPlayer())

	def test_computerMove(self):
		self.game.board.board = [[1,0,1],[2,2,0],[0,0,0]]
		self.assertFalse(self.game.evaluateNext(2,0,1))
		self.assertTrue(self.game.evaluateNext(0,1,1))
		self.assertEqual([1, 2], self.game.computerMove())
		self.assertEqual(2, self.game.nextPlayer())		
		self.game.board.board = [[1,1,2],[0,2,0],[0,0,1]]
		self.assertEqual([2, 0], self.game.computerMove())
		self.game.board.board = [[1,1,0],[0,2,0],[0,0,0]]
		self.assertEqual([0, 2], self.game.computerMove())

if __name__ == '__main__':
    main()



