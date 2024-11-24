# pandas used for data manipulation and analysis.
# creating  a dataframe
import pandas as pd

#creating a dataframe from a dictionary
data = {'Name': ['Alice','Bob','Charlie'],
        'Age' : [24,25,27],
        'City' : ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
# print(df)

# filter_df = df[df['Age'] > 25]
# print(filter_df)

#Adding a new column
# df['IsAdult'] = df['Age'] > 24
# print(df)

# Removing a column
# df.drop(columns=['City'], inplace = True)
# print(df)
# OR
# print(df.drop(columns=['City']))


#Reading a csv file into a Dataframe

# df = pd.read_csv('data.csv')
# print(df.head()) # display the first few rows of the Dataframe
# print((df.head(2))) # it only gives 2 rows of csv file

# writing a dataframe to a csv file
# df.to_csv('output3.csv',index=False) # specity index=False to avoid writing row numbers
# print(df)
# selecting a single column
# print(df["Name"])


