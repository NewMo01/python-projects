from tkinter import *
from tkinter import ttk

# title of calculator
# design the shape
# using functions(show no , + and clear and =)

root=Tk()
s=ttk.Style()
s.theme_use('clam')
# title
root.title('simple calculator')

# using functions
def show(x):
    e.insert(END , x)

def remove():
    e.delete(0, END)


A=[]
def plus():
    global first
    first=float(e.get())
    A.append('+')
    remove()

def sub():
    global first
    first=float(e.get())
    A.append('-')
    remove()

def multy():
    global first
    first=float(e.get())
    A.append('*')
    remove()

def div():
    global first
    first = float(e.get())
    A.append('/')
    remove()


def equal():
    second=float(e.get())
    remove()
    if A[0]=='+':
        show(first+second)
        A.clear()
    elif A[0]=='-':
        show(first-second)
        A.clear()
    elif A[0]=='*':
        show(first * second)
        A.clear()
    elif A[0]=='/':
        show(first / second)
        A.clear()


# deisgn of the shape

e=ttk.Entry(root,width=20,font=50)
e.grid(row=0,column=0,columnspan=3,sticky='snew',padx=4,ipady=14)


b1=ttk.Button(root,text=7,command=lambda:show(7))
b2=ttk.Button(root,text=8,command=lambda:show(8))
b3=ttk.Button(root,text=9,command=lambda:show(9))
b4=ttk.Button(root,text=4,command=lambda:show(4))
b5=ttk.Button(root,text=5,command=lambda:show(5))
b6=ttk.Button(root,text=6,command=lambda:show(6))
b7=ttk.Button(root,text=1,command=lambda:show(1))
b8=ttk.Button(root,text=2,command=lambda:show(2))
b9=ttk.Button(root,text=3,command=lambda:show(3))
b10=ttk.Button(root,text=0,command=lambda:show(0))
b17=ttk.Button(root,text='.',command=lambda:show('.'))
b11=ttk.Button(root,text='clear',command=remove)
b12=ttk.Button(root,text='+',command=plus)
b13=ttk.Button(root,text='=',command=equal)
b14=ttk.Button(root,text='-',command=sub)
b15=ttk.Button(root,text='*',command=multy)
b16=ttk.Button(root,text='/',command=div)



b1.grid(row=1,column=0,sticky='snew',ipady=12)
b2.grid(row=1,column=1,sticky='snew',ipady=12)
b3.grid(row=1,column=2,sticky='snew',ipady=12)
b4.grid(row=2,column=0,sticky='snew',ipady=12)
b5.grid(row=2,column=1,sticky='snew',ipady=12)
b6.grid(row=2,column=2,sticky='snew',ipady=12)
b7.grid(row=3,column=0,sticky='snew',ipady=12)
b8.grid(row=3,column=1,sticky='snew',ipady=12)
b9.grid(row=3,column=2,sticky='snew',ipady=12)
b10.grid(row=4,column=0,sticky='snew',ipady=12)
b17.grid(row=5,column=1,sticky='snew',ipady=12)
b11.grid(row=5,column=2,sticky='snew',ipady=12)
b12.grid(row=4,column=2,sticky='snew',ipady=12)
b13.grid(row=6,column=1,columnspan=2,sticky='snew',ipady=12)
b14.grid(row=4,column=1,sticky='snew',ipady=12)
b15.grid(row=5,column=0,sticky='snew',ipady=12)
b16.grid(row=6,column=0,sticky='snew',ipady=12)


root.mainloop()
