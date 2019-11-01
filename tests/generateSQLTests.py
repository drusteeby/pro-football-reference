from classes import SingleGameData

gameData = SingleGameData.SingleGameData()

gameData.addStat("test1", "1")
gameData.addStat("test2", "2")
gameData.addStat("test3", "3")
gameData.addStat("test4", "4")

sql = gameData.generateSQL()

expected = '''INSERT OR IGNORE INTO Stats (test1, test2, test3, test4) VALUES (1, 2, 3, 4);'''

areequal = sql == expected

if(areequal):
    print("Success!")
else:
    print("Failure")
    print("Expected:")
    print(expected)
    print("Actual:")
    print(sql)