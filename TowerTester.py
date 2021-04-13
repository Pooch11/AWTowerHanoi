from TowerGame import Disk, Peg, TowerGame



#Test Default Game to have wincon
def testWinCon(testGame):
    testGame
    testGame.moveDisktoPeg( 1, 2)
    testGame.moveDisktoPeg( 1, 3)
    testGame.moveDisktoPeg( 2, 3)
    testGame.moveDisktoPeg( 1, 2)
    testGame.moveDisktoPeg( 3, 1)
    testGame.moveDisktoPeg( 3, 2)
    testGame.moveDisktoPeg( 1, 2)
    testGame.moveDisktoPeg( 1, 3)
    testGame.moveDisktoPeg( 2, 1)
    testGame.moveDisktoPeg( 2, 3)
    testGame.moveDisktoPeg( 1, 3)
    testGame.moveDisktoPeg( 2, 1)
    testGame.moveDisktoPeg( 3, 2)
    testGame.moveDisktoPeg( 3, 1)
    testGame.moveDisktoPeg( 2, 3)
    testGame.moveDisktoPeg( 1, 2)
    testGame.moveDisktoPeg( 3, 2)
    testGame.moveDisktoPeg( 1, 3)
    testGame.moveDisktoPeg( 2, 1)
    testGame.moveDisktoPeg( 2, 3)
    testGame.moveDisktoPeg( 1, 3)
    assert testGame.WINCONDITION == True

testGame = TowerGame()
WINCONDITION = False
testWinCon(testGame)