import NameMapper

class SingleGameData(object):       

    # Initializer / Instance Attributes
    def __init__(self):
        self.statsDict = {}
        self.NameMapper = NameMapper.NameMapper()
        self.NameMapper.addNewMapping("test1","test5")
        # Instance method
    def addStat(self, name, value):
        mappedName = self.NameMapper.getMappedName(name)
        self.statsDict[mappedName] = value
    