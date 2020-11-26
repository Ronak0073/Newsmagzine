# importing Module
from  tkinter import *
import datetime
import pygame


# defining GUi
root=Tk()

# setting resoulution
root.geometry("900x750")                            #intiling the windows with resoulution
root.maxsize(900,750)                               #maximum resoulition of window
root.minsize(900,750)                               #minimum resoulution of window


# window tittle                                     #tittle of the window
root.title("Newspaper")


# logo of the newspaper
logo=Button(text="New York Times",font="elephant 18 italic",bg="black",fg="white",relief=SUNKEN,borderwidth=5,padx=1,pady=10)
logo.pack(fill=X)

# Date
c=datetime.datetime.now()
time=Label(text=c)
time.place(x=8,y=90)


# Headline
h1=Label(text="Trump Administration Approves Start of Formal Transition to Biden",font='cambria 16 bold')
h1.place(x=125,y=120)

#  Discription
content=Label(text="""A key official designated President-elect Joe Biden as the apparent winner after Michigan
 certified his victory there and President Trump lost another court decision in Pennsylvania.

""",font="century 12",padx=1)
content.place(x=110,y=165)

# image
p1=PhotoImage(file="1.png")
pic=Button(image=p1,relief=GROOVE,borderwidth=2)
pic.place(x=380,y=225)

# main  content
with open("trump.txt") as f:
    a=f.read()

content1=Label(text=a,font="century 12")
content1.place(x=50,y=400)

# music for fun :)

pygame.init()
def play():
    pygame.mixer.music.load("C:\\Users\\Aarush\\Music\\sample1.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device

music=Button(text="play",command=play,font='elephant 8 italic')
music.place(x=525,y=363)


# running the Gui/program
root.mainloop()
