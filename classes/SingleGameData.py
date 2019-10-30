class SingleGameData:       

    # Initializer / Instance Attributes
    def __init__(self):
        self.statsDict = {}

        # Instance method
    def addStat(self, name, value):
        self.statsDict[name] = value