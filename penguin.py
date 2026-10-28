import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
print(penguins.head())
print(penguins.shape)
print(penguins.info())
print(penguins.isnull().sum())
penguins = penguins.dropna()

sns.histplot( data=penguins , x= "body_mass_g" )
plt.title("histogram of penguins")
