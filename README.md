Goal:
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

Make your app available as a Github repository.  Please have your solution posted within 5 days of receiving the test.

Technical Requirements:
Python 3 and PIP, see requirements.txt to see full list of packages to include

TowerGame.py - Contains all the game puzzle logic

TowerAPI.py - An API endpoint to invoke moves/options within the game

TowerTester - An automated tester to check the validity of each game function

config.py - (deprecated) Initialy made to load in different settings for the game but is less userful at this time.


Development environment:

Ensure you have python installed and proper environmnet variables are set


pip install -r "requirements.txt"

This will install Flask onto your environmnet

To run the Towers of Hanoi API - open a cmd prompt window in the file directory and type - python TowerAPI.py

This will create an endpoint that interacts with one instance of the game located at 127.0.0.1:5000/

See Endpoint documentation for end-user functions

The Towers of Hanoi game can be interactable in 2 main ways.

Running 'python TowerAPI.py' and then navigating to the browser

or

Running 'python TowerGame.py' as the main entry point into a CMD version of the game

The Tester file - TowerTester.py validates both Functions at the Game level version but can also be called to test appropriate respponses from the API calls made.

