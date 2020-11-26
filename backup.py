import threading,socket,time
from PIL import Image,ImageTk
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("800x600")
ip=socket.gethostname()
port=5151
addr=(ip,port)
class gamer:
    def __init__(self):
        self.startview()
    def move(self,x):
        if x=='w':
            if self.y>0:
                self.y=self.y-10
        if x=='s':
            if self.y<350:
                self.y=self.y+10
            
        self.yourlabel.place(x=10,y=self.y)
    def moveplayer(self):
        root.bind("<w>",lambda x: self.move("w"))
        root.bind("<s>",lambda x: self.move("s"))
    def start(self):
        self.startframe.destroy()
        self.startframe2=Frame(root,height=500,width=780,bg="red")
        self.startframe2.place(x=10,y=10)
        photo1=PhotoImage(file="box.png").subsample(3,4)
        thread1=threading.Thread(target=self.moveplayer())
        thread1.start()
        self.yourlabel=Label(self.startframe2,image=photo1)
        self.yourlabel["image"]=photo1
        self.yourlabel.place(x=10,y=self.y)
        
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
        self.y=80
        self.startframe=Frame(root,bg="pink",height=400,width=500)
        self.startframe.pack(pady=20)
        Label(self.startframe,text="Hello player Best of luck",font=("Georgia",22,"bold")).pack(padx=30,pady=20)
        Button(self.startframe,text="play",font=("Georgia",22,"bold"),command=lambda:self.play()).pack(pady=20)
gamer()
root.mainloop()