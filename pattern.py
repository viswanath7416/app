'''x=input()
if x==''.join(reversed(x)):
    print("this is a palindrom")
else:
    print("this is not a palindrom")'''

'''def factors(num):
 fact=[]
 for i in range(1,num+1):
    if num%i==0:
        fact.append(i)
    return fact


c=factors(100)
print(c)'''
'''num=int(input())
for i in range(num+1):   #this is for right arrow space
    for j in range(i+1):
       print(i,end="")
    print('')
for i in range(num):
    for j in range(i,num):
        print(i,end="")
    print('') '''#HERE IT END
'''for i in range(1,num+1):
    for j in range(0,num-i):
        print("",'*',end="")
    print("")'''
'''for i in range(1,num+1):
    print(" ","*")
    for j in range(1,i-1):
        print('*',end="")
    print(' ')'''
'''for i in range(num):
    for j in range(i,num):
        print(" ",end="")
    for j in range(i+1):
       print("num",end=" ")   #this 
    print(' ')'''
     
'''for i in range(num-1):
    for j in range(i,num):
        print(" ",end="")
    for j in range(i+1):     #FOR REVERSE
        print("*",end="")
    print('')
for i in range(num):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,num):
        print("*",end="")
    print("")'''
"""for i in range(num-1):
    for j in range(i,num):
        print(" ",end="")
    for i in range(i+1):
        print("*",end=" ")
    print("")             #for space between star
for i in range(num):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,num):
        print("*",end=" ")
    print("")"""
'''for i in range(num):
    for j in range(i,num):
        print(" ",end="")
    for j in range((2*i)-1):
        print("*",end="")
    print("")'''
'''for i in range(num):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,(2*num)-1):
        print("*",end=" ")
    print("")'''
    
    
    
x=int(input("enter x value "))
'''y=int(input("enter y value "))
z=int(input("enter z value "))
if (x>y)and (x>z):
    print("x is greater")
elif (y>x)&(y>z):
    print("y is greater")
else:
    print("z is greater")'''
def multiplication(*x):
    m=1
    for i in range(1,*x):
        i=m*i
    print(i)x