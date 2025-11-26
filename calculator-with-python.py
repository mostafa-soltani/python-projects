from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("310x400")
root['bg'] = 'black'
root.resizable(False, False)

#show the title
label = Label(root, text='Pro Calculator', width=300, bg='black', fg='white', font='arial 12 bold')
label.pack()

data = ''  #save the input


#show in the label
def show_on_label(button_text):
    global data
    data += button_text  #add another data
    label_for_shownum.config(text=data[:11])  #limited to 11 char


#func to use eval
def calculate():
    global data
    try:
        #use eval() to calculate
        result = eval(data)
        label_for_shownum.config(text=str(result))  #show result
        data = str(result)  #save the result for next calculate
    except Exception as e:
        label_for_shownum.config(text="Error")
        data = ''


#reset the data
def clear():
    global data
    data = ''
    label_for_shownum.config(text='')

#deleted the last char
def backspace():
    global data
    data = data[:-1]  # حذف آخر کاراکتر 
    label_for_shownum.config(text=data)


#keyboard manengment
def key_press(event):
    global data
    key = event.char


    #if key was operator or number
    if key.isdigit() or key in '+-*/)()':
        data += key
        label_for_shownum.config(text=data[:11])
    elif key == '\r':
        calculate()

    elif key == '\x08':
        backspace()



#the advanced func
def calculate_sin():
    global data
    try:
        result = math.sin(math.radians(float(data)))
        label_for_shownum.config(text=str(round(result, 5)))
        data = str(result)
    except:
        label_for_shownum.config(text="Error")
        data = ''


def calculate_cos():
    global data
    try:
        result = math.cos(math.radians(float(data)))
        label_for_shownum.config(text=str(round(result, 5)))
        data = str(result)
    except:
        label_for_shownum.config(text="Error")
        data = ''


def calculate_tan():
    global data
    try:
        result = math.tan(math.radians(float(data)))
        label_for_shownum.config(text=str(round(result, 5)))
        data = str(result)
    except:
        label_for_shownum.config(text="Error")
        data = ''


def calculate_log():
    global data
    try:
        result = math.log10(float(data))
        label_for_shownum.config(text=str(round(result, 5)))
        data = str(result)
    except:
        label_for_shownum.config(text="Error")
        data = ''


#label for show the calculate
label_for_shownum = Label(root, text='0', font='arial 35 bold', bg='black', fg='white', anchor='e')
label_for_shownum.place(x=0, y=40, width=310, height=50)

# location of buttons 
buttons = [
    ('7', 0, 100), ('8', 44, 100), ('9', 88, 100), ('/', 133, 100),
    ('4', 0, 156), ('5', 44, 156), ('6', 88, 156), ('*', 133, 156),
    ('1', 0, 212), ('2', 44, 212), ('3', 88, 212), ('-', 133, 212),
    ('C', 0, 268), ('0', 44, 268), ('=', 88, 268), ('+', 133, 268),
    ('sin', 178, 100), ('cos', 221, 100), ('tan', 265, 100),
    ('log', 178, 156), ('%', 221, 156), ('pi', 265, 156),
    ('(', 178, 212), (')', 221, 212), ('.', 265, 212),
]

#make the buttons 
for (text, x, y) in buttons:
    if text == '=':
        Button(root, text=text, width=5, height=2, bg='orange', fg='white', command=calculate).place(x=x, y=y)
    elif text == 'C':
        Button(root, text=text, width=5, height=2, bg='red', fg='white', command=clear).place(x=x, y=y)
    elif text == 'sin':
        Button(root, text=text, width=5, height=2, bg='grey', fg='white', command=calculate_sin).place(x=x, y=y)
    elif text == 'cos':
        Button(root, text=text, width=5, height=2, bg='grey', fg='white', command=calculate_cos).place(x=x, y=y)
    elif text == 'tan':
        Button(root, text=text, width=5, height=2, bg='grey', fg='white', command=calculate_tan).place(x=x, y=y)
    elif text == 'log':
        Button(root, text=text, width=5, height=2, bg='grey', fg='white', command=calculate_log).place(x=x, y=y)
    else:
        Button(root, text=text, width=5, height=2, bg='grey', fg='white',
               command=lambda t=text: show_on_label(t)).place(x=x, y=y)


root.bind('<Key>',key_press)

root.mainloop()