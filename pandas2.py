import pandas as pd

# #creating a dataframe from a dictionary
# data = {'Name': ['Alice','','Bob','Charlie','Jake','','Rae'],
#         'Age' : [24,25,None,27,None,34,26],
#         'City' : ['New York', 'Los Angeles','', 'Chicago','Berlin','Bejing',''],
#         'Date': ['2024/12/14','2024/12/15','2024/12/16','20241217','2024/12/18','20241219','2024/12/20']}

# df = pd.DataFrame(data)
# print(df)
# df['Date'] = pd.to_datetime(df['Date'],format = "ISO8601")
# print(df.to_string())

# for x in df.index:
#     if df.loc[x, "Age"] < 30:
#         df.loc[x, "Age"] = 25
# print(df)

# for x in df.index:
#     if df.loc[x, "Age"] > 30:
#         df.drop(x, inplace=True)   

# print(df)              

# new_df = df.dropna()
# print(new_df)

# df.fillna(130,inplace=True)
# print(df)

# deleting the duplicates row 

# data1 = {'Name': ['Alice','Bob','Alice','Charlie'],
#         'Age' : [24,25,24,27],
#         'City' : ['New York', 'Los Angeles','New York', 'Chicago']} 

# df = pd.DataFrame(data1) 
# # print(df)
# df.drop_duplicates(inplace=True)
# print(df)

