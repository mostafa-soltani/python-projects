from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo(' ', 'bashe')


def motionmose(event):
    btnyes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='are you gay?? ', font='Arial 20 bold', bg='white')
label.pack()

btnyes = Button(root, text='no', font='Arial 20 bold', command=no)
btnyes.place(x=170, y=100)
btnyes.bind('<Enter>', motionmose)

btnno = Button(root, text='yes', font='Arial 20 bold', command=no)
btnno.place(x=350, y=100)

root.mainloop()