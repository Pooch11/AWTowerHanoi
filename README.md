# Contents
## 1. [Goal](https://github.com/Pooch11/AWTowerHanoi#Goal)
## 2. [Technical Requirements](https://github.com/Pooch11/AWTowerHanoi#Technical-Requirements)
## 3. [Development environment Requirements](https://github.com/Pooch11/AWTowerHanoi#Development-environment)
## 4. [API Method Reference](https://github.com/Pooch11/AWTowerHanoi#API-Methods)

## Goal

You must implement a "Tower of Hanoi" game engine. Your implementation must expose a RESTful API which a client (implementation not in scope) can use to modify the state of a game.

        Requirements:
		
        - The game engine has these responsibilities:
		
         - Enforce the rules of the game (as stated in the article above) and report an error if any attempted move violates the rules
		 
         - Apply the effects of any valid move to the game state
		 
         - Provide the client with the complete state of the rods and disks
		 
         - Determine if the victory conditions have been met
		 
        - The game engine must support 4 disks
		
 
Any requirements not stated above should be decided upon by you, and documented along with your code.

That said, we are happy to consider solutions in other languages and frameworks.Don’t forget about test coverage.Feel free to use third-party widgets and layout frameworks, build tools or whatever you would normally use

------------------------------------------------------------------------------------------------

## Technical Requirements:
Python 3 and PIP, see requirements.txt to see full list of packages to include

*TowerGame.py* - Contains all the game puzzle logic

*TowerAPI.py* - An API endpoint to invoke moves/options within the game

*testTowerGame.py* - An automated tester to check the validity of each game function

*testTowerAPI.py* - An automated tester that calls game functions through the API to validate the return data

*config.py* - (deprecated) Initialy made to load in different settings for the game but is less userful at this time.

Different game setting could be implemented using the config file but for ease of use the game configuration is determined by variables:

_disk_num 

_peg_num

--------------------------------------------------------------------------------------------------------------------

## Development environment: 

Ensure you have python installed and proper path environment variables are set

__pip install -r "requirements.txt"__

This will install Flask and requests onto your environment which is a necessary module for the web API version of this game

When run, the file TowerAPI.py will create an endpoint that interacts with one instance of the game located at __127.0.0.1:5000/__

See endpoint documentation API Methods for end-user functions

The Towers of Hanoi game can be interactable in 2 main ways.

Running _'python TowerAPI.py'_ and then navigating to the browser(127.0.0.1:5000/)

or

Running 'python TowerGame.py -d' as the main entry point into a CMD version of the game in a debug mode

### Tester Files 

- testTowerGame.py uses python's unittest module to assert the return of expected behaviour

- testTowerAPI.py asserts the return value of the API calls and ensures the endpoint is reachable 

-------------------------------------------------------------------------------------------------------------------------------------------------------------
## API Methods
### /

Description:
The home page of the web application, starts a new game when called unless one is already in progress
Otherwise, reports the game state information in JSON format

Parameters:
(Optional) - 'new'
	- restarts to a new game

### /newgame
Description:
Forcibly starts a new game

Parameters:
 - None

### /movepeg
Description:
Executes a user's game move by attempting to move a disk from the source peg to the destination peg

Parameters:

Parameter 1 (int) - from
	- The source peg
	
Parameter 2 (int) - to
	- The destination peg
	
Example Usage:

	http://127.0.0.1:5000/movepeg?from=1&to=3


### /gamewin
Description:
Checks the state of the game by reporting if the game is complete or not

Parameters:

- None

Returns Code 400 if Game is not complete, 200 if game is won


### /gamestatus
Description:
Reports the status of the game by reporting the contents of each peg in the game instance in JSON format if the game is still in progress

Parameters:
- None

### /pegstatus
Description:
Reports the status of a single peg and returns a JSON string representation of the Peg

Parameters:

Parameter 1 (int) - peg

Example Usage:

	http://127.0.0.1:5000/pegstatus?peg=1
