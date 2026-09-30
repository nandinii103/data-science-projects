import numpy as np
import pandas as pd

subjects = ["Math" , "science" , "english" , "computer science" ]
max_marks = pd.Series([100,100,100,100] , index=subjects)
data = {
    "maths":[85,90, np.nan , 78] , 
    "science":[92,88,76,95] ,
    "english":[78,85,70,65] ,
    "computer science":[95,92,89,90]
}

df = pd.DataFrame(data, index=["Student_1" , "Student_2" , "Student_3" , "Student_4"])
print("dataframe")
print(df)

print("data info")
print(df.info)

df_cleaned = df.fillna(50)
print("filled missing value and empty spaces")
print(df_cleaned)

