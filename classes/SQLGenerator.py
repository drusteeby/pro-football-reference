class SQLGenerator(object):

    def generateSQL(self, gameData):       
        """ update/insert rows into objects table (update if the row already exists)
            given the key-value pairs in kwargs """
        keys = list()
        values = list()

        for key in gameData.statsDict:
            keys.append(str(key))
            values.append(str(gameData.statsDict[key]))

        sql = list()
        sql.append("INSERT OR IGNORE INTO Stats (")
        sql.append(", ".join(keys))
        sql.append(") VALUES (")
        sql.append(", ".join(values))       
        sql.append(");")
        return "".join(sql)