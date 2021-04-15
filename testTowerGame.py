import unittest
from TowerGame import Disk, Peg, TowerGame
import requests

class TowersTestCase(unittest.TestCase):
    #Test InitGame
    def test_InitGame(self):
        testGame = TowerGame()
        self.assertEqual(isinstance(testGame, TowerGame), True)

    #Test getPeg returns Peg Obj
    def test_getPeg(self):
        self.testGame = TowerGame()
        the_Peg = self.testGame.getPeg(1)
        self.assertEqual(isinstance(the_Peg, Peg), True)
    
    #try getting Peg not in game range
    def test_invalid_getPeg(self):
        self.testGame = TowerGame()
        invalidPeg = self.testGame.getPeg(6)
        self.assertEqual(invalidPeg, None)
    
    #try invalid input to getPeg
    def test_badInput_getPeg(self):
        self.testGame = TowerGame()     
        invalidPeg = self.testGame.getPeg('a')
        self.assertEqual(invalidPeg, None)

    #Test _inspectPeg - Inspect peg 1 and 2 after game creation should return a string representation of dict
    def test_inspectPeg(self):
        testGame = TowerGame()
        testContents = testGame.getPeg(1)._dump()
        contents_1 = {'Peg': {'Disks': {0: {'Disk': {'size': 0}}, 1: {'Disk': {'size': 1}}, 2: {'Disk': {'size': 2}}, 3: {'Disk': {'size': 3}}}, 'Position': 1}}
        self.assertEqual(testContents, contents_1)
        contents_2 = {'Peg': {'Disks': {}, 'Position': 2}}
        testContents = testGame.getPeg(2)._dump()
        self.assertEqual(testContents, contents_2)

    #Try moving Disk (default)
    def test_MoveDisktoPeg(self):
        self.testGame = TowerGame()
        validMove = False
        validMove = self.testGame.moveDisktoPeg(self.testGame.getPeg(1), self.testGame.getPeg(2))
        self.assertEqual(validMove, True)

    #Try moving larger disk on smaller stack
    def test_Larger_MoveDisktoPeg(self):
        self.testGame = TowerGame()
        validMove = self.testGame.moveDisktoPeg(self.testGame.getPeg(1), self.testGame.getPeg(2))
        if (validMove):
            validMove = self.testGame.moveDisktoPeg(self.testGame.getPeg(1), self.testGame.getPeg(2))
        self.assertEqual(validMove, False)
    
    #Try moving no disk to peg
    def test_None_MoveDisktoPeg(self):
        self.testGame = TowerGame()
        validMove = self.testGame.moveDisktoPeg(self.testGame.getPeg(3), self.testGame.getPeg(1))
        self.assertEqual(validMove, False)
    
    #Try moving same disk to peg
    def test_Same_MoveDisktoPeg(self):
        self.testGame = TowerGame()
        validMove = self.testGame.moveDisktoPeg(self.testGame.getPeg(1), self.testGame.getPeg(1))
        self.assertEqual(validMove, True)

    #Try moving same disk to non-existant peg
    def test_Invalid_MoveDisktoPeg(self):
        self.testGame = TowerGame()
        validMove = self.testGame.moveDisktoPeg(self.testGame.getPeg(1), self.testGame.getPeg(4))
        self.assertEqual(validMove, False)
        validMove = self.testGame.moveDisktoPeg(self.testGame.getPeg(6), self.testGame.getPeg(7))
        self.assertEqual(validMove, False)
    
    #Try checkingWinCondition
    def test_check_win(self):
        testGame = TowerGame()     
        self.assertEqual(testGame.check_win(), False)
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(2))
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(3))
        testGame.moveDisktoPeg( testGame.getPeg(2), testGame.getPeg(3))
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(2))
        testGame.moveDisktoPeg( testGame.getPeg(3), testGame.getPeg(1))
        testGame.moveDisktoPeg( testGame.getPeg(3), testGame.getPeg(2))
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(2))
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(3))
        testGame.moveDisktoPeg( testGame.getPeg(2), testGame.getPeg(1))
        testGame.moveDisktoPeg( testGame.getPeg(2), testGame.getPeg(3))
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(3))
        testGame.moveDisktoPeg( testGame.getPeg(2), testGame.getPeg(1))
        testGame.moveDisktoPeg( testGame.getPeg(3), testGame.getPeg(2))
        testGame.moveDisktoPeg( testGame.getPeg(3), testGame.getPeg(1))
        testGame.moveDisktoPeg( testGame.getPeg(2), testGame.getPeg(3))
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(2))
        testGame.moveDisktoPeg( testGame.getPeg(3), testGame.getPeg(2))
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(3))
        testGame.moveDisktoPeg( testGame.getPeg(2), testGame.getPeg(1))
        testGame.moveDisktoPeg( testGame.getPeg(2), testGame.getPeg(3))
        testGame.moveDisktoPeg( testGame.getPeg(1), testGame.getPeg(3))
        self.assertEqual(testGame.check_win(), True)


if __name__ == '__main__':
    unittest.main()