Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hour challenge")
30 days 30 hour challenge
>>> print('30 days 30 hour challenge')
30 days 30 hour challenge
>>> print('''30 days 30 hour challenge''')
30 days 30 hour challenge
>>> Hours = "thirty"
>>> print(Hours)
thirty
>>> Days = "Thirty days"
>>> print(Days[3])
r
>>> Challenge = "I will win"
>>> print(Challenge[2:7])
will 
>>> print(len(Challenge))
10
>>> print(Challenge.lower())
i will win
>>> a = "30 Days"
>>> b = "30 hours"
>>> c = a + b
>>> print(c)
30 Days30 hours
>>> c=a+' '+b
>>> print(c)
30 Days 30 hours
>>> text = "Thirty days and Thirty hours"
>>> x = text.casefold()
>>> print(x)
thirty days and thirty hours
>>> text="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
>>> x=text.casefold()
>>> print(x)
don’t trouble trouble until trouble troubles you
>>> y=x.capitalize()
>>> print(y)
Don’t trouble trouble until trouble troubles you
>>> f=x.find(trouble)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    f=x.find(trouble)
NameError: name 'trouble' is not defined
pri
>>> f=x.find(t)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    f=x.find(t)
NameError: name 't' is not defined
>>> f=x.find("trouble")
>>> print(f)
6
>>> print('1') if (x.isalpha()) else print('0')
0
>>> a=text.isalnum()
>>> print(a)
False
>>> b=text.isalnum('A')
Traceback (most recent call last):

  File "<pyshell#32>", line 1, in <module>
    b=text.isalnum('A')
TypeError: str.isalnum() takes no arguments (1 given)
>>> a='A'
>>> b=a.isalnum()
>>> print(b)
True
>>> b=a.isalpha()
>>> print(b)
True
>>> 