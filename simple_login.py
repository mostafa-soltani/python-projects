from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import csv
from tkinter import messagebox

 


# function for create account and save the data on csv 
def open_win():
    save_pass = tk.Toplevel()
    save_pass.geometry('400x400')
    save_pass.resizable(False,False)
    label = Label(save_pass,text='!!! welcome  !!!',font='arial 36 bold',bg='blue',fg='white')
    label.place(x=40,y=90)

    def on_focus_in(event):
        if entry_for_username1.get() == 'Username: ':
            entry_for_username1.delete(0, tk.END)
            entry_for_username1.config(fg='black')

    def on_focus_out(event):
        if entry_for_username1.get() == '':
            entry_for_username1.insert(0,'Username: ')
            entry_for_username1.config(fg='black')


    entry_for_username1 = tk.Entry(save_pass,width=30)
    entry_for_username1.place(x=115,y=160)
    entry_for_username1.insert(0,'Username: ')

    entry_for_username1.bind('<FocusIn>', on_focus_in)
    entry_for_username1.bind('<FocusOut>', on_focus_out)


    entry_for_password1 = tk.Entry(save_pass,width=30)
    entry_for_password1.place(x=115,y=190)
    entry_for_password1.insert(0,'Password: ')

    def on_focus_in(event):
        if entry_for_password1.get() == 'Password: ':
            entry_for_password1.delete(0, tk.END)
            entry_for_password1.config(fg='black')

    def on_focus_out(event):
        if entry_for_password1.get() == '':
            entry_for_password1.insert(0,'Password: ')
            entry_for_password1.config(fg='black')


    entry_for_password1.bind('<FocusIn>', on_focus_in)
    entry_for_password1.bind('<FocusOut>', on_focus_out)

    user_pass = {}
    # func for save the user data on csv
    def cocc():
        try:
            with open('D:/MOSIISOM/python file/pass_user.csv','a+',newline = '')as f:
                writer = csv.writer(f)
                writer.writerow([entry_for_username1.get(),entry_for_password1.get()])
                usarname = entry_for_username1.get()
                password = entry_for_password1.get()
                user_pass[entry_for_username1.get()] = entry_for_password1.get()
                print(user_pass)
                messagebox.showinfo('allright','password saved',icon='info')
                save_pass.destroy()
            f.close()
                

        except Exception as e:
            messagebox.showerror('error',e,icon='error')

    button_for_create = Button(save_pass,text=' create ',width=20,bg='black',fg='white',command=cocc)
    button_for_create.place(x=130,y=220)

root = tk.Tk() 
root.title('password manenger')
root.geometry('400x400')
root['bg'] = 'grey'



label = Label(root,text='!!! welcome back !!!',font='arial 27 bold',bg='grey',fg='black')
label.place(x=40,y=90)

def on_focus_in(event):
    if entry_for_username.get() == 'Username: ':
        entry_for_username.delete(0, tk.END)
        entry_for_username.config(fg='black')

def on_focus_out(event):
    if entry_for_username.get() == '':
        entry_for_username.insert(0,'Username: ')
        entry_for_username.config(fg='black')


entry_for_username = tk.Entry(root,width=30)
entry_for_username.place(x=115,y=160)
entry_for_username.insert(0,'Username: ')

entry_for_username.bind('<FocusIn>', on_focus_in)
entry_for_username.bind('<FocusOut>', on_focus_out)


entry_for_password = tk.Entry(root,width=30,show="*")
entry_for_password.place(x=115,y=190)
entry_for_password.insert(0,'Password: ')

def on_focus_in(event):
    if entry_for_password.get() == 'Password: ':
        entry_for_password.delete(0, tk.END)
        entry_for_password.config(fg='black',show='*')

def on_focus_out(event):
    if entry_for_password.get() == '':
        entry_for_password.insert(0,'Password: ')
        entry_for_password.config(fg='black',show='*')


entry_for_password.bind('<FocusIn>', on_focus_in)
entry_for_password.bind('<FocusOut>', on_focus_out)



button_for_create_account = Button(root,text='create an account',bg='black',fg='white',command=open_win)
button_for_create_account.place(x=10,y=10)

def see_existense():
    real_username = entry_for_username.get()
    real_password = entry_for_password.get()

    try:
        with open('D:/MOSIISOM/python file/pass_user.csv', 'r', newline='') as f:
            reader = csv.reader(f)

            found = False # if founded the user
            found_pass = False
            for row in reader:
                if len(row) < 2:  #if the row was half
                    continue

                username, password = row[0], row[1]

                if username == real_username:  #founded the user
                    found = True
                    if password == real_password:
                        messagebox.showinfo('welcome back', 'your entrance is ok!!!', icon='info')
                    if not found_pass:
                        messagebox.askretrycancel('error', 'password is incorrect', icon='error')
                        entry_for_password.delete(0,END)
                    break

            if not found:
                messagebox.askretrycancel('error', 'username is incorrect', icon='error')
                entry_for_username.delete(0,END)
                entry_for_password.delete(0,END)
    except Exception as e:
        messagebox.showerror('error', str(e), icon='error')

        
    

button_for_sign_in = Button(root,text='sign in',bg='black',fg='white',width=20,command=see_existense)
button_for_sign_in.place(x=130,y=220)


def sign_in():
    print()

root.mainloop() 