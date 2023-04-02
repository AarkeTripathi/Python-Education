import time
t1=time.time()
import numpy as np
import pandas as pd

movies_data=pd.read_csv(r'D:\tmdb_5000_movies.csv')     #read_csv class of pandas module reads the csv file and returns a data frme which is stored in movies_data variable
print(movies_data)
print(type(movies_data))        #this will show that movis_data is a data frame which will contain a dataset of the data in the csv file it is reading

print('\n\n')       #this creates some space between two elements of the program when the code is executed

#A pandas dataframe can also be created from the text in the clipboard
text="""Date;Event;Cost
    10/2/2011;Music;10000
    11/2/2011;Poetry;12000                
    12/2/2011;Theatre;5000
    13/2/2011;Comedy;8000
    """                                     #This is the text to be copied on the clipboard

text_data=pd.read_clipboard(sep=';')        #sep attribute defines the symbol which is to be used as a seperator for data within different columns in the clipboard
print(text_data)

print('\n\n')

movies_data_selective=pd.read_csv(r'D:\tmdb_5000_movies.csv', usecols=['runtime'])      #usecols attribute takes a lsit of selective columns in the csv file and creates a data frame consisting of those columns only
print(movies_data_selective)

print('\n\n')

print(movies_data.shape)        #returns the shape of movies_data data frame

print('\n\n')

print(movies_data.size)         #returns the size of data frame, i.e., total number of values in data frame (multiplication of rows and columns)      

print('\n\n')

print(movies_data.count())      #returns number of values in each column in the data frame that are defined and not null

print('\n\n')

print(movies_data.sum().runtime)       #returns the sum of values in the given column, given that the values in the column are of numerical data type
#movies_data.runtime.sum() will also work as movies_data.runtime will be a series and the sum() function of series will then be applied to it

print('\n\n')

print(movies_data.columns)      #returns list of columns

print('\n\n')

print(sorted(movies_data))      #applying sorted function on a dataframe also returns a list containing of all the column names in the dadtaframe sorted in alphabetical order

print('\n\n')

print(movies_data.index)        #returns starting, stopping and stepping value of index 

print('\n\n')

print(movies_data.head(10))       #head method of read_csv class returns first 10 rows of movies_data. If no value is entered in place of 10, it returns first 5 rows by default

print('\n\n')

print(movies_data.tail(10))       #tail mrthod of read_csv class returns last 10 rows of movies_data. If no value is entered in place of 10, it returns last 5 rows by default

print('\n\n')

movies_data.info()      #info method of read_csv class returns information about movies_data. It already contains print function and return none value, i.e., no value, therefore print function needs not be used with this method

print('\n\n')

print(movies_data.describe())       #gives statistical description of movies data

print('\n\n')

print(movies_data.head(5).T)               #the T stands for transversal. it turns the columns into rows and rows into columns of the dataframe

print('\n\n')



'''___________________________Changing index column of data frame___________________________'''



movies_df=pd.read_csv(r'D:\tmdb_5000_movies.csv', index_col='original_title')       #this will set the original_title column as the index. in place of the name of the column the position (i.e, index) of the column can also be used

#NOTE- if an already defined dataframe with a user defined index is saved as a csv file and then the csv file is again imported as a dataframe, then the index column will itself be treated as another column of the dataframe created. in such case, the index_col comes in handy as it can be used to define the previous index as the index column of the new dataframe as well

print(movies_df)

print('\n\n')

print(movies_df.loc['Spectre'])     #this gives the information of the row at index 'Spectre' (i.e., the movie with name spectre)

print('\n\n')

print(movies_df.loc['Spectre', 'runtime'])          #loc method can also be used to give information of a certain column belonging to the row with given index (i.e., Spectre)

print('\n\n')

print(movies_df.reset_index())       #this will show the resetted form of data frame, i.e., it will show the data frame as it initially looked with its default index column.

print('\n\n')

#NOTE- the reset_index method does not affect the actual data frame (here, movies_df) but only shows its resetted form without actually resetting it

print(movies_df)        #this will give the data frame with original_title as index column

print('\n\n')

movies_df.reset_index(inplace=True)          # now, by setting inplace attribute to true, the reset_index method will actually reset the index of the given data frame
print(movies_df)

print('\n\n')

movies_df.set_index('original_title', inplace=True)      #set_index method will set the given column as the index of the given data frame and setting inplace attribute to true will apply the change to the original data frame
print(movies_df)

print('\n\n')

movies_df.reset_index(level=['original_title'], inplace=True)       #The level attribute of the reset_index function takes a column of the dataframe as input and makes it the seconf column in appearance after the default index
print(movies_df)

print('\n\n')

movies_df.set_index('original_title', inplace=True)

print('\n\n')

#the data type of index and columns is same

print(type(movies_df.index))

print('\n\n')

print(type(movies_df.columns))

print('\n\n')

print(movies_df.index[0])       #this will give the name of the 0th index in the given data frame

print('\n\n')

print(movies_df.columns[-2])     #this will give the name of the column at 2nd last position

print('\n\n')

print(movies_df.index[3:6])     #this will give a list containing the names of the 3rd, 4th and 5th indices (similar can be done with columns)

print('\n\n')

print(movies_df.index.get_loc('Spectre'))       #returns the position of the index named spectre

print('\n\n')

print(movies_df.index.is_unique)    #returns true if the every index is unique(i.e., no two movies have same name in this case), else, returns false

print('\n\n')





'''___________________________Selcting columns___________________________'''



print(movies_data['budget'])        #returns a panda series containing the contents of every row belonging to the given  colummn, i.e., budget

print('\n\n')

print(movies_data['budget'].unique())         #returns an array containing the data belonging to the 'budget' column of the dataframe uniquely, i.e., any value that appears in more than one rows will be in the list only once

print('\n\n')

print(pd.unique(movies_data['budget']))         #the above task can also be performed by using the unique method under pandas module directly and then passing the selected column from the datframe as a parameter under the unique function

print('\n\n')

print(movies_data['budget'].nunique(dropna=True))       #returns the number of unique values in the given column of the dataframe except null values if the dropna parameter is assigned True value to it

print('\n\n')

print(movies_data[['budget']])      #returns a panda data frame (by using two brackets) containing the contents of every row belonging to the given column, i.e., budget

print('\n\n')

print(movies_data[['budget','original_title']].head())       #returns first 5 rows of a data frame containing the contents of every row belonging to the given columns, i.e., budget and original title

print('\n\n')





'''_____________________________Selecting rows_____________________________'''




#single rows cannot be selected through indexing, so we use slicing for selection of rows

print(movies_data[0:1])     #this will give row at 0th position, i.e., 1st row, which will basically be a dataframe of 1 row

print('\n\n')

print(movies_data[2:5])     #this will give rows from 2nd to 4th positions, i.e., 3rd, 4th and 5th rows

print('\n\n')

data=movies_data[2:5]       #the object obtainined by applying slicing on a data frame, stored in variable "data" here, is a data frame itself. This implies that we can use all
print(type(data))           #operations of data frame over it, i.e., we can select columns from it and apply header method on it

print('\n\n')

#to select rows single rows using indexing, we use iloc method

print(movies_data.iloc[0])          #this will give row at 0th position, i.e., 1st row
print(type(movies_data.iloc[0]))        #indexing through iloc returns a panda series

print('\n\n')

print(movies_data.iloc[0:5])        #slicing can also be done using iloc method
print(type(movies_data.iloc[0:5]))      #and it will return a data frame

print('\n\n')

print(movies_data.iloc[[0,2,3]])        #to get info about certain rows, pass a list of the indices of the required rows

print('\n\n')

print(movies_data.loc[0:3])     #in loc method, unlike in iloc and other slicing, last element is also included, i.e., the element at 3rd index will also be printed 

print('\n\n')




#______________________________________________________________________________________________________________________________________________________________________________________





data=pd.read_csv(r'D:\tmdb_5000_movies.csv', index_col='original_title')        #index_col attribute sets given column, i.e., 'original_title' as index column
print(data)

print('\n\n')

print(data.loc['Avatar'])       #indexing through the index column

print('\n\n')

print(data.loc[['Avatar','Spectre']])       #to get info of certain movies, pass a list of the indices of the required movies

print('\n\n')

print(data.loc[['Avatar','Spectre'],['budget','original_language']])       #to print budget and language info of movies with indeics 'Avatar' and 'Spectre'

print('\n\n')

print(data.loc[['Avatar','Spectre'],['budget','original_language']])        #above witten code line can also ber written this way to produce same results (specific for loc)   

print('\n\n')




#_______________________________________________________________________________________________________________________________________________________________________________________






'''________________________________________Working with series______________________________________'''



ser=movies_data['runtime']         #<--------|
print(ser)                         #         |
                                   #         |  series can be created by any of the two syntaxes given
print('\n\n')                      #         |
                                   #         |
alt_ser=movies_data.runtime        #<--------|  
print(alt_ser)

print('\n\n')

print(ser.head(10))       #prints to 10 rows of the given data series. If no argument passed, gives top 5 rows. Same ways, tail method can also be used

print('\n\n')

print(ser.dtype)       #dtype attribute gives data type of the data in the series (basically, the data type of the data in a particular column of our data set)

print('\n\n')

#info method is only for data frame and can not be used with series

print(ser.describe())       #same as data frame

print('\n\n')

print(ser.shape)       #same as data frame

print('\n\n')

print(ser.size)       #same as data frame

print('\n\n')

print(ser.count())      #returns number of values in the given series that are defined and not null

print('\n\n')

print(ser.index)       #same as data frame
 
print('\n\n')



'''_______________________________Methods and Attributes specific to series (that cannot be used in data frame)_____________________________'''



print(ser.sum())        #returns sum of all values in the series (only if values are numbers)

print('\n\n')

print(ser.mean())        #returns mean of all values in the series (only if values are numbers)

print('\n\n')

print(ser.std())        #returns standard deviation of all values in the series (only if values are numbers)

print('\n\n')

print(ser.median())        #returns median of all values in the series (only if values are numbers)

print('\n\n')

print(ser.min())        #returns minimum among all values in the series (only if values are numbers) (same way max method also  works)

print('\n\n')

#NOTE- The above methods can also be used with a data frame if all the data in it is of numerical type

print(ser.unique())     #returns a numpy array containing all values (including none if appeared at least once) uniquely(i.e., each value will appear only once in the list even if it appears multuple times in the series)

print('\n\n')

print(len(ser.unique()))        #returns length of the array returned by unique method, i.e., counts the number of values in the series uniquely

print('\n\n')

print(ser.nunique())        #works same as len(ser.unique()) but it does not count none value whereas len(ser.unique()) counts none. Therefore it is one less than len(ser.unique())

print('\n\n')

print(ser.nunique(dropna=False))     #now it will also count none (uniquely)

print('\n\n')

#NOTE- nunique method can also be used with data frame

print(ser.value_counts())       #returns how many times each value has appeared in the series (by default, the values are arranged in descending order of their appearance count)

print('\n\n')

print(ser.value_counts(ascending=True, bins=3))     #works same as ser.value_counts() but instead of returning each value and its appearnace count, it returns as many intervals of values as the value of bins command and the appearance count of all values in given intervals

print('\n\n')

print(ser.to_frame())          #A sries can also be printed as a data frame using the to_frame() method, although it does not actually change the series to a data frame

print('\n\n')

print(type(ser))         #This shows that the data type of ser is still pandas series

print('\n\n')

print(ser[0])           #Elements of a series can be selected through indexing and slicing

print('\n\n')

print(ser[[0,2,4,6]])      #Unlike other arrays, multiple elements can be selected from a pandas series through indexing by passing a list of indices of the elements to be selected

print('\n\n')


'''___________________________Creating series from arrays (without any involvement of data frames)___________________________'''


anime=['My Hero Academia','One Punch Man','Death Note','Swords Art Online','Domestic Girlfriend','Yuri on ice','Doraemon']
genre=['shounen','shounen','Action Adventure','action','shounen/shojo','sports','kodomomuke']

ani_ser=pd.Series(anime, name='Anime',)      #series class of pandas creates a series based on anime list (any array can be used instead of list) name attribute assigns a name to it
print(ani_ser)

print('\n\n')

ani_ser2=pd.Series(genre, name='anime genre', index=anime)      #index attribues assigns the contents of given array (i.e., anime list) as index of ani_ser2 series
print(ani_ser2)

#NOTE-the array on bassis of which the series is being created (i.e., genre in the abpve case) and the array which is being assigned as the index (i.e., anime in the abpve case) must be of same length

print('\n\n')

dic={
    'My Hero Academia' : 'shounen',
    'One Punch Man' : 'Shounen',
    'Death Note' : 'Action Adventure',
    'Swords Art Online' : 'action',
    'Domestic Girlfriend' : 'shounen/shojo',
    'Yuri on ice' : 'sports',
    'Doraemon' : 'kodomomuke' 
    }

ani_ser3=pd.Series(dic, name='anime genre')     #this will create a series on the basis of dic dictionary with its keys assingned as indices of the series and its values as the values of the series
print(ani_ser3)

print('\n\n')

ani_ser4=pd.read_csv(r'D:\tmdb_5000_movies.csv', usecols=['runtime'], squeeze=True)     #setting squeeze attributes to true returns a series (otherwise a data frame would have been returned)

#NOTE- to create a series using the above method, only one column must be passed the the list assigned to usecols attribute

print('\n\n')

#creating own index and using it as index in series

defined_index=pd.Index(['A','B','C'])
print(type(defined_index))

print('\n\n')

print(defined_index.is_unique)      #this is to show that every function that can be performed on index of a data frame can also be performed on defined_index

print('\n\n')

ser3=pd.Series([1,2,3], index=defined_index, name='Sample series')        #this will create a series with name sample series and defined_index as its index
print(ser3)

print('\n\n')



'''________________________________Sorting of series_________________________________'''


num_dic={1:'one', 3:'three', 2:'two', 4:'four'}
dic_ser=pd.Series(num_dic, name='Series to sort')
print(dic_ser)

print('\n\n')

dic_ser.sort_index(ascending=False, inplace=True)       #sort_index method will sort the series on the  basis of index. By default, it will sort in ascending order, but if value of ascending parameter is set to false, then it sorts in descending order. Setting Inplace attribute to True ensures that sorting is applied to the series permanently. otherwise the sort_index method would just show the sorted series but not actually sort it
print(dic_ser)

print('\n\n')

dic_ser.sort_values(ascending=False, inplace=True)
print(dic_ser)

print('\n\n')

#NOTE- sorting methods sort any column (i.e., index or values) numerically, if they contain numbers, and alphabetically, if they contain strings



'''____________________________Conversion of a pandas series into a python array______________________________'''



print(dic_ser.tolist())         #returns a list containing the actual data (i.e., values) of the series
print(type(dic_ser.tolist()))

print('\n\n')

print(dic_ser.values)           #returns a numpy array containing the values of the series
print(type(dic_ser.values))

print('\n\n')



'''_______________________________Finding the smallest and largest values from a series (only for series containing numerical data)_________________________________'''


print(ser)

print('\n\n')

ser5=movies_data['original_title']
lst=ser5.tolist()

ser6=pd.Series(ser.tolist(), index=lst, name='runtime series')
print(ser6)

print('\n\n')

print(ser6.nsmallest(n=3))       #nsmallest method returns the smallest values in the series in ascending order. Setting the value of 'n' parameter to a number (i.e., here 3) returns that many (i.e., returns 3) smallest values. By defaul it is set to 5, so that enterin no value returns 5 smallest values

print('\n\n')

print(ser6.nsmallest().index[0])     #this returns the name of the index at 0th position (i.e., the value at 0th position of index column)

print('\n\n')

#In the same way there is nlargest method which works similar to nsmallest but prints largest values in descending order

#NOTE- the nsmallest and nlargest are also applicable on dataframe

print(movies_df.nsmallest(5,['runtime']))

print('\n\n')






'''_____________________________________Filtering Data________________________________________'''




suicide_data=pd.read_csv(r'D:\master.csv')
print(suicide_data)

print('\n\n')

suicide_series=suicide_data.country
print(suicide_series)

print('\n\n')

print(suicide_series.unique())
print(type(suicide_series.unique()))

print('\n\n')

suicide_data.set_index('country', inplace=True)
print(suicide_data.loc['Israel'])
print(type(suicide_data.loc['Israel']))                          #This shows that if a name has multiple entries in the index column, then the loc method returns a data frame containing the information of every entry of the name in the index

print('\n\n')

print(data.loc['Avatar'])
print(type(data.loc['Avatar']))                         #This shows that if a name has single entry in the index column, then the loc method returns a panda series containing the information of that entry of the name in the index

print('\n\n')

#Setting country column as the index of the data frame and then searching for a particular country is one way to filter the data of that country (Israel in this case) 
#Another way is given below.

#print(suicide_data.country=='Israel')          #The == sign will convert the given statement as a condition will then applied to every row of the 'suicide_data' data frame to check whether the data in the country column of that row is Israel
#print(type(suicide_data.country=='Israel'))         #The object obtained in return from the above command is a panda series

#print('\n\n')

#print(suicide_data[suicide_data.country=='Isreal'])      #This is the second way to get info about all the rows in which the country is Israel

#print('\n\n')

#mask=suicide_data.country=='Israel'
#print(suicide_data[mask, ['country', 'sex', 'year', suicides_no])     #Passing a list of columns while calling the data frame under certain given conditions (here, mask4) gives a data frame that contains only those columns which are in the list as a result

#print('\n\n')

#mask1=suicide_data.sex=='male'                           #By this way the boolean values of the given conditions can be applied to a variable
#mask2=suicide.year>=1991                                   and the variable can then be used as an attribute to print a data frame on which the given conditions apply 
#print(suicide_data[mask1 & mask2])

#print('\n\n')

#mask3=suicide.year.between(1989, 2000)                   #between attribute takes two arguments and finds the result that contains values between the two arguments including those two arguments
#print(suicide_data[mask3])

#print('\n\n')

#mask4=suicide_data.year.isin([2000, 2010])             #isin attributes gives the result that contains values only from the array that has been given in it as an argument
#print(suicide_data[mask4])

#print('\n\n')

#print(suicide_data[~mask4])                          #The ~ sign will give results that contain all the values except those in the array passed as an argument in the mask4 variable
#print(suicide_data[~mask4].unique())                #Therefore the numpy array obtained by the given command will contain all the years in the data frame ecxcept those in the mask4 variable(i.e., 2000 and 2010)








'''__________________________________________Creating Data Frame________________________________________________'''





# When data is arranged in columns

name=['Aarke', 'Rohit', 'Rahul']
work=['Coding', 'Plumbing', 'Hotel Management']
height=['165cm', '169cm', '169cm']

data_frame1=pd.DataFrame({'Name':name, 'Work':work, 'Height':height})        #When data is arranged in columns then a dictionary is passed as a parameter containing column names as keys and the data to be entered as values 
print(data_frame1)

print('\n\n')

print(data_frame1.T)

print('\n\n')

data_frame1.set_index('Name', inplace=True)
print(data_frame1)

print('\n\n')



# When data is arranged in rows

person1=['Aarke', 'Coding', '165cm']
person2=['Rohit', 'Plumbing', '169cm']
person3=['Rahul', 'Hotel Management', '169cm']

data_frame2=pd.DataFrame(data=[person1, person2, person3], columns=['Name', 'Work', 'Height'])         #When data is arranged in rows then two parameters are passed, one is the data parameter which contains the list of all the rows of data to be entered and the other is the column parameter which contains the list of the names of all the columns
print(data_frame2)
 
print('\n\n')

data_frame2.set_index('Name', inplace=True)
data_frame2.index.names=[None]                     #This will set the head name of index column as none, i.e., here, the column 'Name' is set as index column so its name will be displayed as the head name of the index colum, but setting the names attribute of index function to none will make the name of the index column dissapear
print(data_frame2)

print('\n\n')

hobby=['playing games', 'playing games', 'watching movies']
data_frame2['Hobby']=hobby                                                    #New data can be entered into a data frame by assigning it to a column of the data frame. If that column already exists in the data frame, then the data in the column is changed to the new data entered and if the column does not exist in the data frame, then a new column is created in the data frame with the same name and the new data is assigned to it
print(data_frame2)

print('\n\n')

#Column names and Indices of a dataframe can be renamed using various methods

data_frame2.reset_index(inplace=True)

data_frame2.columns=['Names', 'Work', 'Heights', 'Hobbies']        #columns attribute of the data frame takes a list of string values as input and assigns them as the name of the column of the data frame

data_frame2.index=['Person1','Person2','Person3']                  #index attribute of the data frame takes a list of string values as input and assigns them as the name of the index column of the data frame
print(data_frame2)

print('\n\n')

#The values attribute under the columns attribute of the data frame can also be used to rename the columns and indices of the dataframe by indexing and slicing

data_frame2.columns.values[2]='Height'

data_frame2.columns.values[:]=['Name', 'Work', 'Height', 'Hobby']           
print(data_frame2)

print('\n\n')

print(data_frame2.loc['Person1'])

print('\n\n')

data_frame2.reset_index(inplace=True)
print(data_frame2.index[0])

print('\n\n')

#Similarly series can also be created

series1=pd.Series(data= work)            #The data to be used to create the series is passed under the data parameter of the Series function of pandas
print(series1)

print('\n\n')






#___________________________________________________________________________________________________________________________________________________________________________________________







'''__________________________________About Time Series module of Pandas________________________________________'''





import datetime                       #importing python's own datetime module (which does not belong to pandas)


#In this module of Pandas, we can include the date and time for every record and can fetch the records of dataframe.
#We can find out the data within a certain range of date and time by using pandas module named Time series

#Objectives of time series analysis

# -> Create the series of date
# -> Work with data timestamp
# -> Convert string data to timestamp
# -> Slicing of data using timestamp
# -> Resample your time series for different time period aggregates/summary statistics
# -> Working with missing data




#Creating datetime data type

#the main method of creating a datetime is by using the pd.to_datetime() method. the datetime method of the pandas module takes a list of various items that can be converted to datetime format

a1=pd.to_datetime(['1/6/2020', '1-7-2020', datetime.datetime(2020, 1, 8), np.datetime64('2020-01-09')])         #this shows that can convert string format, datetime datatype and even numpy's datetime64 data into pandas dataframe and the default format of the pandas datetime is yyyy-mm-dd
print(a1)

#NOTE- any array and even dataframe can be passed in the pd.to_datetime() method given that their data is suitable for conversion th4o timestamp(date time format)

print('\n\n')

print(type(a1))                        #this shows that the data type of a1 is pandas date time index

print('\n\n')

print(type(a1[0]))                     #this shows that the data inside the date time index array a1 is of the data type timestamp 

print('\n\n')

#we can also define the format of the data entered in the list input in the datetime method to avoid any confusion.

a2=pd.to_datetime(['2020/14/6', '2020/15/06'], format='%Y/%d/%m')              #NOTE- the values entered in the format parameter is case sensitive, i.e., for mentioning month, only 'm' can be used and for mentioning minutes, only 'M' can be used
print(a2)

print('\n\n')

#similarly hours and minutes can also be added to the datetime object created by using format parameter

a3=pd.to_datetime(['2020/6/8 14.05', '2020/6/9 6.45'], format='%Y/%m/%d %H.%M')
print(a3)

print('\n\n')

#another way to create a datetime is by using the pd.date_range() method.

b1=pd.date_range('2019/1/1', '2019/1/9', freq='1d')                  #the date_range method of pandas takes a starting date value, an ending date value and a frequency, i.e. a gap of time , an creates a list of periods from the starting date to the ending date with time gap equal to the frequency entered
print(b1)                                                             #NOTE- the value entered in the freq parameter is case insensitive because it is different for every time period unit. eg, frequency for months in 'm' or 'M', whereas the frequency for minutes is 'min' or 'Min'. Also a number can be used before the units to define the gaps of more than a single unit

print('\n\n')

b2=pd.date_range('2020/6/1', periods=30, freq='d')                   #the data_range method can also be written in another syntax which contains a starting date, value of periods (i.e., the number of time periods in the resultant list), and the frequency as its input
print(b2)

print('\n\n')

#the datetime index array craeated by using the above method of pandas can be used as a column while creating a dataframe

import random

df1=pd.DataFrame({'Score':np.random.randint(10,100,30)}, index=b2)
print(df1)

print('\n\n')

print(df1['2020-06-12':'2020-06-18'])                #now, the dates can be used for indexing and slicing of the dataframe and so any data can now be fetched from the dataframe by the date assigned to it(eg., the date of its entry if the date assigned to it corresponds to the date of its entry)

#NOTE- while sliccing through datetimeindex, the last date of the slice is also included in the result, unlike other slicing
 
print('\n\n')

df1.to_csv(r'D:\file1.csv')
df2=pd.read_csv(r'D:\file1.csv', index_col=0)       #if the index column is not defined then the datetime index that was the inde column in th previous datafram will become just another ormal column in the new dataframe. the index_col prevents that from happening                   
print(df2)

print('\n\n')

print(type(df2.index[0]))                           #the dates in the new dataframe are imported from a csv file, where they were converted into string. so their data type need to be changed again into datetime index

print('\n\n')

df2.index=pd.to_datetime(df2.index, format='%Y-%m-%d')
print(type(df2.index[0]))

print('\n\n')

#converting a whole dataframe into datetime format by using the pd.to_datetime() method

yyyy=[random.randint(1995,2005) for i in range(100)]
mm=[random.randint(1,12) for j in range(100)]
dd=[random.randint(1,28) for k in range(100)]

df3=pd.DataFrame({'Year':yyyy,'Month':mm,'Day':dd})                 #NOTE- the names of the columns in the strings cannot be changed and must be specifially the same as in the given dataframe. for ex, the last column can not be named as date. because pandas datetime requires it to be named day for changing it to the day part of the timestamp
print(df3.head())

print('\n\n')

df3=pd.to_datetime(df3)                                             #the resultant dataframe contains only of one column which contains the timestamp data formed from the data in the prevous columns
print(df3.head())

print('\n\n')

#the to_datetime and date_range methods of pandas take an array of values and creates a datetime index consisting of multiple time stamps.
#single timestamps can also be created by giving only one value as data input by using the pd.Timestamp() method

ts=pd.Timestamp('02-6-2018')                       #NOTE- format parameter does not work in this method
print(ts)

#Timestamps alone is not very useful, until we create an index out of it. The index that we create using the Timestamps are of DatetimeIndex type.

print('\n\n')

df4 = pd.DataFrame({'City':['Lisbon', 'Parague', 'Macao', 'Venice'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})

index_ = [pd.Timestamp('01-06-2018'), pd.Timestamp('04-06-2018'), pd.Timestamp('07-06-2018'), pd.Timestamp('10-06-2018')]
print(type(index_))                 #this shoe=ws that index_ is a list of timestamps but not a datetime index which is to be expected and shows that datetime index and list of multiple timestamps are different things.

df4.index = index_
print(type(df4.index))              #this shows that although index_ was a list as expected, the data type of the index column of the formed dataframe is not a pandasindex bt unexpectedly a datetime index

print('\n\n')

print(df4)

print('\n\n')

#as timestamps are used to create certain point of time, similarly periods are used to create time periods within pandas . it could be a month, year, day, jhour, etc.

pr=pd.Period('2020-06')
print(pr)

print('\n\n')

#Period objects alone is not very useful until it is used as an Index in a Dataframe or a Series. An index made up of Periods are called PeriodIndex.

index2_ = [pd.Period('02-2018'), pd.Period('04-2018'), pd.Period('06-2018'), pd.Period('10-2018')]
df4.index=index2_
print(type(df4.index))                    #this shows that just like in the above case, index2_ is a normal python list but the index of the dataframe df4, after being assigned index2_, is Period Index datatype

print('\n\n')

print(df4)

print('\n\n')



t2=time.time()
print(t2-t1,' seconds')






