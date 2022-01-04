#!/usr/bin/env python
# coding: utf-8

# In[20]:


import os
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

netflix_stocks = pd.read_csv("NFLX.csv")
dowjones_stocks = pd.read_csv("DJI.csv")
netflix_stocks_quarterly = pd.read_csv("NFLX_daily_by_quarter.csv")

# rename columns
netflix_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)
dowjones_stocks.rename(columns = {'Adj Close': 'Price'}, inplace = True)
netflix_stocks_quarterly.rename(columns = {'Adj Close': 'Price'}, inplace = True)


# visualizing the netflix quarterly data
ax = plt.subplot()
sns.violinplot(data = netflix_stocks_quarterly, x = "Quarter", y = "Price")
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
plt.xlabel("Business Quarters in 2017")
plt.ylabel("Closing Stock Price")

plt.savefig("Distribution of 2017 Netflix Stock Prices by Quarter.png")
plt.show()

# scatter plot
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

ax2 = plt.subplot()
plt.scatter(x_positions, earnings_actual, color = "red", alpha = 0.5)
plt.scatter(x_positions, earnings_estimate, color = "blue", alpha = 0.5)
plt.legend(["Actual", "Estimate"])
plt.title("Earnings Per Share in Cents")
ax2.set_xticks(x_positions, chart_labels)

plt.savefig("Earnings Per Share.png")
plt.show()

# side by side bar plot
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

n = 1
t = 2
d = 4
w = 0.8
bars1_x = [t*element + w*n for element in range(d)]
plt.bar(bars1_x, revenue_by_quarter, label = "Revenue")

# Earnings
n = 2
t = 2
d = 4
w = 0.8
bars2_x = [t*element + w*n for element in range(d)]
plt.bar(bars2_x, earnings_by_quarter, label = "Earnings")

plt.legend()
plt.title("Revenue vs Earnings")

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
plt.xticks(middle_x, quarter_labels)

plt.savefig("evenue vs Earnings")
plt.show()

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]



# subplots
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title("Netflix")
plt.xlabel("Date")
plt.ylabel("Stock Price")

ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title("Dow Jones")
plt.xlabel("Date")
plt.ylabel("Stock Price")

plt.subplots_adjust(wspace=.5)

plt.savefig("Stock Proces Netflix vs. Dow Jones.png")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




