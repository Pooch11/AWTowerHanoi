import flask
import json
from flask import request, jsonify
from TowerGame import Disk, Peg, TowerGame

app = flask.Flask(__name__)
app.config["DEBUG"] = True
GLOBALGAME = {}

@app.route('/', methods=['GET'])
def start():
    global GLOBALGAME
    if (isinstance(GLOBALGAME, TowerGame)):
        if 'new' in request.args:
            GLOBALGAME = TowerGame()
            return "Started a new game!"
        return "Already a game in progress\n" + GLOBALGAME.jsonifyGameState()
    else:
        GLOBALGAME = TowerGame()
        return "Started a new game!"

@app.route('/newgame', methods=['GET'])
def newgame():
    global GLOBALGAME
    GLOBALGAME = TowerGame()
    return "Started a new game!"

@app.route('/movepeg', methods=['GET'])
def movePeg():
    if 'from' in request.args:
        fromID = int(request.args['from'])
    else:
        return "Error: 'From' Peg ID was not valid"
    if 'to' in request.args:
        toID = int(request.args['to'])
    else:
        return "Error: 'To' Peg ID was not valid"
    _from = GLOBALGAME.getPeg(fromID)
    _to = GLOBALGAME.getPeg(toID)
    if isinstance(_from , Peg) and isinstance(_to , Peg):
        valid_move = GLOBALGAME.moveDisktoPeg(_from, _to)
        if (valid_move ):
            return "Results <br/>  Peg {0}".format(fromID) + str(_from._dump()) + "<br/>" + "Peg {0}".format(toID) + str(_to._dump())
        else:
            return "Invalid Move <br/> " + GLOBALGAME.jsonifyGameState()
    else:
        return "Invalid input from Query Parameters"
@app.route('/gamewin', methods=['GET'])
def reportWin():
    if (GLOBALGAME.WINCONDITION is False):
        return "Game not completed", 400
    else:
        return "Game Complete!", 200

@app.route('/gamestatus', methods=['GET'])
def inspectGame():
    if (isinstance(GLOBALGAME, TowerGame)):
        if (GLOBALGAME.WINCONDITION is False):
            return GLOBALGAME.jsonifyGameState()
        else:
            GLOBALGAME.jsonifyGameState() + "The Game is Won! go to " + 'localhost:5000/?newgame=1'
    else:
        return "No Game has been started"

@app.route('/pegstatus', methods=['GET'])
def inspectPeg():
    if (isinstance(GLOBALGAME, TowerGame)):
        if (GLOBALGAME.WINCONDITION is False):
            if 'peg' in request.args:
                peg_num = int(request.args['peg'])
                return str(GLOBALGAME.getPeg(peg_num)._dump())

app.run()