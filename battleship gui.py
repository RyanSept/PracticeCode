from Tkinter import *
import ttk
import tkMessageBox
import random
from PIL import Image, ImageTk

root=Tk()
root.title('Battleships(Ryan Games TM)')
root.option_add('*tearOff', FALSE)

board=Frame(root)
bdict={}
l=ttk.Label(root,text="Let's play Battleships ! Try to guess where my battleship is hidden",justify=CENTER,font=('DigifaceWide',9))
l.grid(column=0,row=0,sticky=(NSEW),columnspan=3,rowspan=2)
count=0

p1=Image.open('D:/Users/user/Desktop/PICTURES/missed.jpg')
p1.thumbnail((150,90))
missed=ImageTk.PhotoImage(p1)
p2=Image.open('D:/Users/user/Desktop/PICTURES/ocean.jpg')
ocean=ImageTk.PhotoImage(p2,size=(100,50))
p3=Image.open('D:/Users/user/Desktop/PICTURES/battleship.jpg')
p3.thumbnail((570,100))
sunk=ImageTk.PhotoImage(p3)
p4=Image.open('D:/Users/user/Desktop/PICTURES/ship.jpg')
p4.thumbnail((130,180))
ship=ImageTk.PhotoImage(p4)

buttonids=['button1', 'button2', 'button3', 'button4', 'button5', 'button6', 'button7', 'button8', 'button9', 'button10', 'button11', 'button12', 'button13', 'button14', 'button15', 'button16', 'button17', 'button18', 'button19', 'button20', 'button21', 'button22', 'button23', 'button24', 'button25']
def setship_id():
    global ship_id
    ship_id=random.choice(buttonids)
setship_id()
bid=0
counter=[]
def newgame():
    counter[:]=[]
    setship_id()
    for b in buttonids:
        bdict[b]['image']=ocean
        bdict[b]['state']=NORMAL
class commandset(Button):
    def __init__(self,button,name):
        self.name=name
        self.button=button
        self.button['command']=self.compare
    def compare(self,*args):
        guess=self.name
        if guess==ship_id:
            bdict[ship_id]['image']=sunk
            for b in buttonids:
                if bdict[b]!=bdict[ship_id]:
                    bdict[b]['state']=DISABLED
            if tkMessageBox.askyesno('New Game','You successfully sunk the battleship! \n Would you like to play a new game?'):
                newgame()
        else:
            bdict[guess]['image']=missed
        print ship_id
        counter.append('y')
        if len(counter)>=4:
            bdict[ship_id]['image']=ship
            for b in buttonids:
                if bdict[b]!=bdict[ship_id]:
                    bdict[b]['state']=DISABLED
            if tkMessageBox.askyesno('New Game','The battle has been lost but the war rages on \n Would you like to play a new game?'):
                newgame()
            else:
                root.destroy()
for row in range(1,6):
    for col in range(1,6):
        bdict[buttonids[bid]]=Button(board,width=100,height=90,image=ocean)
        bdict[buttonids[bid]].grid(row=row,column=col)
        bid+=1
for b in buttonids:
    commandset(bdict[b],b)

menubar=Menu(root)
root['menu']=menubar
menu_game=Menu(menubar)
menu_help=Menu(menubar)
menubar.add_cascade(menu=menu_game,label='Game')
menubar.add_cascade(menu=menu_help,label='Help')
menu_game.add_command(label='New Game',command=newgame)
menu_game.add_command(label='Quit Game',command=lambda: root.destroy())

board.grid(sticky=N+S+E+W,pady=2,padx=1)
root.maxsize(532,503)
root.minsize(532,503)
root.geometry('533x505')

root.mainloop()


