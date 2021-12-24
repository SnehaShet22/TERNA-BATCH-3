# AND : TRUE only if all conditions true
# OR :  FALSE only if all conditions false 

'''
a = 200
b = 33
c = 500
#    true     true
if a > b and c > a :
    print("THAT'S RIGHT") 
else:
    print('NO') 


a = 200
b = 33
c = 500
#   
if a > b or a > c :
    print("THAT'S RIGHT")
    print('hii')
else:
    print('NO') 


# NESTED IF 

x = 41 

if x > 10 :
    print('Above ten ,')

    if x > 20 :
        print("and also above 20!")
    else:
        print('but not above 20!') 
else:
    print('not above 10')


a = 33 
b = 200 

if b > a :
    pass 


# take input from user
# if that number is divisible by 3 print FIZZ
# if that number is divisible by 5 print BUZZ
# if that number is divisible by 3 and 5 print FIZZBUZZ 
# if not divisible print that number


a = int(input("Enter the number: "))

if (a%3==0 and a%5==0):
    print("FIZZBUZZ")
elif(a%5==0):
    print("BUZZ")
elif(a%3==0):
    print('FIZZ')
else:
    print(a)


# WHILE LOOP 

i = 1 
while i < 6:  
    print(i)  # 1 2 3 4 5 
    i += 1 


# BREAK 
# CONTINUE 


i = 1 
while i < 6:     
    print(i)    # 1 2 3
    if i == 3 :
        break #out of the loop
    i +=1 

i = 1 
while i < 11:     
    print(1)    
    i +=1 



i = 0 
while i < 6:    
    i +=1          # 1 2 3 4 5 6 
    if i == 3 :
        continue   # restart our loop
    print(i)       # 1 2 4 5 6 



i = 1 
while i<6:
    print (i) 
    i+=1 
else :
    print('i is no longer less than 6') 



fruits = ['apple','kiwi','grapes','raspberry']

for i in fruits:
    print(i)


for i in 'fruits':              # f r u i t s 
    print(i)


fruits = ['apple','kiwi','grapes','raspberry']

for i in fruits:
    print(i)
    if i == 'grapes':
        break 


fruits = ['apple','kiwi','grapes','raspberry']
for i in fruits:
    if i == 'grapes':
        continue
    print(i) 



for i in range(6) :  # for i in range (0 , 6 ): 
    print(i)         # 1 2 3 4 5 


for i in range(2 , 6) :  # for i in range (2 , 6 ): 
    print(i)             #  2 3 4 5 


for i in range(0 , 10 , 2 ) :  # for i in range (start , end , increment )
    print(i) 

# 0 2 4 6 8  


for i in range(6):
    print(i)                        # 0 p 1 p 2 p 3 
    if i == 3 :
        break 
    else:
        print('finally finished')    



for i in range (10):
    if i<=4:
        print(i)            # 1 2 3 4 
    else :
        print ("number is greater than 4")
        break
        

for i in range(6):  
    if i == 3 :         # 0 1 2 3
        break 
    print(i)             # 0 1 2
else:
    print('finally finished')   


# NESTED FOR LOOP 
adjective = ['red','yellow','green'] 
fruits = ['apple','banana','kiwi']

for i in adjective:       # red                      yellow 
    for j in fruits:      # apple  banana  kiwi
        print(i , j)      # ra   rb      rk 

''' 

# write a program which iterates from 1 to 50 .
# if that number is divisible by 3 print FIZZ
# if that number is divisible by 5 print BUZZ
# if that number is divisible by 3 and 5 print FIZZBUZZ 
# if not divisible print that number

for a in range(1,51):         # 1 , 2 , 3 ,,,, 50
    if(a%3==0 and a%5==0):
        print('FIZZBUZZ')
    elif(a%5==0):
        print("BUZZ")
    elif(a%3==0):
        print("FIZZ")
    else:
        print(a)


'''
1
2
FIZZ
4
BUZZ
FIZZ
7
8
FIZZ
BUZZ
11
FIZZ
13
14
FIZZBUZZ
16
''' 

# CALCULATE  SUM OF ALL THE NUMBERS FROM 1 TO N 
# TAKE INPUT FROM USER 