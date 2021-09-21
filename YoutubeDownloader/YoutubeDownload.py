
from tkinter import *
from tkinter import ttk , messagebox
from pytube import YouTube

def download(url , details):
    try:
        youtube = YouTube(url)
        video = youtube.streams.first()
        video.download()
        details['text'] = "Title: "+ youtube.title + '\n'\
                          + "Length: " + str(youtube.length/60)+ '\n'\
                          + "Views: " + str(youtube.views) + '\n' \
                          + "Description: " + youtube.description
    except:
        messagebox.showerror(":((" , 'Failed to download')

root = Tk()
root.title("My download app")
root.geometry("300x400")
root.configure(bg = '#000000')
root.resizable(width=0 , height = 0)
s = ttk.Style()
s.theme_use('clam')
s.configure("TButton" , background="#f3ca20" , font=("Arial",9,'bold'))


e_link = ttk.Entry(root)


l_details = ttk.Label(root , background="#f3ca20")

b_download = ttk.Button(root , text="DOWNLOAD" , command=lambda:download(e_link.get() , l_details) )

# show components
e_link.place(x = 10 , y = 20 , width=280 , height=30)
b_download.place(x=100 , y=70 , width=90 , height=28 )
l_details.place(x = 20 , y = 120 , width=260 , height=260 )


root.mainloop()
