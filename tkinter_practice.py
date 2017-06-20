####import Tkinter
####top=Tkinter.Tk()
####top.mainloop()
####from Tkinter import Tk, Frame, BOTH
##  
##from Tkinter import *
##import ttk
##root = Tk()
##l =Label(root, text="Starting...",anchor=SE)
##l.grid()
##l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
##l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
##l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
##l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
##l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
##f=Frame(root)
##f2=Frame(root)
##pic=PhotoImage(file='D:/Users/user/Desktop/PICTURES/Internet pics/akamaru gatsuga.gif')
##b1=Button(root, text='A')
##b2=Button(root, text='b',compound='bottom')
##b3=Button(root, text='C')
##b1.place(x=1, y=2)
##b3.place(x=42, y=50)
##b2.place(x=300,y=300)
##f['borderwidth'] = 5
##f['relief'] = 'sunken'
##f2['borderwidth'] = 50
##f2['relief'] = 'groove'
##measureSystem = StringVar()
##check = Checkbutton(root, text='Use Metric',
##	    onvalue='metric', offvalue='imperial')
##check.place(x=55, y=99)
##phone = StringVar()
##home = Radiobutton(root, text='Home', variable=phone, value='home')
##office = Radiobutton(root, text='Office', variable=phone, value='office')
##cell =Radiobutton(root, text='Mobile', variable=phone, value='cell')
##home.place(y=100,x=150)
##office.place(y=150,x=150)
##cell.place(y=200,x=150)
##countryvar = StringVar()
##country = ttk.Combobox(root, textvariable=countryvar)
##country.place(x=66,y=150)
##country['values'] = ('USA', 'Canada', 'Australia','Kenya represent','India', 'Japan','Finland')
##root.mainloop()

from Tkinter import *
import ttk
import tkFileDialog
from tkdndwrapper import TkDND

root = Tk()
dnd = TkDND(root)
root.title('Prac')
menubar=Menu(root)
root['menu']=menubar
menu_file=Menu(menubar)
menubar.add_cascade(menu=menu_file,label='File')
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)
lst=('un','deux','trois','quatre','cinq')
nums=StringVar(value=lst)
l=Listbox(frame, height=20,listvariable=nums).grid(column=2, row=1,sticky=E+W)
onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)
f=tkFileDialog.askopenfilenames(parent=root,title='Choose a file...')
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")
print f
content.grid(column=0, row=0,sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2,sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2,sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2,sticky=(N,E, W),pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)
root.mainloop()

##from Tkinter import *
##import ttk
##
##def calculate(*args):
##    try:
##        value = float(feet.get())
##        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
##    except ValueError:
##        pass
##    
##root = Tk()
##root.title("Feet to Meters")
##
##mainframe = ttk.Frame(root, padding="3 3 12 12")
##mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
##mainframe.columnconfigure(0, weight=1)
##mainframe.rowconfigure(0, weight=1)
##
##feet = StringVar()
##meters = StringVar()
##
##feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
##feet_entry.grid(column=2, row=1, sticky=(W, E))
##
##ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
##ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
##
##ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
##ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
##ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
##
##for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
##
##feet_entry.focus()
##root.bind('<Return>', calculate)
##
##root.mainloop()

