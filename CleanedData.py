# importing all necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("IMDB-Movie-Data.csv")
df

# 1. Display Top 10 Rows of The Dataset
df.head(10)
# 2. Check Last 10 Rows of The Dataset
df.tail(10)
# 3. Finding the  Shape of Our Dataset (Number of Rows And Number of Columns)
df.shape  #shape is attribute it return (rows , column)
# Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns,
# Datatypes of Each Column And Memory Requirement
df.info()
# 4checking the null value in dataset
df.isnull().sum()
#5 Drop All The Missing Values
drop = df.dropna(axis=0)
drop
sns.heatmap(drop.isnull())
plt.show()
#6 heck For Duplicate Data
df.duplicated().any()
# 7Get Overall Statistics About The DataFrame
df.describe()
#8 Display Title of The Movie Having Runtime >= 180 Minutes
df.columns
Run_t180=df[df['Runtime (Minutes)']>=180]["Title"]
Run_t180

#  9In Which Year There Was The Highest Voting?
df.columns
df.groupby("Year")["Votes"].max()
sns.barplot(x="Year",y="Votes",data=df)
plt.title("Votes vs Year")
plt.show()
# 10In Which Year There Was The Highest Revenue?
df.columns
df.groupby("Year")["Revenue (Millions)"].max()
sns.barplot(x="Year",y="Revenue (Millions)",data=df)
plt.title("Revnue Vs Year")
plt.show()
# 11 Find The Average Rating For Each Director

df.columns
df.groupby("Director")["Rating"].mean().sort_values(ascending=False)
# 12Display Top 10 Lengthy Movies Title
df.columns
Top_10 = df.nlargest(10,"Runtime (Minutes)")[["Title","Runtime (Minutes)"]].set_index("Title")
sns.barplot(x="Runtime (Minutes)",y = Top_10.index,data = Top_10)
plt.title("Top 10 movies Lenghty Movies")
plt.show()
# 13 Display Number of Movies Per Year
df.columns
sns.countplot(x = "Year",data=df)
plt.title("Number of movies per year")
plt.show()
# 14 Find Most Popular Movie Title (Higest Revenue)
df.columns

a=df[df["Revenue (Millions)"].max()==df["Revenue (Millions)"]]["Title"]
a
highest = df.nlargest(1, "Revenue (Millions)")
print(highest[["Title", "Revenue (Millions)"]])

# 15Display Top 10 Highest Rated Movie Titles And its Directors
df.columns
le =df.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']]. \
set_index('Title')
sns.barplot(x=le['Runtime (Minutes)'],y=le.index)
plt.title('Top 5 Lengtly Movies')
plt.show()
# .16 Display Number of Movies Per Year
df.columns
sns.countplot(x="Year",data=df)
plt.show()
# 17  Find Most Popular Movie Title (Higest Revenue)
a =df[df["Revenue (Millions)"].max()==df["Revenue (Millions)"]]["Title"]
a
a=df.nlargest(1,"Revenue (Millions)")
print(a[["Title","Revenue (Millions)"]])
# 18 Display Top 10 Highest Rated Movie Titles And its Directors
df.columns
# top_10 = df.nlargest(10,"Rating")[["Title","Rating","Director"]].set_index("Title")
top_10=df.nlargest(10,'Rating')[['Title','Rating','Director']].set_index('Title')
# Mv_10r=Mv_10r.sort_values(by="Rating",ascending=True)
# print(top_10[["Title","Rating","Director"]].sort_values(by="Rating",ascending=True))

sns.barplot(x=top_10['Rating'],y=top_10.index)
plt.title("Display Top 10 Highest Rated Movie Titles")
#  19 Display Top 10 Highest Revenue Movie Titles
df.columns
a=df.groupby("Title")["Revenue (Millions)"].max()
b=a.sort_values(ascending=False)
b[0:10]
z=df.nlargest(10,"Revenue (Millions)")[["Title","Director","Revenue (Millions)"]].set_index("Title")

sns.barplot(x=z["Revenue (Millions)"],y=z.index)
plt.title("Top 10 Movies with High Revenue")
plt.show()

#  Find Average Rating of Movies Year-wise
df.groupby("Year")["Rating"].mean()
# df.columns
sns.barplot(x="Year",y="Rating",data=df)
# 19. Does Rating Affect The Revenue?
sns.scatterplot(x="Rating",y="Revenue (Millions)",data=df)
plt.title("Comparison Through Scatterplot")
plt.show()
# 20. Classify Movies Based on Ratings [Good,Better and Best]

def rating(rating):
    if rating>=7.0:
        return 'Excellent'
    elif rating>=6.0:
        return 'Good'
    else:
        return 'Average'
df['rating_cat']=df['Rating'].apply(rating)
df.head(10)

# 21. Count Number of Action Movies
df.columns
a=df['Genre']=="Action"
len(a)
len(df[df['Genre'].str.contains('action',case=False)])
# 22.Find Unique values from Genre
df.columns

list1=[]
for value in df["Genre"]:
  list1.append(value.split(","))

list1
one_d=[]
for item in list1:
  for item1 in item:
    one_d.append(item1)

one_d
# 23 how many films of each genre were made
uni_list=[]
for item in one_d:
  if item  not in uni_list:
    uni_list.append(item)

uni_list

# -----Project Completed--------#
