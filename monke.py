from tkinter import * 
import random
import monke_menues_hehe
from datetime import date 
def monkee():
    f=Tk() 
    f.title("monke game") 
    f.geometry("800x500")
    gameboard=Frame(f,bg="black",height=500,width=800)
    gameboard.place(x=0,y=0,bordermode=OUTSIDE)
    buttons=[]
    for i in range(5): 
        for j in range(8):  
            buttons.append(Button(gameboard,fg="red",bg="white",width=13,height=6).grid(column=j,row=i))

    presed=[False for i in range(9)]
    t=[]

    def thework(i): 
        t[i].destroy()
        presed[i]=True
        
    def gamestart():
        print("game started")
        for i in range(9): 
            t[i]["text"]=""
        t[0]["command"]=lambda: do(t,0)

    def do(t,n):
        lostwon=False
        if n==0:
            thework(n) 
            presed[0]=True
            n+=1
        elif n==8 and presed[7]==True :
            thework(8)
            f.destroy()
            monke_menues_hehe.won()
            lostwon=True
            
        elif presed[n-1]==False: 
            f.destroy()
            monke_menues_hehe.lost()
            lostwon=True
        else: 
            thework(n)
            n+=1
        h=len(open("records.txt").readlines())
        if lostwon==True:
            with open("records.txt","a") as s: 
                ch=str(h)+" "+str(n)+" "+str(n==8)+" "+str(date.today())
                s.write("\n"+ch)
            s.close()

    for j in range(9): 
        t.append(Button(gameboard,text=str(j+1),bg="black",bd=3,fg="yellow",padx=0,pady=0, width=13,height=6))

    t[0]["command"]=lambda:gamestart()
    t[1]["command"]=lambda:do(t,1)
    t[2]["command"]=lambda:do(t,2)
    t[3]["command"]=lambda:do(t,3)
    t[4]["command"]=lambda:do(t,4)
    t[5]["command"]=lambda:do(t,5)
    t[6]["command"]=lambda:do(t,6)
    t[7]["command"]=lambda:do(t,7)
    t[8]["command"]=lambda:do(t,8)

    x=[]
    y=[]
    for i in range(9): 
        xpos=random.randrange(8)
        ypos=random.randrange(5)
        while (xpos in x) and (ypos in y) :
            xpos=random.randrange(8)
            ypos=random.randrange(5)
        t[i].grid(column=xpos,row=ypos)
        x.append(xpos)
        y.append(ypos)
    f.mainloop() 
