from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Employee Details")
window.geometry('500x400')
window.configure(background = "black");
Employee_Name = Label(window ,text = "Employee Name").grid(row = 0,column = 3)
Employee_Id = Label(window ,text = "Employee Id").grid(row = 0,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 3,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 2,column = 0)
Age = Label(window ,text = "Age").grid(row = 4,column = 3)
Gender = Label(window ,text = "Gender").grid(row = 4,column = 0)
Branch = Label(window ,text = "Branch").grid(row = 5,column = 0)
Shift = Label(window ,text = "Shift").grid(row = 5,column = 3)
Language = Label(window ,text = "Language").grid(row = 6,column = 0)
Specialised = Label(window ,text = "Specialised on").grid(row = 7,column = 0)
Employee_Name1 = Entry(window).grid(row = 0,column = 4)
Employee_Id1 = Entry(window).grid(row = 0,column = 1)
Email1 = Entry(window).grid(row = 3,column = 1)
Mobile1 = Entry(window).grid(row = 2,column = 1)
Age1 = Entry(window).grid(row = 4,column = 4)
Gender1 = Entry(window).grid(row = 4,column = 1)
Branch1 = Entry(window).grid(row = 5,column = 1)
Shift1 = Entry(window).grid(row = 5,column = 4)
Language1 = Entry(window).grid(row = 6,column = 1)
Specialised1 = Entry(window).grid(row = 7,column = 1)

#function declaration
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=9,column=0)
window.mainloop()
