#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("TTM.csv")
df.head()
df.shape

#set date as index
df= df.set_index(pd.DatetimeIndex(df['Date'].values))
df

#create funtion to get moving average 
def SMA (data , period = 30 , column = "Close"):
  return data[column].rolling(window=period ).mean()

#create the column to store the short sma and long sma
df["shortSMA"] = SMA(df , 50)
df["longSMA"] = SMA(df , 150)

#plot the chart
column_list = ["shortSMA" , "longSMA" , "Close"]
df[column_list].plot(figsize=(15,6))
plt.title("death / golden ratio")
plt.show()

#create the funtion to see the dates of each death and golden cross over
def death_gold_ratio():
  first_cross = 0
  #loop through the dataset
  for i in range(0 , len(df)):
    if df["shortSMA"][i]<df["longSMA"][i] and first_cross == 0:
      print("death cross on day " , df.index[i] , "expect price to continue to fall")
      first_cross = 1
    elif df["longSMA"][i]<df["shortSMA"][i] and first_cross == 1:
      print("death golden ratio on this day",df.index[i],"expect price to continue to rise")
      first_cross = 0

#run the function
death_gold_ratio()
