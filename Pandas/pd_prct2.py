import numpy as np
import pandas as pd

lst=[['Aarke', 20], ['Mayank', 20], ['Raunak', 19]]


df=pd.DataFrame([['Aarke', 20], ['Mayank', 20], ['Raunak', 19]], columns=['Name', 'Age'])
print(df)

print('\n\n')

lst2=[['NewYork (City)', 'NewDelhi (Delhi)', 'London', 'Abu Dhabi', 'neworleans'], [10565000, 105860000, 5000000, 8500000, 7800000], [700000, 50000, 500000, 2500000, 65000]]
df2=pd.DataFrame({'City':lst2[0], 'Population':lst2[1], 'Living Cost':lst2[2]})
print(df2)

print('\n\n')

def updatation_of_df(df):
        df_updated = df2.replace(to_replace ='[nN]ew', value = 'New_', regex = True)
        return df_updated

print('\n\n')

# Importing re package for using regular expressions
import re

# Function to clean the names
def Clean_names(City_name):

	# Search for opening bracket in the name followed by any characters repeated any number of times
	if re.search('\(.*', City_name):

		# Extract the position of beginning of pattern
		pos = re.search('\(.*', City_name).start()

		# return the cleaned name
		return City_name[:pos]

	else:
		# if clean up needed return the same name
		return City_name
		
# Updated the city columns
df2['City']=df2['City'].apply(Clean_names)

# Print the updated dataframe
df2 = updatation_of_df(df2)
print(df2)

print('\n\n')

# List of nested dictionary initialization
lst3 = [
        {
        "Student": [{"Exam": 90, "Grade": "a"},
                    {"Exam": 99, "Grade": "b"},
                    {"Exam": 97, "Grade": "c"},
                   ],
        "Name": "Paras Jain"
        },
        {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                   ],
        "Name": "Chunky Pandey"
        }
       ]
  
print(lst3)

print('\n\n')

rows = []
  
# appending rows
for data in lst3:
    data_row = data['Student']
    time = data['Name']
      
    for row in data_row:
        row['Name']= time
        rows.append(row)
  
# using data frame
df3 = pd.DataFrame(rows)
print(df3)

print('\n\n')

lst4=df3['Name'].unique()
lst5=[]

df3.set_index('Name', inplace=True)

for i in lst4:
	lst6=[]
	df4=df3.loc[i]
	for j in list(df4['Exam']):
		lst6.append(j)
	lst5.append(lst6)

for i in lst5:
	i.reverse()

for i in range(len(lst5)):
	lst5[i].append(lst4[i])

for i in lst5:
	i.reverse()

df5=pd.DataFrame(lst5, columns=[ 'Name', 'Maths', 'Physics', 'Chemistry'])
df5.set_index('Name', inplace=True)
print(df5)

print('\n\n')

#Creating a dataframe from multiple series
author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti']
article = [210, 211, 114, 178]
  
auth_series = pd.Series(author)
article_series = pd.Series(article)
  
frame = { 'Author': auth_series, 'Article': article_series }
  
result = pd.DataFrame(frame)
age = [21, 21, 24, 23]
  
result['Age'] = pd.Series(age)
  
print(result)

print('\n\n')


#Cleaning the string data in the given Pandas Dataframe
df6 = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':[' UMbreLla', '  maTress', 'BaDmintoN ', 'Shuttle'],
                   'Updated_Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 8, 15, 10]})

def clean_names2(i):
        return i.strip().capitalize()                                #Capitalize function capitalizes the first letter of the string and makes the rest small

df6['Product']=df6['Product'].apply(clean_names2)
print(df6)

print('\n\n')



'''_______________________________________Mapping Data_________________________________'''




#Mapping external value to a dataframe means using different sets of values to add in that dataframe by keeping the keys of external dictionary as same as the one column of that dataframe.



#Creating new dataframe
initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'], 
        'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'], 
        'Age': [42, 52, 36, 21, 23], 
        'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}
  
df7 = pd.DataFrame(initial_data)
  
# Create new column using dictionary
new_data = { "Ram":"B.Com",
             "Mohan":"IAS",
             "Tina":"LLB",
             "Jeetu":"B.Tech",
             "Meera":"MBBS" }
  
# combine this new data with existing DataFrame
df7["Qualification"] = df7["First_name"].map(new_data)
  
print(df7)

print('\n\n')

#Similarly data can be replaced by mapping or using the replace method or update method of pandas dataframe

new_data2={'Ram':'Shyam',
           'Mohan':'Sohan',
           'Tina':'Rina'}

df7['First_name']=df7['First_name'].map(new_data2)
print(df7)

print('\n\n')

#the replacement can also be done by using the replace function of pandas dataframe

new_data3={'Shyam':'Ram',
           'Sohan':'Mohan',
           'Rina':'Tina'}

df7=df7.replace({'First_name':new_data3})
print(df7)

print('\n\n')

new_data4={ 0:"Shyam",
            2:"Riya",
            3:"Jitender" }

df7['First_name'].update(pd.Series(new_data4))
print(df7)

print('\n\n')


        




#___________________________________________________________________________________________________________________________________________________________________________________________






'''___________________________________________________________________________ABOUT ROWS_________________________________________________________________________________________________'''






'''_____________________________________Reshaping a pandas DataFrame using stack,unstack and melt method_______________________________________'''




df8 = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
print(df8.head())

print('\n\n')

df_stacked = df8.stack()
print(df_stacked.head())               #The stack method stacks all rows as columns on top of each other with every column name infront of the related data everytime(i.e., for every row)

print('\n\n')

#Similarly a stacked dataframe can be unstacked
df_unstacked=df_stacked.unstack()
print(df_unstacked.head())                         #Basically, df_unstacked is the same as df8

print('\n\n')

#Dataframes in pandas can aslo be rehaped using melt method. Melt in pandas reshape dataframe from wide format to long format. It uses the “id_vars[‘col_names’]” for melt the dataframe by column names.
df_melt = df8.melt(id_vars =['Name', 'Team']) 
print(df_melt.head())

print('\n\n')




'''____________________________________Iterating(Going through) rows of a dataframe_______________________________________'''




#Rows can be iterated through iterrows() and itertuples() methods



#iterating through iterrows() method
input_df = [{'name':'Sujeet', 'age':10},
            {'name':'Sameer', 'age':11},
            {'name':'Sumit', 'age':12}]
  
df9 = pd.DataFrame(input_df)
print('Original DataFrame: \n', df9)

print('\n\n')
  
print('\nRows iterated using iterrows() : ')
for index, row in df9.iterrows():
    print(row['name'], row['age'])

print('\n\n')

#Not discussing the itertuples method as it is very ugly




#Selecting rows on the basis of certain conditions

#One way to filtering the rows is though vectorisation as discussed below

filtered_df=df9[df9['age']>10]
print(filtered_df)

print('\n\n')

#Similarly rows can also be filtered on the basis of certain condityions by using the query method of pands dataframe

print(df9.query('age > 10'))            #The result will be the same as from the above command

print('\n\n')

print(df9.loc[df9['age']>10])                  #Above code can also be written in this way, i.e., by using loc method

print('\n\n')

#Selecting those rows whose column value is present in the list using isin() method of the dataframe.

city=['Varanasi', 'Mumbai', 'Delhi', 'Bangalore']
filtered_df2=df7[df7['City'].isin(city)]
print(filtered_df2)

print('\n\n')

#Selecting all the rows from the given dataframe in which ‘Stream’ is not present in the options list

filtered_df3=df7[~df7['City'].isin(city)]
print(filtered_df3)

print('\n\n')


#Selecting rows based on multiple column conditions using '&'(and) or '|'(or) operator.
filtered_df4=df7[(df7['City'].isin(city)) & (df7['Age']>35)]            #Not enclosing each condition in paranthesis somehow gives a empty dataframe, maybe its a fault or something
print(filtered_df4)

print('\n\n')

filtered_df5=df7[(df7['City'].isin(city)) | (df7['Age']>35)]
print(filtered_df5)

print('\n\n')

#Selecting rows that contain certain substrings
filtered_df6=df7[df7['Qualification'].str.contains('B.')]
print(filtered_df6)

print('\n\n')


#Selecting any row from a Dataframe using iloc[] and iat[] in Pandas

#Rows can be selected by indexing through iloc[] and loc[] method as studied before but iat[] method takes two indices, one for row and one for column

for i in range(df9.shape[0]):
        for j in range(df9.shape[1]):
                print(df9.iat[i,j], end='\n')

print('\n\n')

#Another way to filter the rows is to drop the unwanted rows by using the drop function of pandas dataframe

print(df7.drop(df7[df7['Age']<=35].index))              #This shows that the drop fuction of the dataframe takes a dataframe itself and then removes that dataframe from the dataframe on which it is being applied to

print('\n\n')



#Writing a function to insert a row at desired position in a dataframe


def insert_row(df, pos, data_list):
        lst=[*range(0, pos, 1)]+[*range(pos+1, df.shape[0]+1, 1)]             #the asterisk before the range actually defines the length of the list by expanding the range function
        df.index=lst
        df.loc[pos]=data_list
        return df.sort_index()

df9=insert_row(df9, 2, ['Aarke', 19])
print(df9)

print('\n\n')

#Another function to perform the same task as the above function using concat function of pandas

def insert_row2(df, pos, data_list):
        df1=df[:pos]
        df2=df[pos:]
        df1.loc[pos]=data_list         
        result_df=pd.concat([df1, df2])
        result_df.index=[*range(result_df.shape[0])]           ##Always remember to redifine the index of the artificial dataframe properly
        return result_df

df9=insert_row2(df9, 3, ['Vivek', 18])
print(df9)        

print('\n\n')

print(df9[1:2])


#Ranking rows of dataframe based on a column using rank method of pandas dataframe


df9['age_ranking']=df9['age'].rank(ascending=1)          #setting the value of ascending attribute to 1 will rank the rows in ascending order of the attended column values and setting it to 0 will rank them in descending order
print(df9)

print('\n\n')


#Sorting rows of dataframe using sort_values function of pandas dataframe

df9=df9.sort_values(by=['age', 'name'], ascending=True)            #by attribute of the sort_values function takes a column name or a list of column names of the dataframe it is being applied to and sorts the rows on the basis of that column first in the row and then according to the column second in it in either ascending or descending based on given command
print(df9)

print('\n\n')


#getting standard deviation value for every column of a datarame


print(df9.std())                          #Similarly maximum and minimum values and other calculational values can be obtained for every row. since std can only be applied on numbers, so the result will also contain the data reated to the colunmns that contain numerical data

print('\n\n')


#Pivoting a dataframe


df10 = pd.DataFrame({'Name': ['Geeks', 'Peter', 'James', 'Jack', 'Lisa'],
                   'Team': ['Boston', 'Boston', 'Boston', 'Chele', 'Barse'],
                   'Position': ['PG', 'PG', 'UG', 'PG', 'UG'],
                   'Number': [3, 4, 7, 11, 5],
                   'Age': [33, 25, 34, 35, 28],
                   'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'],
                   'Weight': [89, 79, 113, 78, 84],
                   'College': ['MIT', 'MIT', 'MIT', 'Stanford', 'Stanford'],
                   'Salary': [99999, 99994, 89999, 78889, 87779]},
                   index =['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])

print(df10)

print('\n\n')


#A dataframe can be pivoted by using the pivot function of padas dataframe, i.e. the data of one column can be used as index while another column's data be used as the columns itself.

pivoted_df= df10.pivot(index='Position', columns='Name')
print(pivoted_df)

print('\n\n')



#Selecting random rows from a dataframe

#One way to select a random row from a dtaframe is to use the sample function of the dataframe

print(df10.sample(n=3))            #the parameter n takes an integral value and returns that many roes from the dataframe randomly

print('\n\n')

print(df10.sample(frac=0.5))       #similarly the parameter frac takes a fractional value and returns that much part of the dataframe(for example, here it retruns 0.5 fraction or part of the dataframe)

print('\n\n')

#sample also allows to select desired number of random columns inplace of rows by ssetting the axis attribute of the sample function
print(df10.sample(n=2, axis=1))

print('\n\n')


#random rows can also be selected using numpy arrays and loc method of pandas datframe







#___________________________________________________________________________________________________________________________________________________________________________________________








'''_________________________________________________________________________________ABOUT COLUMNS_________________________________________________________________________________________'''





#Renaming a column

#A column can be renamed using rename function of pandas dataframe

print(df10.rename(columns={'Number':'Numbers', 'Team':'team'}))          #The change is still not applied the original dataframe and can be applied on it by setting the inplace attribute to True

print('\n\n')

#Similarly columns can also be renamed by indexing and slicing through the values attribute of columns fumction of pandas dataframe

df10.columns.values[3]='Numbers'
print(df10)

print('\n\n')

#Columns can also be renamed using the columns function of pandas datarame itself

df10.columns=['Name', 'Team', 'Position', 'Number', 'Age', 'Height', 'Weight', 'College', 'Salary']
print(df10)

print('\n\n')

#One way to detect if certain column names are present in a dataframe

print({'Position', 'Number'}.issubset(df10.columns))            #This returns a boolean value depending on the fact that whether the items in the array on which the issubset method is being applied on are the subset of the dataframe defined under the issubset method

print(type({'a','b'}))                                          #This is to show that the array in the curly brackets is known as python set(will have to study about it later)

print('\n\n')

#NOTE - Basically set is just like the sets from maths and contains all teh fuctions and methods that the sets in maths contain. so it has basically one advantage over other arrays that it unly stores values uniquely, i.e., only once and thus preventing any sort of data duplicacy


#Creating new columns in a dataframe based on certain conditions

map_dict_df10={'PG':'Senior', 'UG':'Junior'}
df10['Designation']=df10['Position'].map(map_dict_df10)
print(df10)

print('\n\n')

#Same can be done by using apply function

def set_value(row_number, assigned_value):
        return assigned_value[row_number]

map_dict2_df10={'MIT':'Honor student', 'Stanford':'Average Student'}
df10['Student Type']=df10['College'].apply(set_value, args=(map_dict2_df10,))
print(df10)

print('\n\n')


#Splitting a column in Pandas dataframe and getting part of it (the returned part is actually a pandas series)

print(df10['Height'].str.split('-').str[0])                    #str is a special attribute of pandas dataframes and series and can be used to perform various string based operations on dataframes and their columns

print('\n\n')

lst_df=df10['Height'].str.split('-').str[0]
print(lst_df)
print(type(lst_df))

print('\n\n')

#Creating a dataframe by splittin a string into columns

movie_data = ["Name: The_Godfather, Year: 1972, Rating: 9.2",
            "Name: Bird_Box, Year: 2018, Rating: 6.8",
            "Name: Fight_Club, Year: 1999, Rating: 8.8"]

lst_of_movie=[]
rand_lst=movie_data[0].split(':')
lst_of_columns=[i for i in range(len(rand_lst)-1)]
for i in movie_data:
        lst=i.split(':')
        lst_of_columns[0]=lst[0]
        for j in range(1,len(lst)-1):
                lst2=lst[j].split(',')
                lst_of_columns[j]=lst2[1]
                lst[j]=lst2[0]
        lst.remove(lst[0])
        lst_of_movie.append(lst)

movie_df=pd.DataFrame(lst_of_movie, columns=lst_of_columns)
print(movie_df)
                        
print('\n\n')

#Getting frequency of items in one or more columns

#One way to this is by using value_counts() method of pandas series

print(df10['Position'].value_counts())

print('\n\n')

#another method is by using the count function of the groupby method of pandas dataframe

print(df10.groupby(['Position', 'College']).count())           #Groupby method groups the data in the datframe on the basis of the items in the column(or columns if multiple columns are passed under it) passed under it

print('\n\n')

#another method is by using the size function of the groupby method of pandas dataframe

print(df10.groupby(['Position']).size())                  #It actually works the same as count method      

print('\n\n')


#Changing the data type of columns in dataframe

#one way is to use the datframe.astype() method. it changes all the columns to a particular data type if the data type is passeddf as a argument in the method or changes the data type of particular columns to the particular data types if a dictionary is passed as an argument containing column names as keys and the data types to be assigned as values.\

df10=df10.astype(str)
print(df10.dtypes)

print('\n\n')

convert_dict = {'Number': float,
                'Age': float}
  
df10= df10.astype(convert_dict)
print(df10.dtypes)

print('\n\n')

#datatypes of columns can also be changed by using dataframe.apply method

df10[['Number']]=df10[['Number']].apply(pd.to_datetime)        #similarly, We can pass pandas.to_numeric, pandas.to_datetime and pandas.to_timedelta as argument to apply() function to change the datatype of one or more columns to numeric, datetime and timedelta respectively
print(df10.dtypes)

print('\n\n')

#Splitting a text column into two columns in Pandas DataFrame

df11=df2['City'].str.split(expand=True)               #setting expand parameter to true gives a dataframe that contains the each half of the splitted text as data in each column in it. otherwise it would return a series containing lists consisting of each halves of the splitted text as their items
print(df11)                                           #the dataframe df11 can be then assigned to the two columns which are solely created for the assignment of the splitted data 

print('\n\n')


#finding the difference between two columns of a dataframe

rand_dic={'Salary':int,'Weight':int}
df10=df10.astype(rand_dic)

df10['Diff_bw_pos&sal']=df10['Salary']-df10['Weight']
print(df10)

print('\n\n')

#getting the index of the row with max value in a particular column

#one way is the traditional one by using conditioning 

print(df10[df10['Diff_bw_pos&sal']==df10['Diff_bw_pos&sal'].max()].index)

print('\n\n')

#another way is using the idxmax method

print(df10['Salary'].idxmax())

print('\n\n')


#dropping one or more columns. just like rows columns can also be dropped by using the drop method of pandas dataframe

print(df10.drop(['Position'], axis=1))

print('\n\n') 

#formatting the data in particular column of a datframe. here we will take the example of lowercasing the data in a dataframe column

df10['Position']=df10['Position'].str.lower()
print(df10)

print('\n\n')
