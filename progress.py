import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
savings = [100, 250, 224, 500, 320]  


plt.plot(days, savings, marker="o", color="blue", linestyle="--")
plt.title("Weekly Savings Line Graph")
plt.xlabel("Days of the Week")
plt.ylabel("Savings (£)")
plt.ylim(0, 600)
plt.grid()
plt.show()


plt.bar(days, savings, color="purple")
plt.title("Weekly Savings Bar Chart")
plt.xlabel("Days of the Week")
plt.ylabel("Savings (£)")
plt.grid()
plt.show()

