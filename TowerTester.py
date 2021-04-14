from TowerGame import Disk, Peg, TowerGame
import requests
testGame = TowerGame()

def testInitGame():
    #try invalid input
    #assert game created as rules default
    pass
def testgetPeg():
    pass
def testinspectPeg():
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

def testMoveAPI(fromPeg, toPeg):
    r = requests.get('http://127.0.0.1:5000/movepeg?from={0}&to={1}'.format(fromPeg, toPeg))
    print(r.text)

def teststartAPI():
    r = requests.get('http://127.0.0.1:5000/')
    print(r.text)
def testnewgameAPI():
    r = requests.get('http://127.0.0.1:5000/?new=1')
    print(r.text)

def testWinConAPI():
    testMoveAPI(1,2)
    testMoveAPI(1,3)
    testMoveAPI(2,3)
    testMoveAPI(1,2)
    testMoveAPI(3,1)
    testMoveAPI(3,2)
    testMoveAPI(1,2)
    testMoveAPI(1,3)
    testMoveAPI(2,1)
    testMoveAPI(2,3)
    testMoveAPI(1,3)
    testMoveAPI(2,1)
    testMoveAPI(3,2)
    testMoveAPI(3,1)
    testMoveAPI(2,3)
    testMoveAPI(1,2)
    testMoveAPI(3,2)
    testMoveAPI(1,3)
    testMoveAPI(2,1)
    testMoveAPI(2,3)
    testMoveAPI(1,3)


testWinCon(testGame)
testnewgameAPI()
testWinConAPI()
testnewgameAPI()
teststartAPI()

