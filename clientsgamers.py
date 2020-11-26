import threading,socket,time
from PIL import Image,ImageTk
from tkinter import *
import random,playsound
from tkinter import messagebox
root=Tk()
root.geometry("800x600")
ip=socket.gethostname()
port=5151
speed=5
addr=(ip,port)
class gamer:
    def __init__(self):
        
        self.startview()
    def gameover(self,winner):
        messagebox.showinfo("winner",winner+" is the winner")
        self.startframemain.destroy()
        self.startview()
    def initial(self):
         self.bx=20
         self.by=20
         self.timer=0.1

    def move1(self,x):
        self.yp=self.startframe2.coords(self.yourlabel)[1]
        if x=='w':
            
            if self.yp>65:
                self.y=-15
            else:self.y=0
            
        if x=='s':
            if self.yp<440:
                self.y=15
            else:self.y=0
            
        self.startframe2.move(self.yourlabel,0,self.y)
    def move2(self,x):
        self.yo=self.startframe2.coords(self.opplabel)[1]
        if x=='u':
            if self.yo>65:
                self.y2=-15
            else:self.y2=0
        if x=='d':
            if self.yo<440:
                self.y2=15
            else:self.y2=0
        self.startframe2.move(self.opplabel,0,self.y2)
    def moveplayer(self):
        root.bind("<Up>",lambda x: self.move2("u"))
        root.bind("<Down>",lambda x: self.move2("d"))
        root.bind("<w>",lambda x: self.move1("w"))
        root.bind("<s>",lambda x: self.move1("s"))
    # def moveball(self):
    #     while True:
    #         while self.move:

        
    def playsound(self,n):
        if n==0:
            playsound.playsound("hit.mp3")
        else:
            playsound.playsound("out.mp3")      
            
    def moveball(self):
        

        while True: 
            if self.score1>=4:
                self.gameover("player1")
            if self.score2>=4:
                self.gameover("player1")
            self.startframe2.move(self.ball,self.bx,self.by)
            root.update()
            time.sleep(self.timer)
            ball_pos = self.startframe2.coords(self.ball)
            xp,yp=self.startframe2.coords( self.yourlabel)
            xo,yo=self.startframe2.coords( self.opplabel)
            xl,yl,xr,yr = ball_pos
            if (xl>18 and xl<=20) and abs(yl-yp)<68:
                # threading.Thread(target=self.playsound(0)).start()
                self.timer-=0.0005
                self.bx = -self.bx
            else:
                if (xr>=730 and xr<=732) and abs(yr-yo)<68:
                   self.timer-=0.0003
                #    threading.Thread(target=self.playsound(0)).start()
                   self.bx = -self.bx
                elif xl < abs(self.bx)  :
                   self.playsound(1)
                   self.score2+=1
                   self.initial()
                   self.startframe2.coords(self.ball,100,100,130,130)
                   
                   self.player2score.configure(text="Player2 score:"+str(self.score2))
                   time.sleep(3)
                   continue
                elif xr > 800-abs(self.bx):
                    self.playsound(1)
                    self.score1+=1
                    self.initial()
                    self.player1score.configure(text="Player1 score:"+str(self.score1))
                    self.startframe2.coords(self.ball,20,20,50,50)
                    time.sleep(3)
                    continue

            if yl < abs(self.by) or yr > 500-abs(self.by):
                   self.by = -self.by


    def start(self):
        self.startframe.destroy()
        self.startframemain=Frame(root,height=600,width=780,bg="blue")
        self.startframemain.place(x=10,y=10)
        self.startframe2=Canvas(self.startframemain,height=500,width=780,bg="red")
        self.startframe2.place(x=0,y=0)
        photo1=PhotoImage(file="box.png").subsample(3,4)
        photo2=PhotoImage(file="ball.png").subsample(3,3)
        thread1=threading.Thread(target=self.moveplayer())
        thread1.start()
        self.yourlabel=self.startframe2.create_image(20,self.y,image=photo1)
        self.opplabel=self.startframe2.create_image(750,self.y2,image=photo1)
        self.ball=self.startframe2.create_oval(100,100,130,130,fill="blue")
        self.player1score=Label(self.startframemain,text="Player1 score:0",font=("Georgia",20,"bold"))
        self.player1score.place(x=40,y=540)
        self.player2score=Label(self.startframemain,text="Player2 score:0",font=("Georgia",20,"bold"))
        self.player2score.place(x=550,y=540)
        threadball=threading.Thread(target=self.moveball())
        threadball.start()
    def play(self):
        #  try:
        #        socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #        socket1.connect(addr)
               self.start()
        #  except:
        #          self.check=True
        #          messagebox.showerror("Error","Cannot connect to the server!! \nmake sure the server is running")
        #          self.startframe.destroy()
        #          self.startview()
    def startview(self):
        self.yp=80
        self.yo=80
        self.score1=0
        self.score2=0
        self.y=80
        self.initial()
        self.y2=80
        self.startframe=Frame(root,bg="pink",height=400,width=500)
        self.startframe.pack(pady=20)
        Label(self.startframe,text="Hello player Best of luck",font=("Georgia",22,"bold")).pack(padx=30,pady=20)
        Button(self.startframe,text="play",font=("Georgia",22,"bold"),command=lambda:self.play()).pack(pady=20)
gamer()
root.mainloop()