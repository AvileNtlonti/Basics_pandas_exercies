import pandas as pd
#Read the hacker_news.csv file from data directory
df=pd.read_csv('hacker_news.csv')
print(df)
#Get the first five rows
print(df.head())
#Get the last five rows
print(df.tail())
#Get the title column as pandas series
print(df.columns)
#Count the number of rows and columns
print(df.shape)