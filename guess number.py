import random
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title('game')
root.geometry('500x400')
root.resizable(False,False)

label = tk.Label(root,text='guess the number',bg='darkred',fg='white',font='arial 30 bold')
label.pack(fill='x',padx=10,pady=10)

doThing = tk.Label(root,text='''pls inter the first guess and click the button
to see if its right or wrong
if its higher than the actual number the color is blue 
and if its lower then actual number the color is red
and if its right and its currect the color is green ''',bg='darkblue',fg='white',font='arial 14 bold')
doThing.place(x=8,y=70)


entry_guess = tk.Entry(root,fg='white',bg='darkgreen',font='arial 30 bold',justify='center')
entry_guess.place(x=30,y=190)


show_status = tk.Label(root,width=80,height=80)
show_status.place(x=0,y=280)

javab = random. randint(1 , 99)
print(javab)

def guess_statues(event=None):
    global javab

    try:
        guess = int(entry_guess.get())

        if guess > javab:
            show_status.config(bg='red')
            messagebox.askretrycancel('lower', 'please guess lower!!!!!')

        elif guess < javab:
            show_status.config(bg='blue')
            messagebox.askretrycancel('higher', 'please guess higher!!!!')

        else:
            show_status.config(bg='green')
            yes_or_no = messagebox.askretrycancel(
                'congrats',
                'you guessed correctly! Want to play again?'
            )

            if yes_or_no:
                entry_guess.delete(0, tk.END)
                javab = random.randint(1, 99)
                show_status.config(bg='white')
            else:
                root.destroy()

    except Exception as e:
        messagebox.showerror('error', str(e))
        entry_guess.delete(0, tk.END)


check_button = tk.Button(root,text='check',bg='cyan',fg='black',font='arial 13 bold',command=guess_statues)
check_button.place(x=220,y=245)


entry_guess.bind('<Return>',guess_statues)

root.mainloop()