import sys, json
#initialize the game with a certain amount of disks from config (and certain amount of pegs)
#Config settings (TODO)
_disk_num = 4
_peg_num = 3



class Disk:
    """
        This class defines the Disk game objects
        Each have a particular size associated with them
    """
    def __init__(self, size):
        self.size = size #has a certain size
    def check_size(self):
        return self.size
    def _dump(self):
        return { "Disk" : { 'size' : self.size}}
class Peg:
    """
        This class defines a Peg game object
        Each Peg has a collection of disks that it keeps. Disks can only be removed through the contents stack.
    """
    def __init__(self, position):
        self.contents = []  #the disks that this peg is currently holding (check for max disks?)
        self.position = position
    def _initContents(self, diskContents :[Disk]):
        if self.position == 1:
            for disk in diskContents:
                self.addDisk(disk)
            print("Disks initialized on Peg#{0}".format(self.position))
    def _peek(self):
        if (len(self.contents) > 0):
            return self.contents[0]
    def _dump(self):
        return { "Peg" : {  'Disks' : self.jsonify_contents(),
                            'Position' : self.position }}
    def jsonify_contents(self):
        disks = {}
        for i, disk in enumerate(self.contents):
           disks.update({ i : disk._dump() })
        return disks
    def checkContents(self):
        for i, disk in enumerate(self.contents):
            print("Disk# {0} - Size: {1}  Peg# {2}".format(("(Top Disk)" if i == 0 else i), disk.check_size(), self.position))
    def isEmpty(self):
        return self.contents == []
    def peekTopSize(self):
        if (len(self.contents) > 0):
            if self.contents[0] is not None:
                return self.contents[0].check_size()
            else:
                return 0
    def addDisk(self, disk :Disk):
        self.contents.insert(0, disk)
        #check contents size (more than 1) else add to list (TODO)
        #check size of disk else cannot add this disk to this peg
    def removeDisk(self):
        return self.contents.pop(0)
    def _checkPostion(self):
        if self.position == 1:
            print("This is the Starter peg")
        elif self.position == _peg_num:
            print("This is the Goal peg")
        else:
            print("This is the working peg")



class TowerGame:
    """
        This class holds an instance of a Tower of Hanoi game
    """
    def __init__(self, disks=4, pegs=3):
        self.WINCONDITION = False   
        self.GameDisks = [] 
        self.GamePegs = []
        self.initGame(disks, pegs)
        #Global Game objects and fields
    def initGame(self, disks, pegs):
        for i in range(disks):
            self.GameDisks.append(Disk(i))
        self.GameDisks.reverse()    
        for i in range(1, pegs + 1):
            print("Peg #{0} created".format(i))
            self.GamePegs.append(Peg(i))
        self.GamePegs[0]._initContents(self.GameDisks)
        
    #Reports the content of Disks to the user
    def _inspectPeg(self, pegNumber : Peg):
        """
            Invokes a print out of the contents (Disks) on a Peg to the caller
        """
        return pegNumber.checkContents()
    def reportGameState(self):
        for i in self.GamePegs:
            print("Peg {0}".format(i.position))
            print("{0}".format(self._inspectPeg(i)))
            print("\n")
    def jsonifyGameState(self):
        state = ""
        for peg in self.GamePegs:
            state += json.dumps(peg._dump())
        return state

    def getPeg(self, pegIndexNumber):
        """
            Translates a Peg number to a Game Peg indexed in the Tower Game
            Returns a Peg Obj
        """
        return self.GamePegs[pegIndexNumber - 1]
    def moveDisktoPeg(self, pegFrom :Peg, pegTo :Peg):
        """
            Method describes the movement of a disk from the source peg to the destination peg
            Handles all the necessary logic to accept or deny movements
            :param pegFrom: (Peg Obj) The source Peg we are taking a disk from
            :param pegTo: (Peg Obj) The destination Peg we are placing a disk to 
        """
        if (pegFrom.isEmpty()):
            print("No disks to move")
            return
        if (len(pegTo.contents) != 0 and len(pegFrom.contents) != 0):
            if (pegTo.peekTopSize() < pegFrom.peekTopSize()):
                print("Cannot make this move, Destination Peg has a smaller disk size.")
            else:
                disk_to_add = pegFrom.peekTopSize()
                pegTo.addDisk(Disk(disk_to_add))
                pegFrom.removeDisk()
                print("Moved disk from Peg #{0} to Peg#{1}".format(pegFrom.position, pegTo.position))
        else:
            disk_to_add = pegFrom.peekTopSize()
            pegTo.addDisk(Disk(disk_to_add))
            pegFrom.removeDisk()
            print("Moved disk from Peg #{0} to Peg#{1}".format(pegFrom.position, pegTo.position))
        #Add check win condition here
        if (len(pegTo.contents) == _disk_num):
            self.check_win()

    def check_win(self):
        """
            Checks if the win condition of the game has been met
        """
        if (len(self.GamePegs[_peg_num -1].contents) == _disk_num):
            nextBiggest = 0 
            for i, disk in enumerate(self.GamePegs[_peg_num -1].contents):   
                if (disk.size <= nextBiggest):
                    nextBiggest = disk.size
                    self.WINCONDITION = True
            if (self.WINCONDITION == True):
                print("All disks in correct order")
                print("Congratulations You Win!")       
        else:
            print("Disks have been stacked on the incorrect Goal Peg (#{0})".format(_peg_num))

##Invoke Game to Interact with
if (len(sys.argv) > 1):
    temp = TowerGame(_disk_num, _peg_num)
    print("Welcome to Towers of Hanoi - There are {0} disks and {1} pegs in this version".format(_disk_num, _peg_num))
    print("Move disks on pegs to by typing out the source peg # and destionation peg # when prompted")
    while(not temp.WINCONDITION):
        temp.reportGameState()
        txt = input("Source Peg# / Destination Peg#: ") 
        source, dest = map(int, txt.split())
        print ("Attempting to move a disk from {0} to {1}".format(source, dest))
        if ((1 <= source and 1 <= dest) and (_peg_num >= source and _peg_num >= dest)):
            temp.moveDisktoPeg( temp.GamePegs[source - 1], temp.GamePegs[dest - 1])
        else:
            print("Cannot execute move - Peg # not in range. There are a maximum of {0} pegs".format(_peg_num))



