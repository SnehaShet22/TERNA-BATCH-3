'''
a , b ='hello' ,  "hello"

print(a,b)

# multiline string 
a =""" hhggggggggggggggggk   gfc
hhhhhhhhhhhhhhhhhhhhhhhhhh
jjjjjjjjjjjjjjjjjj"""



#    0123456
a = 'Hello , World!'

print(a[1])
print(a[3])


for i in 'banana':
    print(i) 

# length of string 
a = 'Hello , World!'
print(len(a))

# python calculates blank spaces as well  

# strings are case sensitive

txt = 'the best things in life are free!'
if 'Free' in txt :
    print('present')
else:
    print('not present') 



txt = 'the best things in life are free!'

if 'Free' not in txt :
    print('not present')
else:
    print('present') 

# String Slicing 

a = 'Hello , World!'
print (a[2:5]) 

#0 1 2 3 45678 9 10 11 121314
#H e l l o , W o r  l d!

print (a[2:11]) 
print (a[:11]) # default starting index is 0 
print (a[2:]) # default ending index is len(string)
print (a[:]) # this prints the whole string 


# negative indexing 

a = 'Hello,World!' 
#'H  e   l l o , W o r l d !' 
#-12-11-10-9-8-7-6-5-4-3-2-1      
print(a[-6:-1]) 
print(a[:-7]) 

# when we go for range/slicing the last element is not inclisive

# Strings are IMMUTABLE (Unchangable)
# we cannot change the string but can modify them through built-in methods 

# 1.upper() = will return string in upper case 
a = 'Hello,World!' 
print(a.upper()) # HELLO,WORLD!

# 2.lower() = will return string in lower case 
a =  'HELLO,WORLD!'
print(a.lower()) #hello,world!

# 3. strip() = will remove white spaces from beging or end

a = '   Hello , World!   ' 
print(a)
print(a.strip())

a = '******Hello**,**World!********'
print(a)
print(a.strip('*')) # Hello**,**World!


# if we want to remove both spaces and stars we need to specify them both to strip function
a = '   Hello**,**World!********'
print(a)
print(a.strip('*')) # Hello**,**World!
print(a.strip()) 


# 3. split() 
a = 'Hello,World!' 
print (a.split(',')) # ['Hello', 'World!']

print (a.split('l')) #['He', '', 'o,Wor', 'd!']
#                      Hello,Wor d!


# String Concatenation

a = 'Satyam'
b = 'Sharma' 

print(a+' '+b) #Satyam Sharma

# cannot add string to integer
#1.convert integer to a string

a = 'Satyam'
b = 'Sharma' 
age = '20'
print(a +' '+ b +' '+ age ) #Satyam Sharma 20



# if we convert all string to integer
a = '118'
b = '112' 
age = 20
print(int(a) +int(b) + age ) #250

# if we convert all integer to string
a = '118'
b = '112' 
age = '20'
print(a +b + age ) #11811220


# use format method 
a = 'Satyam'
b = 'Sharma' 
age = 20
print ((a+' ' ,b),'{}'.format(age)) 

age = 36 
txt = 'my name is john , I am {} years old '.format(age)
print(txt)  #my name is john , I am 36 years old 

quantity = 3 
item_no = 567 
price = 49.5 
my_order = "I want to pay {} dollars for {} pieces of item {}.".format(price , quantity , item_no)
print(my_order)


quantity = 3 
item_no = 567 
price = 49.5                                                           #  0          1         2
my_order = "I want to pay {2} dollars for {0} pieces of item {1}.".format( quantity , item_no , price)
print(my_order) # I want to pay 49.5 dollars for 3 pieces of item 567.


# ESCAPE CHARACTERS 
txt = 'We are the so-called \'Vikings\' from the north.' 

# how to solve this ?
txt = "We are the so-called 'Vikings' from the north." 

txt = 'We are the so-called \'Vikings\' from the north.' 
print(txt)  #We are the so-called 'Vikings' from the north. 


txt = 'i am \n happy'
print(txt)#i am 
          #happy 

txt = 'i am \\happy'
print(txt)  # i am \happy

txt = 'i am \bhappy'
print(txt)  # i amhappy 


a = 5 
if a is 5 :
    print("that's right") 
else:
    print("no") 

a = 5 
if a is not 6 :
    print("no") 
else:
    print("that's right")  
'''

a = 11
b = 5
print(a/b) #2.2
print(a//b) # 2
   
