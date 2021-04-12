import copy
#initialize the game with a certain amount of disks from config (and certain amount of pegs)
#Config settings (TODO)
_disk_num = 4
_peg_num = 3
WINCONDITION = False

#Global Game objects and fields
GameDisks = [] 
GamePegs = []
class Disk:
    def __init__(self, size):
        self.size = size #has a certain size
    def check_size(self):
        return self.size
class Peg:
    def __init__(self, position):
        self.contents = []  #the disks that this peg is currently holding (check for max disks?)
        self.position = position
    def _initContents(self, diskContents :[Disk]):
        if self.position == 1:
            for disk in diskContents:
                self.addDisk(disk)
            print("Disks initialized on Peg#{0}".format(self.position))
    def checkContents(self):
        for i, disk in enumerate(self.contents):
            print("Disk# {0} - Size: {1}  Peg# {2}".format(("(Top Disk)" if i == 0 else i), disk.check_size(), self.position))
    def isEmpty(self):
        return self.contents == []
    def _peek(self):
        if (len(self.contents) > 0):
            return self.contents[0]
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




#Initialize GameDisks on 1 peg in size order
def initGame(disks, pegs = 3):
    for i in range(disks):
        GameDisks.append(Disk(i))
    GameDisks.reverse()    
    for i in range(1, pegs + 1):
        print("Peg #{0} created".format(i))
        GamePegs.append(Peg(i))
    GamePegs[0]._initContents(GameDisks)
    
#Reports the content of Disks to the user
def inspectPeg(pegNumber : Peg):
    return pegNumber.checkContents()

# defines which pegs will be involved in a disk movement
        #Logic to determine if we can put this disk on this peg
        #remove disk from pegFrom
        #add disk to pegTo
def moveDisktoPeg(pegFrom :Peg, pegTo :Peg):
    if (len(pegFrom.contents) == 0):
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
    #Add check win condition here?
    if (len(pegTo.contents) == _disk_num):
        check_win()

def check_win():
    global WINCONDITION
    if (len(GamePegs[_peg_num -1].contents) == _disk_num):
        for i, disk in GamePegs[_peg_num -1].contents:
            if (disk.size == GameDisks[i].size):
                print("All disks in correct order")
        print("Congratulations You Win!")
        WINCONDITION = True
    else:
        print("Disks have been stacked on the incorrect Goal Peg (#{0})".format(_peg_num))

##Game to Interact with
initGame(_disk_num, _peg_num)
print("Welcome to Towers of Hanoi - There are {0} disks and {1} pegs in this version".format(_disk_num, _peg_num))
print("Move disks on pegs to by typing out the source peg # and destionation peg # when prompted")
while(not WINCONDITION):
    for i in GamePegs:
        print("Peg {0}".format(i.position))
        print("{0}".format(inspectPeg(i)))
        print("\n")
    txt = input("Source Peg# / Destination Peg#: ") 
    source, dest = map(int, txt.split())
    print ("Attempting to move a disk from {0} to {1}".format(source, dest))
    if ((1 <= source and 1 <= dest) and (_peg_num >= source and _peg_num >= dest)):
        moveDisktoPeg( GamePegs[source - 1], GamePegs[dest - 1])
    else:
        print("Cannot execute move - Peg # not in range. There are a maximum of {0} pegs".format(_peg_num))



