from Tkinter import *
import ttk
import tkFileDialog

root=Tk()
root.option_add('*tearOff', FALSE)
root.title('Text Prac')
textbox=Text(root)
textbox.grid()

def init():
    with open('D:/Users/user/Desktop/DALC EDUCATION FILES/drunkard.txt') as mytext:
        textbox.insert('end',mytext.read())
def highlight():
    seltextindex=textbox.tag_ranges('sel')
    if len(seltextindex)>1:
        first,last=seltextindex[0],seltextindex[1]
        selectedtext=textbox.get(first,last)
        textbox.tag_add('highlight',first,last)
        textbox.tag_configure('highlight',background='green')
        print selectedtext
    else:
        print 'None'
def copy(*args):
    seltextindex=textbox.tag_ranges('sel')
    if len(seltextindex)>1:
        first,last=seltextindex[0],seltextindex[1]
        selectedtext=textbox.get(first,last)
        root.clipboard_clear()
        root.clipboard_append(selectedtext)
        print root.clipboard_get()
    else:
        print 'None'
def paste(*args):
    textbox.insert('insert',root.clipboard_get())
def selectall(*args):
    textbox.tag_add('sel','1.0','end')
menubar=Menu(root)
root['menu']=menubar
clickmenu=Menu(root)
clickmenu.add_command(label='Copy',command=copy,accelerator=' Control+c')
clickmenu.add_command(label='Paste',command=paste,accelerator=' Control+v')
clickmenu.add_command(label='Select all',command=selectall)
root.bind('<Control-a>',selectall)
root.bind('<Control-v>',paste)
root.bind('<Control-c>',copy)
menubar.add_command(label='Start',command=init)
menubar.add_command(label='Copy',command=copy)
menubar.add_command(label='Highlight',command=highlight)
menubar.add_command(label='Paste',command=paste)
root.bind('<3>',lambda e:clickmenu.post(e.x_root, e.y_root) ) #Menu that appears on click location

root.mainloop()
