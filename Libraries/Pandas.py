# """
# @author: Hadeel Moustafa
# Pandas Notes 
# """
# #################################
# # library: 
# #################################
# import pandas as pd 
# import os

# #################################
# # Example:
# #################################
# fileName = 'Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv'
# filePath = os.path.abspath(os.path.join(os.getcwd(), '..' ,'Datasets', fileName))
# Data = pd.read_csv(filePath)
 
# #################################
## Explore and manipulate
# #################################
# Data.head()  # To preview the first few rows of the dataset
# Data.info()  # To get a summary of the data types and non-null counts
# Data.describe()  # To get summary statistics for numerical columns
# Data.index  # to get the row labels of a DataFrame
# Data.columns # to get the column labels of a DataFrame

# #################################
# # create: 
# #################################
# pd.DataFrame(series or lst,index=lst, columns=lst)

# Example with list of lists
#data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # A list of rows
#index_labels = ['Row1', 'Row2', 'Row3']   # Row labels
#column_labels = ['Col1', 'Col2', 'Col3']  # Column labels
#df = pd.DataFrame(data, index=index_labels, columns=column_labels)

#or
# dic = {'x': [1, 2, 3], 'y': [3, 4, 5]}  
# pd.DataFrame(dic)

# pd.Series(lst, index=lst)


# #################################
# Slicing and accessing:
# #################################

# Access a single column
# data['colName']
# Access multiple columns
# data[['Col1', 'Col2']]

# Access a single row
# data.loc[rowIndex] 
# Access multiple rows
# data.loc[['Row1', 'Row2']]



# data.loc[rowIndexStart:rowIndexEnd,:]
# data.loc[:,'colStart':'colStart']

# data.iloc same but not index
# Access a single row by integer position
# data.iloc[0]

# Access a single column by integer position
# data.iloc[:, 0]

# Row slicing by position
# data.iloc[0:2]

# Column slicing by position
# data.iloc[:, 0:2]


# data[data['colName']==value] #creates a boolean Series where each entry is True if the condition is met

#data = pd.DataFrame({'A': [1, 2, 3, 4],'B': ['a', 'b', 'a', 'b']})
# Filter rows where column 'B' is equal to 'a'
#filtered_data = df[df['B'] == 'a']

# data[(data['colName'] == val) & (data['colName'] == val)]

# data[data['colName'].isin(lst)]
# Filter rows where column 'A' is in [1, 3]
# filtered_data = data[data['A'].isin([1, 3])]


# #################################
# Apply:
# #################################
## Apply a lambda function to make sth on each value in colName, fx double (x*2) 
# data['colName'].apply(lambda x : x * 2)

# Apply a lambda function to calculate the sum of 'colName1' and 'colName2' for each row
# data.apply(lambda row : row['colName1']+row['colName2'], axis = 1) 
# axis=1 specifies that the function should be applied to rows 
# axis=0, the function will be applied to columns.

# #################################
# Copy:
# #################################
# data.copy()
# pd.Series.copy() """ pd.Series is a data['colNme'] """


# #################################
# Date:
# #################################
# pd.to_datetime(Data['Date']) # comparsion is okay
# pd.to_datetime(data['Date']).dt.month
# pd.to_datetime(data['Date']).dt.day
# pd.to_datetime(data['Time'].astype(str), format='%H:%M:%S').dt.hour
# pd.to_datetime(data['Time'].astype(str), format='%H:%M:%S').dt.minute

# .astype(str), format='%H:%M:%S' to converts the time data into a string format.

# #################################
# Functions:
# #################################
# data.reset_index(drop=True)

# pd.Series.sort_index()
# pd.Series.sort_values(ascending=False)

# data.drop(columns='colName')
# data.drop(index=rowindex)

# data['colName'].unique()
# data['colName'].nunique()

# data.groupby(['colName','colName'])['ColName'].count()
# data.groupby(['colName','colName'])['ColName'].size().unstack()

# counts = df[df.Category == 'WEAPON LAWS']['DayOfWeek'].value_counts()
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# counts = counts.reindex(weekdays)

# data.shape

# data['colName'].values()


####### examples: 
# fileName = 'MVC_SL_W_Final.csv'
# filePath = os.path.abspath(os.path.join(os.getcwd(), fileName))
# Data.to_csv(filePath)


####### ref 
# .groupby()
# .count()
# .size()
# .unstack()

# .reset_index()
# .sort_index()
# .sort_values()
# .drop()

# .value_counts()
# .shape
# .values
# .index
# .columns
# .copy()
# .apply()

# .loc()
# .iloc()

# .sample(frac=1) """ shuffle rows"""
# .drop(columns=[])
# .rename(columns={colName:toColName})


# Table = pd.pivot_table(df_crimes, index = "Hour", columns = "Category", values = 'PdId' ,aggfunc = 'count')
# The above is equivalent to using .groupby(), then using .unstack().

# .select_dtypes(include=object)

# .to_frame()
