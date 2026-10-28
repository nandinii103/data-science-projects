import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("tips")
df = df.dropna()
print(df.head())
print(df.info())

sns.barplt(x = "days" , y = "total no of bills" , hue= "sex" , data = df)
plt.title("average total bill")
plt.xlabel("day")
plt.ylabel("average bills")
plt.show()

sns.countplot(x = "day" , hue = "sex" , data=df)
plt.title("number of diners per day")
plt.xlabel("days")
plt.ylabel("count/number")
plt.show()
sns.boxplot(x = "days" , y = "total bills" data=df)
plt.title("total bill per day")
plt.xlabel("day")
plt.ylabel("total bills")
plt.show()

sns.striplot(x = "days" , y ="total bill" data= df)
plt.title("amount per day")
plt.xlabel("day")
plt.ylabel("total")
plt.show()

sns.swarmplot(x = "days" , y="total bill" , data=df)
plt.title("bill per day")
plt.xlabel("days")
plt.ylabel("total bills")
plt.show()

sns.jointplot(x="total bill" , y="tips" , data=df , kind= "kde")
plt.subtitle("taoal and tips ")
plt.show()

sns.jointplot(x="total bill" , y="tips" , data=df , kind= "kde")
plt.subtitle("taoal and tips KDE joint plot ")
plt.show()


