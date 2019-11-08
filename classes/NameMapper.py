class NameMapper(object):
    """Maps HTML attribute names into a more descriptive name"""
    def __init__(self):
        self.nameMapDictionary = {}

    #Adds a new mapping to the dictionary
    def addNewMapping(self, oldName, newName):
        self.nameMapDictionary[oldName] = newName

    #Returns the mapped name for a given old name
    def getMappedName(self, oldName):
        if oldName in self.nameMapDictionary:
            return self.nameMapDictionary[oldName]
        return oldName


