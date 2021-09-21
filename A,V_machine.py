import math
from tkinter import *
from tkinter import ttk
root=Tk()
# Title
root.title('Good machine')
s=ttk.Style()
s.theme_use('clam')
s.configure('TEntry',foreground='blue')
mode='nothing'
# The functions to do operations
def show_from_0(n):
    e.delete(0, END)
    e.insert(0, n)
def remove():
    e.delete(0,END)
def get_dimansions():
    global height,width,base,radius,dim,mode,kind,length,shape
    if dim=='h':
        if shape=='para_rect':
            e.delete(0,8)
            length=float(e.get())
            show_from_0('Height: ')
            mode = 'math'
            kind = 'para_rect'
            b24 = ttk.Button(root, text='=', command=equal)
            b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
        elif shape=='triangle':
            e.delete(0,6)
            base=float(e.get())
            show_from_0('Height: ')
            mode = 'math'
            kind = 'triangle_Area'
            b24 = ttk.Button(root, text='=', command=equal)
            b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
        elif shape=='cylinder' or shape=='cone':
            show_from_0('Height: ')
            dim='r'
            if shape=='cylinder':
                shape='cylinder'
            elif shape=='cone':
                shape = 'cone'
            b24 = ttk.Button(root, text='=', command=get_dimansions)
            b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
    elif dim=='w':
        show_from_0('Width: ')
        dim='L'
        b24 = ttk.Button(root, text='=', command=get_dimansions)
        b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
    elif dim=='b':
        show_from_0('Base: ')
        dim='h'
        shape='triangle'
        b24 = ttk.Button(root, text='=', command=get_dimansions)
        b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)

    elif dim=='r':
        if shape == 'circle' or shape == 'Ball':
            show_from_0('Radius: ')
            mode='math'
            if shape=='circle':
                kind='circle_Area'
            elif shape=='Ball':
                kind='Ball'
            b24 = ttk.Button(root, text='=', command=equal)
            b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
        else:
            e.delete(0, 8)
            height = float(e.get())
            show_from_0('Radius: ')
            mode = 'math'
            if shape=='cone':
                kind = 'cone'
            elif shape=='cylinder':
                kind = 'cylinder'
            b24 = ttk.Button(root, text='=', command=equal)
            b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
    elif dim=='L':
        if shape == 'rect':
            e.delete(0, 7)
            width = float(e.get())
            show_from_0('Length: ')
            mode = 'math'
            kind = 'rectangle_Area'
            b24 = ttk.Button(root, text='=', command=equal)
            b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
        elif shape=='para_rect':
            e.delete(0, 7)
            width = float(e.get())
            show_from_0('Length: ')
            dim='h'
            b24 = ttk.Button(root, text='=', command=get_dimansions)
            b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
        else:
            show_from_0('Length: ')
            mode='math'
            if shape == 'square':
                kind='square_Area'
            elif shape == 'Cubic':
                kind = 'cubic'
            b24 = ttk.Button(root, text='=', command=equal)
            b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def square_root():
    global mode
    mode='square_root'
    show_from_0('sqr_root: ')
def square():
    global mode
    mode='square'
    show_from_0('Square of: ')
def tri_A():
    global mode,dim
    mode='triangle'
    show_from_0('(/\)A mode, click(=) to enter dimansions ')
    dim = 'b'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def cir_A():
    global mode,dim,shape
    mode = 'circle'
    show_from_0('(O)A mode, click(=) to enter dimansions ')
    dim='r'
    shape='circle'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def rec_A():
    global mode,dim,shape
    mode = 'rect'
    show_from_0('(|___|)A mode, click(=) to enter dimansions ')
    dim='w'
    shape='rect'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def sqr_A():
    global mode,dim,shape
    mode = 'square_A'
    show_from_0('(|_|)A mode, click(=) to enter dimansions ')
    shape = 'square'
    dim='L'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def ball_V():
    global mode,dim,shape
    mode = 'ball'
    show_from_0('(Ball V) mode, click(=) to enter dimansions ')
    dim='r'
    shape='Ball'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def cyl_V():
    global mode,dim,shape
    mode = 'cylinder'
    show_from_0('(Cylinder V) mode, click(=) to enter dimansions ')
    dim='h'
    shape='cylinder'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def cub_V():
    global mode,dim,shape
    mode = 'cubic'
    show_from_0('(Cubic V) mode, click(=) to enter dimansions ')
    dim='L'
    shape = 'Cubic'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def cone_V():
    global mode,dim,shape
    mode = 'cone'
    show_from_0('(Cone V) mode, click(=) to enter dimansions ')
    dim='h'
    shape = 'cone'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def para_rec_V():
    global mode,dim,shape
    mode = 'para_rect'
    show_from_0('(Para rect V) mode, click(=) to enter dimansions ')
    dim='w'
    shape='para_rect'
    b24 = ttk.Button(root, text='=', command=get_dimansions)
    b24.grid(row=9, column=2, stick='snew', padx=22, pady=15)
def numbers(x):
    e.insert(END,x)
def equal():
    global dim,mode,height,base,width,radius,length
    if mode=='square_root':
        e.delete(0,9)
        show_from_0(math.sqrt(float(e.get())))
    elif mode=='square':
        e.delete(0,11)
        show_from_0(float(e.get())**2)
    elif mode=='triangle':
        tri_A()
    elif mode == 'circle':
        cir_A()
    elif mode == 'rect':
        rec_A()
    elif mode == 'square_A':
        sqr_A()
    elif mode == 'ball':
        ball_V()
    elif mode== 'cylinder':
        cyl_V()
    elif mode=='cubic':
        cub_V()
    elif mode=='cone':
        cone_V()
    elif mode=='para_rect':
        para_rec_V()
    elif mode=='math':
        if kind=='triangle_Area':
            e.delete(0,8)
            height=float(e.get())
            show_from_0(0.5*base*height)
        elif kind=='circle_Area':
            e.delete(0,8)
            radius=float(e.get())
            show_from_0((math.pi)*radius**2)
        elif kind=='rectangle_Area':
            e.delete(0, 8)
            length = float(e.get())
            show_from_0( width * length)
        elif kind=='square_Area':
            e.delete(0,8)
            length=float(e.get())
            show_from_0(length**2)
        elif kind=='Ball':
            e.delete(0,8)
            radius=float(e.get())
            show_from_0((4/3)*(math.pi)*radius**3)
        elif kind == 'cubic':
            e.delete(0, 8)
            length = float(e.get())
            show_from_0(length ** 3)
        elif kind == 'cylinder':
            e.delete(0, 8)
            radius = float(e.get())
            show_from_0(height * (math.pi) * radius ** 2)
        elif kind=='cone':
            e.delete(0, 8)
            radius = float(e.get())
            show_from_0((1/3)*height * (math.pi) * radius ** 2)
        elif kind=='para_rect':
            e.delete(0,8)
            height=float(e.get())
            show_from_0(width*length*height)


#  Design the machine
# The label
e=ttk.Entry(root,width=40,font=('Arial',12,'bold'))
e.grid(row=0,column=0,columnspan=3,ipady=5)
# The buttons
b1=ttk.Button(root,text='sqr_root',command=square_root)
b2=ttk.Button(root,text='X^2',command=square)
b3=ttk.Button(root,text='clear',command=remove)
b4=ttk.Button(root,text='(/\)A',command=tri_A)
b5=ttk.Button(root,text='(O) A',command=cir_A)
b6=ttk.Button(root,text='(|___|)A',command=rec_A)
b7=ttk.Button(root,text='( |_| ) A',command=sqr_A)
b8=ttk.Button(root,text='Ball V',command=ball_V)
b9=ttk.Button(root,text='Cylinder V',command=cyl_V)
b10=ttk.Button(root,text='Cubic V',command=cub_V)
b11=ttk.Button(root,text='cone V',command=cone_V)
b12=ttk.Button(root,text='Parallel rectangles V',command=para_rec_V)
b13=ttk.Button(root,text='1',command=lambda:numbers(1))
b14=ttk.Button(root,text='2',command=lambda:numbers(2))
b15=ttk.Button(root,text='3',command=lambda:numbers(3))
b16=ttk.Button(root,text='4',command=lambda:numbers(4))
b17=ttk.Button(root,text='5',command=lambda:numbers(5))
b18=ttk.Button(root,text='6',command=lambda:numbers(6))
b19=ttk.Button(root,text='7',command=lambda:numbers(7))
b20=ttk.Button(root,text='8',command=lambda:numbers(8))
b21=ttk.Button(root,text='9',command=lambda:numbers(9))
b22=ttk.Button(root,text='0',command=lambda:numbers(0))
b23=ttk.Button(root,text='.',command=lambda:numbers('.'))
b24=ttk.Button(root,text='=',command=equal)
# put them in a grid
b1.grid(row=1,column=0,sticky='snew',padx=22,pady=15)
b2.grid(row=1,column=1,sticky='snew',padx=22,pady=15)
b3.grid(row=1,column=2,sticky='snew',padx=22,pady=15)
b4.grid(row=2,column=0,sticky='snew',padx=22,pady=15)
b5.grid(row=2,column=1,sticky='snew',padx=22,pady=15)
b6.grid(row=2,column=2,sticky='snew',padx=22,pady=15)
b7.grid(row=3,column=0,columnspan=3,padx=22,sticky='snew',pady=15)
b8.grid(row=4,column=0,sticky='snew',padx=22,pady=15)
b9.grid(row=4,column=1,sticky='snew',padx=22,pady=15)
b10.grid(row=4,column=2,sticky='snew',padx=22,pady=15)
b11.grid(row=5,column=0,sticky='snew',padx=22,pady=15)
b12.grid(row=5,column=1,columnspan=2,sticky='snew',padx=22,pady=15)
b13.grid(row=6,column=0,sticky='snew',padx=22,pady=15)
b14.grid(row=6,column=1,sticky='snew',padx=22,pady=15)
b15.grid(row=6,column=2,sticky='snew',padx=22,pady=15)
b16.grid(row=7,column=0,sticky='snew',padx=22,pady=15)
b17.grid(row=7,column=1,sticky='snew',padx=22,pady=15)
b18.grid(row=7,column=2,sticky='snew',padx=22,pady=15)
b19.grid(row=8,column=0,sticky='snew',padx=22,pady=15)
b20.grid(row=8,column=1,sticky='snew',padx=22,pady=15)
b21.grid(row=8,column=2,sticky='snew',padx=22,pady=15)
b22.grid(row=9,column=0,sticky='snew',padx=22,pady=15)
b23.grid(row=9,column=1,sticky='snew',padx=22,pady=15)
b24.grid(row=9,column=2,stick='snew',padx=22,pady=15)


root.mainloop()