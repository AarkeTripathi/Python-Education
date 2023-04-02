#STRING FORMATTING

#sometimes, we have to print a statement that  require the values of various variables in the midst of strings.
#the general method of doing this is given below.

name='Harshit'
age=24

print('Hello '+name+' your age is '+str(age), end='\n\n')

#the above syntax is ugly and complex. To make it simple, we use string formatting.
#there are two types of string formatting.

#1- formatting of v3 or above
print('Hello {} your age is {}'.format(name,age))            #the curly braces are called placeholders and the data input in the format parameter is assigned to the placeholders in order

#2- formatting of v3.6 or above
print('hello {name} your age is {age+2}')                    #in this way of formatting, the variables are placed directly in the placeholders and even some valid operations can be performed as well
#this wont work here





#STRING METHODS

#1- len() method                                            this gives the ;ength, ie, the number of characters in the string

#2- lower() method                                          this method conerts all the alphabetical characters in the string into lowercase

#3- upper() method                                          this method conerts all the alphabetical characters in the string into lowercase

#4- title() method                                          this method converts the first alphabetical charancter of every word in a string into uppercase and the rest in lowercase

#5- count() method                                          this method gives the occurence count of every character appered in a string





#strip() method
#the strip method and itws variants, if not given any parameter, remove the spaces in the beginning and ending of a string

print('      Hello world      ')
print('      Hello World      '.strip())          #similarly, lstrip will only remove the spaces in beginning and rstrip will remove it from the ending

#if the space in between the string is to be removed, then strip method is useless, the space can be replaced with no space using the replace method

name='     Har     shit       ...'
print(name.replace(' ',''))                 #the replace method does not makes real changes to the original data and just shows modified data like strip method
#the number of times that a character has to be replaced can also be defined as third argument in the replace function
print('\n\n')
#CENTER METHOD

#the center method adds characters at the beginning and the end of the string
name='Harshit'
print(name.center(11,'*'))            #in the center method two arguments are to be passed, one is the length of the final string obtained after modification and the second is the character that has to be inserted
#if the legth of final string is given such that symmetry canot be established, then the extra character will be added to the right, i.e., at the end
print(name.center(12,'*'))
print('\n')

a,b,c=input('PLease enter the three numbers:').split(',')
a,b,c=int(a),int(b),int(c)
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
