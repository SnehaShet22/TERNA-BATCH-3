thisdict = {
    'brand' : 'Ford' , 
    'model' : 'Mustang' , 
    'year' : '1964'
}

print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': '1964'}

print(thisdict['brand']) #Ford 

thisdict = {
    'brand' : 'Ford' , 
    'model' : 'Mustang' , 
    'year' : '1964' ,
    'Year' : 'Ford'
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': '2021'} 
#{'brand': 'Ford', 'model': 'Mustang', 'year': '1964', 'Year': 'Ford'}
#dictionary keys cannot have duplicates but values can 

print(len(thisdict)) # 4

thisdict = {
    'brand' : 'Ford' ,
    'electric': False ,
    'year' : 1964 ,
    'colours': ['red','white','blue']
}

print(type(thisdict)) #<class 'dict'> 

# ACCESSING DICTIONARY ITEMS 

thisdict = {
    'brand' : 'Ford' ,
    'electric': False ,
    'year' : 1964 ,
    'colours': ['red','white','blue']
}

print(thisdict['brand'])

#METHOD 2 : get() 

x = thisdict.get("brand")

print(thisdict.get("brand")) 


#GET KEYS 
x = thisdict.keys()
print(x)          #dict_keys(['brand', 'electric', 'year', 'colours'])


car ={
    'brand' : 'Ford' , 
    'model' : 'Mustang' , 
    'year' : '1964'
}
x = car.keys() 
print(x)  # before change  dict_keys(['brand', 'model', 'year'])
car['colour'] = 'white' # added new key 
print(x)  #dict_keys(['brand', 'model', 'year', 'colour']) 

y = car.values() 
print(y)           #dict_values(['Ford', 'Mustang', '1964', 'white'])
car['year'] = 2020 
print(y)           #dict_values(['Ford', 'Mustang', 2020, 'white'])



# GET VALUES 

y = thisdict.values() 
print(y)        #dict_values(['Ford', False, 1964, ['red', 'white', 'blue']]) 

# GET ITEMS 

z = thisdict.items() 
print(z)
#dict_items([('brand', 'Ford'), ('electric', False), ('year', 1964), ('colours', ['red', 'white', 'blue'])])



thisdict = {
    'brand' : 'Ford' , 
    'model' : 'Mustang' , 
    'year' : '1964' ,
}

if 'model' in thisdict:
    print('yes')   #yes 
else:
    print('no')

thisdict['year'] = 2018 
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}



# update()

thisdict.update({'year':2030}) 
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 2030}  


thisdict['color'] = 'red' 
thisdict.update({'colour':'white'}) 

print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2030, 'color': 'red', 'colour': 'white'} 


#REMOVING ELEMENTS 

#pop() 

thisdict.pop('colour') 
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2030, 'color': 'red'}


thisdict.popitem()
print(thisdict)   #{'brand': 'Ford', 'model': 'Mustang', 'year': 2030}  

del thisdict['brand'] 
print(thisdict)    #{'model': 'Mustang', 'year': 2030}

'''
del thisdict 
print(thisdict) #NameError: name 'thisdict' is not defined
''' 
#clear() 
thisdict.clear() 
print(thisdict)  # {} 



# set 
s = {1,2,3}
s.clear()
print(s)      #set()





thisdict = {
    'brand' : 'Ford' , 
    'model' : 'Mustang' , 
    'year' : '1964' ,
}

for i in thisdict:  # printing keys of dictionary
    print(i) 

for i in thisdict:  # printing values of dictionary
    print(thisdict[i])  


for i in thisdict.keys():  # printing keys of dictionary
    print(i) 

for i in thisdict.values():  # printing values of dictionary
    print(i) 

for i in thisdict.items():  # printing items of dictionary
    print(i) 

[('brand', 'Ford'), ('electric', False), ('year', 1964), ('colours', ['red', 'white', 'blue'])]

('brand', 'Ford')
('electric', False)
('year', 1964)
('colours', ['red', 'white', 'blue'])

# copy dictionary 
thisdict = {
    'brand' : 'Ford' , 
    'model' : 'Mustang' , 
    'year' : 1964 ,
}
mydict = thisdict   # both variables are pointing to same dictionaries
print(mydict) # before change

thisdict['color'] = 'white' 
print(mydict)  # after change 

mydict = thisdict.copy()
print(mydict)          

thisdict.popitem() 

print(mydict)


#dict() 
mydict = dict(thisdict)  # can copy the dictionary 

myfamily = {
    'child1': {
        'name':'Emily',
        'Year' : 2004
    },

    'child2' : {
        'name':'Tobias',
        'Year' : 2007
    } ,

    'child3' : {
        'name':'Linus',
        'Year' : 2011
    }


}

print(myfamily) 
#{'child1': {'name': 'Emily', 'Year': 2004}, 'child2': {'name': 'Tobias', 'Year': 2007}, 'child3': {'name': 'Linus', 'Year': 2011}}


c1= {
        'name':'Emily',
        'Year' : 2004
    }

c2 = {
    'name':'Tobias',
    'Year' : 2007
} 

c3 = {
    'name':'Linus',
    'Year' : 2011
}

myfamily = {
    'child1':c1,
    'child2':c2,
    'child3':c3,
} 



x = ('key1' , 'key2' , 'key3') 
y = 0 

thisdict = dict.fromkeys(x,y) 

print(thisdict)  #{'key1': 0, 'key2': 0, 'key3': 0}

x= ('Tanay','Kaushik','Faheem')
y = ('Student','student1','student2') 

terna = dict.fromkeys(x,y) 
print(terna) #{'Tanay': 'Student', 'Kaushik': 'Student', 'Faheem': 'Student'}
# {'Tanay': ('Student', 'student1', 'student2'), 'Kaushik': ('Student', 'student1', 'student2'), 'Faheem': ('Student', 'student1', 'student2')}


x= ('Tanay','Kaushik','Faheem') 

terna = dict.fromkeys(x) 
print(terna)

#{'Tanay': None, 'Kaushik': None, 'Faheem': None} 

# setdefault () 

car ={
    'brand' : 'Ford' , 
    'model' : 'Mustang' , 
    'year' : '1964'
} 

x = car.setdefault('Model','Bronco') 
print(x)   #Mustang


# IF ELSE 

a = 33 
b = 33 
if b > a :
    print(" b is greater than a") 
else:
    print('b is less than a')


a = 33 
b = 33 
if b > a :
    print(" b is greater than a") 

elif b==a :
    print('b is equal to a')

else:
    print('b is less than a')    

#b is equal to a

'''
a=0
if a:               # if this condition true 
    print()         #then execute this statement and ignore other elif /else conditions
elif a :
    print() 
elif a :
    print() 
elif a :
    print() 
else :
    print()
'''


# short-hand if only applicable if we have one single statement
a = 33 
b = 333 
if b > a :print("b is greater than a")  #b is greater than a

else:print('b is less than a')

a = 33 
b = 33

print('a')   if a < b else print('=')  if a==b else print('b') #a
                               # = 


# SET DEFAULT METHOD FROM DICTIONARIES 

car ={
    'brand' : 'Ford' , 
    'model' : 'Mustang' , 
    'year' : '1964'
} 

x = car.setdefault('colour','white') 
print(x)  # white

x = car.setdefault('year',2020) 
print(x)   #1964