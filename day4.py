Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=b=c=10
>>> a=a/10
>>> b=b*50
>>> c=c+60
>>> print(a,b,c)
1.0 500 70
>>> e="GOLEM"
>>> e[2]='G'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    e[2]='G'
TypeError: 'str' object does not support item assignment
>>> e.replace('L','G')
'GOGEM'
>>> e.replace(e[2],'L')
'GOLEM'
>>> a=5
>>> b=2.34
>>> a=int(a)
>>> a=float(a)
>>> print(a)
5.0
>>> b=int(b)
>>> print(b)
2
>>> 