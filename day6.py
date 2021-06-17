Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={'chennai':'csk','Bangalore':'rcb','punjab':'kxip','mumbai':'mi'}
>>> b={'rajastan':'rr'}
>>> c=a+b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c=a+b
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> c=a|b
>>> print(c)
{'chennai': 'csk', 'Bangalore': 'rcb', 'punjab': 'kxip', 'mumbai': 'mi', 'rajastan': 'rr'}
>>> d=merge(a,b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d=merge(a,b)
NameError: name 'merge' is not defined
>>> a=a.update(b)
>>> print(a)
None
>>> print(b)
{'rajastan': 'rr'}
>>> a={'chennai':'csk','Bangalore':'rcb','punjab':'kxip','mumbai':'mi'}
>>> b={'rajastan':'rr'}
>>> a.update(b)
>>> print(a)
{'chennai': 'csk', 'Bangalore': 'rcb', 'punjab': 'kxip', 'mumbai': 'mi', 'rajastan': 'rr'}
>>> del a['rajastan']
>>> print(a)
{'chennai': 'csk', 'Bangalore': 'rcb', 'punjab': 'kxip', 'mumbai': 'mi'}
>>> a=[0,1,2,3,4]
>>> b=['chennai','mumbai','delhi','calcutta','andhra']
>>> c={}
>>> for i in a:
	c[i]=b[i]

>>> print(c)
{0: 'chennai', 1: 'mumbai', 2: 'delhi', 3: 'calcutta', 4: 'andhra'}
>>> d=set(b)
>>> print(b)
['chennai', 'mumbai', 'delhi', 'calcutta', 'andhra']
>>> print(d)
{'mumbai', 'andhra', 'calcutta', 'delhi', 'chennai'}
>>> print(len(d))
5
>>> e={'delhi', 'chennai'}
>>> for i in e:
	remove d(i)
	
SyntaxError: invalid syntax
>>> for i in e:
	d.remove(i)

>>> print(d)
{'mumbai', 'andhra', 'calcutta'}
>>> 