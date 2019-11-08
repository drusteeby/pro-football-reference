import SingleGameData
import SQLGenerator

gameData = SingleGameData.SingleGameData()

gameData.addStat("test1", "1")
gameData.addStat("test2", "2")
gameData.addStat("test3", "3")
gameData.addStat("test4", "4")

generator = SQLGenerator.SQLGenerator()

sql = generator.generateSQL(gameData)

expected = '''INSERT OR IGNORE INTO Stats (test5, test2, test3, test4) VALUES (1, 2, 3, 4);'''

areequal = sql == expected

if(areequal):
    print("Success!")
else:
    print("Failure")
    print("Expected:")
    print(expected)
    print("Actual:")
    print(sql)