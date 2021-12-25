'''
n = int(input('enteranumber'))
sum = 0 
for num in range(1 , n+1):   #num = 5
    sum = sum + num         # 0 + 1 + 2 + 3 + 4 + 5 =15

print("Sum is :",sum) 

# input from user 
# Sum of odd natural numbers till n
# Sum of even natural numbers till n 

n = int (input('Enter a number:'))  # 6 
sodd = 0 
seven = 0        
for num in range(1,n+1):          # 0 1 2 3 4 5 6 
    if num % 2 == 0 :         
        seven = seven + num     #   2 + 4 + 6 = 12

    else:
        sodd = sodd + num       # + 1 + 3 + 5  = 9    
print('Sum of even numbers:',seven)
print('Sum of odd numbers:',sodd)

n = int(input('ENTER')) 
print('Sum of 1ST even :',n*(n+1))   # 2 + 4 + 6 
print('Sum of 1ST odd :',n**2)       # 1 + 3 + 5...

#####

# & and 

a = 14 #1110
b = 4  #0100

print (b and a)   # true true   14
print(b & a)      #0100   4                   2**3 2**2  2**1 2**0 
                                             #  8   4     2     1 
                                             #  1    1     1     0
                                             #   0    1    0      0
a = 9 # 1001
b = 10 #1010 
#       9    10
print (a and b)   # 10
print(a & b)      #1000  8 


\'''
Sum of even numbers: 12
Sum of odd numbers: 9
ENTER3
Sum of 1ST even : 12
Sum of 1ST odd : 9
\'''


n = int(input('ENTER'))              # n = 4 
print('Sum of 1ST even :',n*(n+1))   # 2 + 4 + 6 + 8 
print('Sum of 1ST odd :',n**2)       # 1 + 3 + 5 + 7



n = int(input('enter a number'))  # 3
odd = 0  # sum of odd numbers
temp = 1 
for i in range (1 , n+1): # 1 2 3  
    odd = odd + temp       #  1 + 3 + 5 = 9
    temp = temp + 2        #  7 

print(odd) 


n = int(input('enter a number'))  # 3
even = 0  # sum of even numbers
temp = 2 
for i in range (1 , n+1): # 1  2  3
    even = even + temp     #  2 + 4 + 6  = 12
    temp = temp + 2        #  8

print(even) 


# Write a program to print multiplication table 
# take input from user 

# 2 * 1 = 2
# 2 * 2 = 4

n = int (input('enter a number')) 
for i in range (1 , 11):
    print(n, 'x' , i , '=' , n*i) 


n = int(input("enter a number to get table of it:"))

for k in range (1, 11):
    multi = k * n
    print(n,"*", k, "=",multi)

# factorial of number 
# 6 = 1 * 2 * 3 * 4 * 5 * 6 = 720

n = int(input())          # 6
fact = 1 
for i in range(1 , n+1 ): # 1 2 3 4 5 6
    fact = fact * i        # 1 * 1 * 2 * 3*4*5*6 =720
print(fact)

'''

# count number of digits in a number 
# input from user
# ex : 123456 = 6
# ex : 64949 = 5 





