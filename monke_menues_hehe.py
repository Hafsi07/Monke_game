from tkinter import *
import readline
from numpy import square 
def toyota(f):
    n=[]
    squares=[0 for i in range(9) ]
    gamesplayed=-1
    gameswon=-1
    ch=f.readline()
    while ch!="":
        ch=str(f.readline())
        gamesplayed+=1
        n=ch.split(" ")
        if n!=[''] and n[2]== "False": 
            squares[int(n[1])]+=1
        else: 
            gameswon+=1
    g=Tk() 
    g.geometry("200x150")
    Label(g).pack()
    Label(g,text="Games played: "+str(gamesplayed)).pack()
    Label(g).pack()
    Label(g,text=str(gameswon)+"/"+str(gamesplayed)+" games won" ).pack() 
    Label(g).pack()
    for i in range(9): 
        if max(squares)==squares[i]: 
            break
    if i==0: 
        Label(g,text="Player usually loses on the 1st square").pack()
    elif i==1: 
        Label(g,text="Player usually loses on the 2nd square").pack()
    else: 
        Label(g,text="Player usually loses on the "+str(i+1)+"th square").pack()
    g.mainloop()


def statt(self): 
    ok=True
    self.destroy() 
    try :
        f=open("records.txt","r",encoding="utf-8")
    except :
        f=open("records.txt","w")
        f.write("game stats hehe: ")
        f.close()
        f=open("records.txt","r")
        ok=False
        exit()
    if not ok: 
        exit()
    else: 
        toyota(f)
    f.close()

def replay(self): 
    self.destroy() 
    import monke 
    monke.monkee()

def returrn(self):
    self.destroy()
    main_menu()

def main_menu(): 
    global ch 
    ch=""
    f=Tk()
    f.title("Monke")
    f.geometry("205x200") 
    f["bg"]="black"
    Button(f,text="start the game",command=lambda:replay(f),relief=GROOVE).place(x=60,y=50)
    Button(f,text="view stats",command=lambda:statt(f),relief=GROOVE).place(x=75,y=110)
    f.mainloop()

def lost(): 
    f=Tk()
    f.title("")
    f["bg"]="black"
    f.geometry("300x200")
    Label(f,bg="black",text="You lost!",fg="white",font=("arial",15)).place(x=110,y=30)
    Button(f,text="Replay",width=10,command= lambda :replay(f),relief=GROOVE).place(x=110,y=70)
    Button(f,text="Quit",width=10,command=lambda:f.destroy() ,relief=GROOVE).place(x=110,y=150)
    Button(f,text="Main menu",width=10,command=lambda:returrn(f) ,relief=GROOVE).place(x=110,y=110)

    f.mainloop()

def won():
    f=Tk()
    f.title("")
    f.geometry("300x200")
    f["bg"]="black"
    Label(f, text="Congratulations, \n you beat monke!",fg="white",bg="black",font=("arial",14)).place(x=82,y=35)
    Button(f,text="Replay",width=10,command= lambda :replay(f),relief=GROOVE).place(x=115,y=110)
    Button(f,text="Main menu",width=10,command=lambda:returrn(f) ,relief=GROOVE).place(x=115,y=150)
    f.mainloop()