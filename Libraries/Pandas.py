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
## Explore and manipulate
# #################################
# Data.head()  # To preview the first few rows of the dataset
# Data.tail()  # To preview the last few rows of the dataset
# Data.info()  # To get a summary of the data types and non-null counts
# Data.describe()  # To get summary statistics for numerical columns
# Data.describe(include=['object']) # To apply the method "describe" on the variables of type 'object'
# Data.index  # to get the row labels of a DataFrame
# Data.columns # to get the column labels of a DataFrame
# Data.rename(columns={'old_name': 'new_name'}, inplace=True)
# Data[['rowname1', 'rowname2', 'rowname3', ...]].corr() #Find the correlation between the following columns
#  df['rowname1'].value_counts().idxmax() #the most frequent value of the attribute.

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

# iloc: Selecting Rows by Index
#loc:Selecting Rows by Label	

# data[data['colName']==value] #creates a boolean Series where each entry is True if the condition is met

#data = pd.DataFrame({'A': [1, 2, 3, 4],'B': ['a', 'b', 'a', 'b']})
# Filter rows where column 'B' is equal to 'a'
#filtered_data = df[df['B'] == 'a']

# data[(data['colName'] == val) & (data['colName'] == val)]

# data[data['colName'].isin(lst)]
# Filter rows where column 'A' is in [1, 3]
# filtered_data = data[data['A'].isin([1, 3])]


# #################################
## Deal with missing data:
# #################################
# Data.replace('?',np.NaN, inplace = True) #replace the "?" symbol with NaN 
# Data.dropna(subset=['rowname'], axis=0, inplace=True) # remove missing value
# Data.reset_index(drop=True, inplace=True) # reset index, because we droped two rows

# avg = df["colname"].astype("float").mean(axis = 0)
# Data['rowname'].replace(np.nan, avg, inplace = True) # replace missing value
# Data.drop_duplicates() #Removing Duplicates	

#identify the entries having Null values
#missing_data = data.isnull()

#Count missing values in each column
#for column in missing_data.columns.values.tolist():
#    print(column)
#    print (missing_data[column].value_counts())
#    print("")   


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

# Data['Date'].count() Report the total number of x in the dataset

# pd.to_datetime(Data['Date']) # comparsion is okay
# pd.to_datetime(data['Date']).dt.month
# pd.to_datetime(data['Date']).dt.day
# pd.to_datetime(data['Time'].astype(str), format='%H:%M:%S').dt.hour
# pd.to_datetime(data['Time'].astype(str), format='%H:%M:%S').dt.minute

# .astype(str), format='%H:%M:%S' to converts the time data into a string format.
# Data.['rowname'].astype('int') #convert data type of price fx to int



# #################################
# Functions:
# #################################
# data.reset_index(drop=True)

# pd.Series.sort_index()
# pd.Series.sort_values(ascending=False)

# data.drop(columns='colName')
# data.drop(index=rowindex)

# data['colName'].unique() List the various categories of x
# data['colName'].nunique() How many x category are there?


# Data['colName'].value_counts(ascending=False) List the number of x in each category:
# Data['colName'].value_counts.to_frame() make it as a table
# Data['colName'].value_counts(ascending=False).plot(kind='bar', figsize =(8,8)) # Create a histogram over x occurrences:



###### grouping

# data.groupby(['colName','colName'])['ColName'].count()
# data.groupby(['colName','colName'])['ColName'].size().unstack()

# counts = df[df.Category == 'WEAPON LAWS']['DayOfWeek'].value_counts()
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# counts = counts.reindex(weekdays)

# data.shape

# data['colName'].values()

# pd.get_dummies(data['']) transforms categorical variables into (1,0)

#OR For making different plots

#grouping = data.groupby(['Category','DayOfWeek'], as_index=False).mean()

#pivot
#pivot_table = grouping.pivot(index='Category', columns='DayOfWeek')
#or
#heatmap
#plt.pcolor(grouping,camp='RdBu')
#plt.colorbar()
#plt.show()


# deatals heatmap
#fig, ax = plt.subplots()
#im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
#row_labels = grouped_pivot.columns.levels[1]
#col_labels = grouped_pivot.index

#move ticks and labels to the center
#ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
#ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
#ax.set_xticklabels(row_labels, minor=False)
#ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
#plt.xticks(rotation=90)

#fig.colorbar(im)
#plt.show()


####### bins:
#num_bins = x  # Number of bins
#bins = np.linspace(df['Values'].min(), df['Values'].max(), num_bins + 1)

# group_name=['low', 'medium','high']
# Apply binning with pd.cut
#df['Binned'] = pd.cut(df['Values'], bins=bins, labels=[f'Bin {i}' for i in range(1, num_bins + 1)], right=False)
#df['Binned'] = pd.cut(df['Values'], bins=bins, labels=group_name, include_lowest=True)



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
