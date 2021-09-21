from tkinter import ttk ,messagebox
from tkinter import *
from random import randrange

guessN , myN , newScore, func = 0 , 0 , 100 , 1

def restart():
    e_range1.configure(state='abled')  
    e_range2.configure(state='abled')
    e_range1.delete(0,END)  
    e_range2.delete(0,END)

def onClick():
    global guessN 
    try:
        n1 = int(e_range1.get())
        n2 = int(e_range2.get())
    except:
        messagebox.showerror('Error' , 'please enter an integer numbers.')
    guessN = randrange(n1 , n2)  
    e_range1.configure(state='disabled')  
    e_range2.configure(state='disabled')
    newWindow()

def newWindow():
    # new window
    root2 = Toplevel()
    root2.title("Guess Game")
    root2.geometry("200x200")
    root2.resizable(width = 0 , height = 0)
    root2.configure(bg = "#e52165")

    # score
    l_score = ttk.Label(root2 , text='SCORE: 100')
    l_score.pack(pady = 10)

    # clue
    l_clue = ttk.Label(root2 )
    clue(l_clue)
    l_clue.pack(pady = 10,ipadx=35,ipady=13)

    # entry of solution
    e_sol = ttk.Entry(root2 )
    e_sol.insert(0 , "Enter ur guess number!!")
    e_sol.pack(pady = 10)

    # send button
    send = ttk.Button(root2 , text='send', command=lambda:afterSend(root2 , e_sol , l_score , l_clue) )
    send.pack(pady = 10)

def score(l , newS):
    global newScore
    newScore -= 20
    l["text"] = "SCORE: "+ str(newScore)

def clue(label):
    global func
    before , after = "" , guessN+3
    # n < @
    if func == 1 :
        label['text'] =  " N " + " < " + str(after)
        func = 5
        return None
    # n > @
    if func == 2 :
        after = guessN-2
        label['text'] =" N " + " > " + str(after)
        func = 4
        return None
    # n - @ < @
    if func == 3 :
        before = " N - 4 " 
        label['text'] = before + " < " + str(after)
        func = 2
        return None
    # n + @ > @
    if func == 4 :
        before = " N + 7 " 
    # n * @ > @
    if func == 5 :
        before , after = " N x 3 " , guessN*3 - 3
        func = 3
    label['text'] = before + " > " + str(after)

def afterSend(parent , entry , labelS, labelC):
    global myN , newScore
    try:
        myN = int(entry.get())
    except :
        messagebox.showerror("Bad entering" , "Please, enter integer number bet the range.",parent=parent)
        return None

    if myN == guessN :
        messagebox.showinfo("U win" , "Congratulations!!,U choose the correct answer!",parent=parent)
        newScore = 100 
        parent.destroy()
        return None

    score(labelS ,newScore)

    if myN != guessN and newScore!=0 :
        messagebox.showerror("Wrong answer!!" , "Please try again",parent=parent)
        clue(labelC)
    
    if newScore==0:
        messagebox.showerror("u lose" , "Failed to choose the correct answer!",parent=parent)
        newScore = 100
        parent.destroy()
        return None
           



# main root
root = Tk()
root.title("Guess Game")
root.geometry("400x300")
root.resizable(width = 0 , height = 0)
root.configure(bg = "#e52165")
# style
s = ttk.Style()
s.theme_use('clam')
s.configure('TButton' , font=("Arial",9,"bold") , background='#0d1137', foreground='white')
s.configure('TLabel' , font=("Arial",11,"bold") , background='#0d1137', foreground='white')


# Label
l_to = ttk.Label(root,text=" to:")
l_detail = ttk.Label(root , text="Welcome to our game... you should enter range to let\n \
computer choose a random number\n....then you should Guess it ")

# Entry
e_range1 = ttk.Entry(root , width=5 ,  font=("Arial",14,"bold") , foreground='#0d1137' )
e_range2 = ttk.Entry(root , width=5 ,  font=("Arial",14,"bold") , foreground='#0d1137' )

# Button
b_ok = ttk.Button(root,text="OK" , command=onClick)
b_restart = ttk.Button(root,text="Restart" , command=restart)
b_exit = ttk.Button(root,text="Exit" , command=root.quit)

# show components

l_detail.place(x=10 , y=30  , width=375, height=70)

e_range1.place(x=90 , y=120 , width=70 , height=40)
l_to.place(x=180 , y=125 , width=30 , height=30)
e_range2.place(x=230 , y=120 , width=70 , height=40)

b_ok.place(x=160,y=180 , width=60 , height=30)

b_restart.place(x=70 , y=240 , width=60 , height=30)
b_exit.place(x=260 , y=240 , width=60 , height=30)



root.mainloop()


