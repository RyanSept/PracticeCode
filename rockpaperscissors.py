def rps():
    """Play the classical game Rock, Paper, Scissors"""
    print "Welcome to rock paper scissors. You will be playing against the CPU. Type 'exit' to exit the game any time"
    Player=raw_input('Please enter your name:')
    n='r','p','s'
    import random
    rnd=random.choice(n)
    x=raw_input("Please enter r for Rock, p for Paper or s for Scissors:")
    x=str(x)
    while len(x)<2:
        if x=='exit':
            break
        if x.isalpha()==False or len(x)>1 or len(x)==0:
            print 'Invalid Value.Please try again.'
            x=raw_input("Please enter r for Rock, p for Paper or s for Scissors:")
        if x==rnd:
            print 'Tie. Both player and computer played',x
            x=x+'q'
        elif x=='p' and rnd=='r' or x=='r' and rnd=='s' or x=='s' and rnd=='p':
            print Player,'wins!:',x,'beats',rnd
            x=x+'q'
        elif rnd=='p' and x=='r' or rnd=='r' and x=='s' or rnd=='s' and x=='p':
            print "Computer wins:",rnd,'beats',x
            x=x+'q'
        rnd=random.choice(n)
        play_again=raw_input("Would you like to play again? y or n:")
        if play_again=='y':
            x=raw_input("Please enter r for Rock, p for Paper or s for Scissors:")
        elif play_again=='n':
            print "Thank you for playing. Have a nice day"
        else:
            print 'Invalid Value.Please try again.'
            play_again=raw_input("Would you like to play again? y or n:")
            x=raw_input("Please enter r for Rock, p for Paper or s for Scissors:")
dich={'p':'Paper',
      's':'Scissors',
      'r':'Rock'
      }
from Tkinter import *
import ttk
import random
root=Tk()
root.geometry('850x500')
winner=StringVar()
def oppchoice(choice):
    n=('r','p','s')
    rnd=random.choice(n)
    if choice[1]==rnd:
        winner.set('Tie')
    elif choice[1]=='p' and rnd=='r' or choice[1]=='r' and rnd=='s' or choice[1]=='s' and rnd=='p':
        winner.set("Player wins! \n %s beats %s" %(choice[0],dich[rnd]))
    elif rnd=='p' and choice[1]=='r' or rnd=='r' and choice[1]=='s' or rnd=='s' and choice[1]=='p':
        winner.set("Computer wins \n %s beats %s" %(dich[rnd],choice[0]))
def choicer():
    choice=('Rock','r')
    oppchoice(choice)
def choicep():
    choice=('Paper','p')
    oppchoice(choice)
def choices():
    choice=('Scissors','s')
    oppchoice(choice)
frame=Frame(root)
f2=Frame(root)
l=Label(frame,text='Rock Paper Scissors',font=('Harrington',20))
l2=Label(frame, text='Choose wisely', font=('Mistral',20))
l3=ttk.Label(frame,textvariable=winner,justify=CENTER, font=('Harrington',25))
by=Label(frame,text='Ryan Games TM' ,justify=RIGHT, font=('Gabriola Regular',9))

rpic=PhotoImage(file='D:/Users/user/Desktop/PICTURES/rock.gif')
ppic=PhotoImage(file='D:/Users/user/Desktop/PICTURES/paper.gif')
spic=PhotoImage(file='D:/Users/user/Desktop/PICTURES/scissors.gif')

rock=Button(frame,image=rpic,width=220,height=170,command=choicer)
scissors=Button(frame, image=spic,width=250,height=160,command=choices)
paper=Button(frame, image=ppic,width=240,height=225,command=choicep)
#playagain=Button(frame,text='Play Again?')

rock.grid(row=10,column=3,sticky=(NSEW),padx=5,pady=5)
paper.grid(row=10,column=5,sticky=(NSEW),padx=5,pady=5)
scissors.grid(row=10,column=9,sticky=(NSEW),padx=5,pady=5)
#playagain.grid(row=50,column=5, sticky=(NSEW), padx=10, pady=10)
frame.grid(row=0, column=0, sticky=(NSEW))
frame.columnconfigure(0,weight=3)
frame.columnconfigure(3,weight=2)
frame.columnconfigure(5,weight=2)
frame.columnconfigure(9,weight=2)
frame.rowconfigure(0,weight=2)
frame.rowconfigure(10,weight=2)
l.grid(column=5, row=0,sticky=(NSEW))
l2.grid(column=5, row=1,sticky=(NSEW))
l3.grid(column=5, row=30, sticky=(NSEW))
by.grid(column=10,row=100, sticky=(NSEW))
root.mainloop()

