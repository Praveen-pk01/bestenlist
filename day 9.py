Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #program to add 2 to every element of list
>>> a=[1 ,2,15,21,4,7,68,3,9]
>>> for i in range(0,len(a)):
	a[i]=a[i]+2

>>> print(a)
[3, 4, 17, 23, 6, 9, 70, 5, 11]
>>> #program to print pattern
>>> for i in range(5,0,-1):
    c=i
    for j in range(0,i):
        print(c,end='')
        c-=1
    print()

    
54321
4321
321
21
1
>>> #program to print fibanocci sequence
>>> l=[]
>>> l.append(1)
>>> l.append(1)
>>> for i in range(0,15):
    a,b=b,a+b
    l.append(b)

    
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    a,b=b,a+b
NameError: name 'b' is not defined
>>> l=[]
>>> l.append(1)
>>> l.append(1)
>>> a,b=l[0],l[1]
>>> for i in range(0,15):
    a,b=b,a+b
    l.append(b)

    
>>> print(l)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
>>> #Armstrong Number
'''
	Armstrong number is the one, which the sum of the power of the number
	to the count of the number is equal to the actual number
	(eg): 153=1^3+5^3+3^3=153
	      1=1^1=1
'''
'\n\tArmstrong number is the one, which the sum of the power of the number\n\tto the count of the number is equal to the actual number\n\t(eg): 153=1^3+5^3+3^3=153\n\t      1=1^1=1\n'
>>> def armstrong(n):
	a=n
	c=0
	while(a):
		a=a//10
		c+=1
	a=n
	sum=0
	while(a):
		r=a%10
		m=1
		for i in range(0,c):
		    m=m*r
		sum+=m
		a=a//10
	if(sum==n):
	    print("Armstrong Number")
	else:
	    print("Not a Armstrong Number")
armstrong(153)
SyntaxError: invalid syntax
>>> def armstrong(n):
	a=n
	c=0
	while(a):
		a=a//10
		c+=1
	a=n
	sum=0
	while(a):
		r=a%10
		m=1
		for i in range(0,c):
		    m=m*r
		sum+=m
		a=a//10
	if(sum==n):
	    print("Armstrong Number")
	else:
	    print("Not a Armstrong Number")

>>> armstrong(153)
Armstrong Number
>>> armstrong(10)
Not a Armstrong Number
>>> #program to print table of 9
>>> for i in range(1,16):
	print('9*',i,'=',9*i,sep='')

9*1=9
9*2=18
9*3=27
9*4=36
9*5=45
9*6=54
9*7=63
9*8=72
9*9=81
9*10=90
9*11=99
9*12=108
9*13=117
9*14=126
9*15=135
>>> #Program to check the number is positive or negative
>>> def check(n):
	if(n<0):
		print("Negative")
	elif(n>0):
		print("Positive")
	else:
		print("Zero")

>>> check(53)
Positive
>>> check(-53)
Negative
>>> check(0)
Zero
>>> #Program to convert days to ages
>>> def age(n):
	if(n//365):
		print(n//365,'Year',end=' ')
	if(n%365):
		print(n%365,'days',end=' ')

>>> age(5326)
14 Year 216 days 
>>> age(365)
1 Year 
>>> def arithmetic(a,b,s):
	if(s=='+'):
		return a+b
	if(s=='-')
	
SyntaxError: invalid syntax
>>> #Basic calculator
>>> def arithmetic(a,b,s):
	if(s=='+'):
		return a+b
	if(s=='-'):
		return a-b
	if(s=='*'):
		return a*b
	if(s=='/'):
		return a/b

>>> arithmetic(2,6,'+')
8
>>> arithmetic(86,54,'-')
32
>>> arithmetic(12,2,'*')
24
>>> arithmetic(12,2,'/')
6.0
>>> 