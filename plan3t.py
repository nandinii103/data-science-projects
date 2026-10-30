import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("planets")
df = df.dropna()
print(df.head())

sns.barplot(x = "method" , y = "mass" , data = df)
plt.title("Average Planet Mass")
plt.xlabel("method")
plt.ylabel("average mass")
plt.show()

sns.countplot(x= "method" , data= df)
plt.title("number of planets in total")
plt.xlabel("mass")
plt.ylabel("count")
plt.show()

sns.boxplot(x = "method" , y = "orbital period" , data=df)
plt.title("orbital period")
plt.xlabel("method")
plt.ylabel("orbital period in days")
plt.yscale("log")
plt.show()

sns.swarmplot(x = "method" , y = "mass" , data=df)
plt.title("planet mass")
plt.xlabel("method")
plt.ylabel("mass")
plt.yscale("log")
plt.show()

sns.jointplot(x = "orbital period" , y = "mass" , data=df)
plt.show()

sns.jointplot(x= "orbital period" , y= "mass" , data=df , kind= "kde")
plt.show()

sns.pointplot(x = "method" , y = "mass" , data=df)
plt.title("average planet mass")
plt.xlabel("method")
plt.ylabel("mass")
plt.show()

