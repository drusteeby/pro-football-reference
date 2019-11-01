class SingleGameData:       

    # Initializer / Instance Attributes
    def __init__(self):
        self.statsDict = {}

        # Instance method
    def addStat(self, name, value):
        self.statsDict[name] = value

    def getStat(self, name):
        return self.statsDict[name]

    def generateSQL(self):
        """ update/insert rows into objects table (update if the row already exists)
            given the key-value pairs in kwargs """
        keys = list()
        values = list()

        for key in self.statsDict:
            keys.append(str(key))
            values.append(str(self.statsDict[key]))

        sql = list()
        sql.append("INSERT OR IGNORE INTO Stats (")
        sql.append(", ".join(keys))
        sql.append(") VALUES (")
        sql.append(", ".join(values))       
        sql.append(");")
        return "".join(sql)