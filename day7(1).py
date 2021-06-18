def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
a,b=map(int,input("Enter the two numbers: ").split())
print("Addition of",a,"and",b,'=',add(a,b))
print("Subtraction of",b,"from",a,'=',sub(a,b))
print("Multiplication of",a,"and",b,'=',mul(a,b))
print("Division of",a,"by",b,'=',div(a,b))
