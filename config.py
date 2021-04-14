import os
import configparser as cp

configFile = "config.ini"
GameGroup = "TowersOfHanoi"
DiskKey = "disks"
PegsKey = "pegs"


class Config:
    def __init__(self):
        self.cp = cp.ConfigParser()
        self.check_config()

    def check_config(self):
        if os.path.isfile(configFile):
            self.cp.read(configFile)
            return
        print('No config.ini file. Creating a default one.')
        self.create_config()

    def create_config(self):
        self.cp[GameGroup] = {}
        self.cp[GameGroup][DiskKey] = "4"
        self.cp[GameGroup][PegsKey] = "3"

        with open(configFile, "w") as file:
            self.cp.write(file)

    @property
    def num_disks(self):
        return self.cp[GameGroup][DiskKey]

    @property
    def num_pegs(self):
        return self.cp[GameGroup][PegsKey]