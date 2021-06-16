Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[2,4,6,5,2,1,3]
>>> l.insert(3,9)
>>> print(l)
[2, 4, 6, 9, 5, 2, 1, 3]
>>> l.append(9)
>>> print(l)
[2, 4, 6, 9, 5, 2, 1, 3, 9]
>>> del l[2]
>>> print(l)
[2, 4, 9, 5, 2, 1, 3, 9]
>>> del l[3:5]
>>> print(l)
[2, 4, 9, 1, 3, 9]
>>> l.pop()
9
>>> print(l)
[2, 4, 9, 1, 3]
>>> l+[24,3,21,5,8,6,54,0,5,3]
[2, 4, 9, 1, 3, 24, 3, 21, 5, 8, 6, 54, 0, 5, 3]
>>> l=l+[24,3,21,5,8,6,54,0,5,3]
>>> print(l)
[2, 4, 9, 1, 3, 24, 3, 21, 5, 8, 6, 54, 0, 5, 3]
>>> a=min(l)
>>> b=max(l)
>>> print('min:',a,sep='','max:',b,sep='')
SyntaxError: positional argument follows keyword argument
>>> print('min of list:',min,sep='')
min of list:<built-in function min>
>>> print('min of list:',a,sep='')
min of list:0
>>> print('max of list:',b,sep='')
max of list:54
>>> a=('hello',1,'o','24',5)
>>> print(a)
('hello', 1, 'o', '24', 5)
>>> print(a[::-1])
(5, '24', 'o', 1, 'hello')
>>> b=list(a)
>>> print(b)
['hello', 1, 'o', '24', 5]
>>> 