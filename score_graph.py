import matplotlib.pyplot as plt
data = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]
score = [89,56,34,12,67]
plt.plot(data , score , color="pink" , marker = "o" , linestyle="--")
plt.title("quiz scores linegraph")
plt.xlabel("days")
plt.ylabel("scores")
plt.ylim(0,100)
plt.grid()
plt.show()

plt.bar(data,score , color= "blue" )
plt.title("quiz scores bar chart")
plt.xlabel("days")
plt.ylabel("scores")
plt.grid()
plt.show()