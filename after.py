
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


body_mass = [3750, 3800, 3250, 3450, 3650]

penguins_names = pd.Series(
    body_mass,
    index=[
        "penguin1",
        "penguin2",
        "penguin3",
        "penguin4",
        "penguin5",
    ],
)

print(penguins_names)

masses = np.array(body_mass)

print(np.mean(masses))
print(np.max(masses))
print(np.min(masses))


data = {
    "penguin": [
        "penguin1",
        "penguin2",
        "penguin3",
        "penguin4",
        "penguin5",
    ],
    "bill_length": [39.1, 46.1, 50.0, 38.7, 45.2],
    "flipper_length": [181, 211, 196, 195, 210],
    "body_mass": [3750, 4500, 3800, 3450, 4400],
}

df = pd.DataFrame(data)

print(df)
print(df.loc[0])
print(df.loc[1:3])


penguins = sns.load_dataset("penguins")

print(penguins.head())
print(penguins.tail())
penguins.info()


clean_data = penguins.dropna()
print(clean_data.head())

filled_data = penguins.fillna(0)
print(filled_data.head())


bill_lengths = clean_data["bill_length_mm"].to_numpy()

print(np.mean(bill_lengths))
print(np.median(bill_lengths))
print(np.std(bill_lengths))


sns.scatterplot(
    data=clean_data,
    x="bill_length_mm",
    y="flipper_length_mm",
    hue="species",
)

plt.show()

