from Tkinter import *
import ttk
root= Tk()
prob=StringVar()
ans=StringVar()
probentry=ttk.Entry(root,textvariable=prob,style='TEntry')
probentry.configure(font=('Monaco',15),background='Red')
container=Frame(root,relief='groove',width=30,height=30,borderwidth=2).grid(column=0,row=1,columnspan=5,padx=3,pady=3,sticky=NSEW)
lans=Label(container,textvariable=ans,font=('Monaco',13,'bold'))
def clear(*args):
    probentry.delete(0,END)
y=ttk.Style().configure('TButton',width=5,height=2)
clear=ttk.Button(root, text='AC',command=clear,style='TButton').grid(column=4,row=2,padx=2,pady=2,sticky=NSEW)
def showprob(*args):
    signs=('+','-','*','/')
    for sign in signs:
        if sign in prob.get():
            sn=prob.get()[prob.get().index(sign)]
    val=''
    val+=str(float(prob.get()[:prob.get().index(sn)]))+sn+prob.get()[prob.get().index(sn)+1:]
    print val
    ans.set(eval(val))
equals=ttk.Button(root, text='=', command=showprob,style='TButton').grid(column=4,row=5,sticky=NSEW,padx=2,pady=2)
root.bind('<Return>',showprob)
root.title('Calculator')
class button(object):
    '''Create a button and set its attributes'''
    def __init__(self,parent,name,button):
        self.parent=parent
        self.button=button
        self.name=name
        x=ttk.Style().configure('TButton',font=('Mistral',21),width=5,height=2)
        self.button=ttk.Button(self.parent,text=self.name,command=self.butclick,style='TButton')
    def positionset(self,col,row):
        self.button.grid(column=col,row=row,sticky=NSEW,pady=2,padx=2)
    def butclick(self):
        if self.name=='1':
            probentry.insert(len(probentry.get())+1,1)
        elif self.name=='2':
            probentry.insert(len(probentry.get())+1,2)
        elif self.name=='3':
            probentry.insert(len(probentry.get())+1,3)
        elif self.name=='4':
            probentry.insert(len(probentry.get())+1,4)
        elif self.name=='5':
            probentry.insert(len(probentry.get())+1,5)
        elif self.name=='6':
            probentry.insert(len(probentry.get())+1,6)
        elif self.name=='7':
            probentry.insert(len(probentry.get())+1,7)
        elif self.name=='8':
            probentry.insert(len(probentry.get())+1,8)
        elif self.name=='9':
            probentry.insert(len(probentry.get())+1,9)
        elif self.name=='0':
            probentry.insert(len(probentry.get())+1,0)
        elif self.name=='+':
            probentry.insert(len(probentry.get())+1,'+')
        elif self.name=='-':
            probentry.insert(len(probentry.get())+1,'-')
        elif self.name=='/':
            probentry.insert(len(probentry.get())+1,'/')
        elif self.name=='*':
            probentry.insert(len(probentry.get())+1,'*')
##    def configu(self):
##        self.button.configure('TButton',highlightcolor='Blue',state=DISABLED,borderwidth=1)

probentry.grid(column=0, row=0,columnspan=5,padx=3,pady=3,sticky=NSEW)
lans.grid(column=0,row=1,padx=3,pady=3)
probentry.focus()
e1=button(root,'','')
e1.positionset(0,2)
e2=button(root,'','')
e2.positionset(1,2)
e3=button(root,'','')
e3.positionset(2,2)
e4=button(root,'','')
e4.positionset(3,2)
##e1.configu(), e2.configu(),e3.configu(),e4.configu()
zero=button(root,'0','zero')
zero.positionset(3,5)
one=button(root,'1','one')
one.positionset(0,3)
two=button(root,'2','two')
two.positionset(1,3)
three=button(root,'3','three')
three.positionset(2,3)
four=button(root,'4','four')
five=button(root,'5','five')
six=button(root,'6','six')
four.positionset(0,4)
five.positionset(1,4)
six.positionset(2,4)
seven=button(root,'7','seven')
eight=button(root,'8','eight')
nine=button(root,'9','nine')
seven.positionset(0,5)
eight.positionset(1,5)
nine.positionset(2,5)
plus=button(root,'+','plus')
plus.positionset(3,4)
minus=button(root,'-','minus')
minus.positionset(4,3)
divide=button(root,'/','divide')
divide.positionset(4,4)
multiply=button(root,'*','multiply')
multiply.positionset(3,3)
for i in range(6):
    col=i
    root.columnconfigure(col, weight=3)
for i in range(6):
    row=i
    root.rowconfigure(row, weight=3)
print root.slaves()
root.mainloop()
