# A Python program called game-stats-analyser.py that loads and explores a gaming leaderboard dataset. PART 1 creates a Pandas Series of top player scores with custom player-name labels. PART 2 builds a DataFrame of five players with columns Player, Level, Score, and Wins. PART 3 accesses individual rows using df.loc[]. PART 4 loads leaderboard.csv, then calls head(), tail(), and info() to inspect it. PART 5 cleans the CSV data using dropna() and fillna().

import pandas as pd

print("part 1")
top_score = [800,300,560,340,900]
players_names = pd.Series(top_score , index=["player2020" , "i_like_food" , "ange1_0n_1ce" , "swimmer123go", "SIMBA_isTheBest"])
print(players_names)

print("pandas dataframe")
data = {
    "player": ["player2020" , "i_like_food" , "ange1_0n_1ce" , "swimmer123go", "SIMBA_isTheBest"] ,
    "level": [552,89,72,99] ,
    " top score": [800,300,560,340,900] ,
    "wins": [77,89,34,25]

}
df = pd.datsaframe(data)
print(df)

print("part 3")
print("row 0 , for top player")
print(df.loc[0])
print("rows 2, 3 and 4")
print(df.loc[2:3:4])

# print("part 4")




print("part 5")
