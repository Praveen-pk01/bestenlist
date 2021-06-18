def covid(l):
    a=str(input("Enter the Patient Name:"))
    b=int(input("Enter the temperature:"))
    c=a+'-'+str(b)
    l.append(c)
l=[]
while(1):
    covid(l)
    r=str(input("Do you want to continue(y/n):"))
    if(r=='n'):
        break
print("Patient Details:")
for i in l:
    print(i)
