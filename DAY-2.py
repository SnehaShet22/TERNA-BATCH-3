'''
list = [0 , 1 ]
tuples = (0 , 1)
sets = {1 ,3} no indexing
'''

'''
# SETS ARE UNORDERED
li = ['apple' , 'banana' , 'mango']

s = {'apple' , 'banana' , 'mango' , 'kiwi' , 'blueberry' , 'papaya'}
# {'blueberry', 'banana', 'apple', 'kiwi', 'mango', 'papaya'}
print('list',li)
print('set',s)

# ALLOWS NO DUPLICATES

s = {'apple' , 'banana' , 'mango' , 'kiwi' , 'blueberry' , 'papaya', 'apple' , 'apple'}
print(s)    # {'kiwi', 'mango', 'apple', 'banana', 'blueberry', 'papaya'}

print(len(s))   # 6

s = {1 , 1.2 , True , 'strings'}   # set can contain different datatype 

print(type(s)) # <class 'set'> 

# set () 

thisset =   set (('apple' , 'banana' , 'mango')) 
print(type(thisset))  # <class 'set'>  


# TYPE CASTING 
thistuple = ('apple' , 'banana' , 'mango') 
# for converting from tuple to list  list()

thistuple = list( ('apple' , 'banana' , 'mango') )
print(type(thistuple))  # <class 'list'> 

# for converting from list to tuple tuple() 
list1 = ['apple' , 'banana' , 'mango']

list1 = tuple(['apple' , 'banana' , 'mango'])
print(type(list1))  # <class 'tuple'> 


# ACCESSING ITEMS OF A SET 

thisset= {'apple' , 'banana' , 'mango' , 'kiwi' , 'blueberry' , 'papaya'}

for x in thisset:
    print(x) 

print ('banana' in thisset)  # True  



# WE CANNOT CHANGE ITEMS , WE CAN ADD OR REMOVE ITEMS FROM A SET 

#add() = adding single element

s = {'apple' , 'banana' , 'mango' } 
s.add('orange')  
print(s)   # {'banana', 'orange', 'apple', 'mango'} 


# update() = to add another set 
s = {'apple' , 'banana' , 'mango' } 
s1 = {'papaya' , 'blueberry' , 'mango' } 

s.update(s1)
print(s)     #{'papaya', 'blueberry', 'mango', 'banana', 'apple'}
print(s1)    # {'mango', 'papaya', 'blueberry'} 



# REVE SET ITEMS 

#remove()
#discard() 

s = {'apple' , 'banana' , 'mango' } 
s.remove('apple') 
print(s)    #{'banana', 'mango'} 

#s.remove('blueberry')  # it will raise an error KeyError: 'blueberry' 

s = {'apple' , 'banana' , 'mango' } 
s.discard('blueberry')  # will not raise error will return same set  
s.discard('banana') #{'apple', 'mango'}  
print(s)

# pop () to remove last element from set 
s = {'apple' , 'banana' , 'mango' } 
x = s.pop()
print(x) #banana
print(s) # {'mango', 'apple'} 

# clear () : empties the set 
s.clear()   # set()  empty set 
print(s)

# del 
s = {'apple' , 'banana' , 'mango' } 
del s 
#print(s)  # NameError: name 's' is not defined. 

# joining 2 sets 
# 1. update 
# 2. union 

#1.
s = {'apple' , 'banana' , 'mango' } 
s1 = {'papaya' , 'blueberry' , 'mango' } 

s.update(s1)
print(s)     #{'papaya', 'blueberry', 'mango', 'banana', 'apple'}  changed
print(s1)    # {'mango', 'papaya', 'blueberry'}    no changes
 

#2.
set1 = {'1','2','3'} 
set2 = {'a','b','c'} 

set3 = set1.union(set2) 
print(set3)  #{'1', 'b', '3', 'c', '2', 'a'} 

print(set1) # {'1','2','3'}  no changes
print(set2) # {'a','b','c'}   no changes


# keep ONLY  the duplicates 

x = {'apple' , 'banana' , 'blueberry'} 
y = {'google','microsoft','apple'} 

x.intersection_update(y)  

print(x)  # {'apple'}
print(y)  # {'microsoft', 'apple', 'google'}


x = {'apple' , 'banana' , 'blueberry'} 
y = {'google','microsoft','apple'} 

z = x.intersection(y)  

print(x)   #{'banana', 'blueberry', 'apple'}
print(y)   #{'google', 'apple', 'microsoft'}
print(z)   #{'apple'} 


# Keep ALL , but NOT the duplicates 

x = {'apple' , 'banana' , 'blueberry'} 
y = {'google','microsoft','apple'} 

x.symmetric_difference_update(y)

print(x)  #{'banana', 'blueberry', 'microsoft', 'google'}
print(y)  #{'google', 'microsoft', 'apple'}

x = {'apple' , 'banana' , 'blueberry'} 
y = {'google','microsoft','apple'} 

z =x.symmetric_difference(y)

print(x)  #no change
print(y)  # no change
print(z)  # new set {'banana', 'blueberry', 'microsoft', 'google'}


# copy () 

x = {'apple' , 'banana' , 'blueberry'} 
y = x.copy ()   # y became a new object

print(x) # {'apple' , 'banana' , 'blueberry'} 
print(y) # {'apple' , 'banana' , 'blueberry'} 

x.discard('banana')

print(x) #{'blueberry', 'apple'}
print(y) #{'blueberry', 'apple', 'banana'}


x = {'apple' , 'banana' , 'blueberry'} 
y = x   # both y and x are pointing towards same set 

print(x) # {'apple' , 'banana' , 'blueberry'} 
print(y) # {'apple' , 'banana' , 'blueberry'} 

x.discard('banana')

print(x) #{'apple', 'blueberry'}
print(y) #{'apple', 'blueberry'}

# isdisjoint ()
# isdisjoint() method returns true if none of the items are present in both sets , otherwise returns false

x = {'apple' , 'banana' , 'blueberry'} 
y = {'google','microsoft','apple'}  

z = x.isdisjoint(y) 
print(z)    #False


# issubset() 
# issubset() this method returns true if all items in the set exists in specified set , otherwise it will return false
x = {'a','b','c'} 
y = {'f' , 'e' ,'d' , 'c' , 'b' , 'a'} 

z = x.issubset(y)   # if x present in y
print(z)  # true


z = y.issubset(x)  # false 

# issuperset() 
# method returns true if all items in specified set exists in original set , otherwise returns false

x = {'f' , 'e' ,'d' , 'c' , 'b' , 'a'} 
y = {'a','b','c'} 

print(x.issuperset(y)) #True  # if y present in x
'''

# list exercises 
#           0   1       2
my_test = [100,200 ,[10 ,20]]   
            #  0   1
my_test[2]  #[10 ,20]

my_test[2][1]  


#           0   1       2
my_test = [100,200 ,[10 ,20]]   # access 20
#              0    1
my_test[2]  # [10 ,20]

print(my_test[2][1]) 

nested_list =[100 ,200 , 300 , 400 , 500 , 600 , 700, [100 , 5 , 6 ,5 , 4, ['a', 'b' ,'c']]]

# i want to access 'b'
# access 6 
#solution 
# 0    1     2      3    4     5     6                  7
[100 ,200 , 300 , 400 , 500 , 600 , 700, [100 , 5 , 6 ,5 , 4, ['a', 'b' ,'c']]]    # 7 
# 0    1   2  3   4        5
[100 , 5 , 6 ,5 , 4, ['a', 'b' ,'c']]                                              # 5
# 0    1    2 
['a', 'b' ,'c']                                                                    # 1 

print(nested_list[7][5][1] ) #b 

print(nested_list[-1][-1][-2]) # b 

print(nested_list[7][2] )  # 6

print(nested_list[-1][-4] ) # 6
