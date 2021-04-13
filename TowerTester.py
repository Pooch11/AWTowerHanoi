from TowerGame import Disk, Peg, TowerGame
testGame = TowerGame()

def testInitGame():
    #try invalid input
    #assert game created as rules default
    pass

def testMoveDisktoPeg():
    #try invalid move
    #try invalid input
    #try same peg move
    #try invalid syntax
    #assert valid move does move
    pass
#Test Default Game to have wincon
def testWinCon(testGame):
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
    assert testGame.WINCONDITION == True


testWinCon(testGame)