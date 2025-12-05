import tkinter as tk # library for grafical programingg
from tkinter import messagebox
from deep_translator import GoogleTranslator # to translate with google translator
root = tk.Tk()
root.title('translate')
root.geometry('642x400')
root.resizable(False,False)

ruw_data = tk.Text(root, height=2, bg='black', fg='white')
ruw_data.pack(fill='x', padx=10, pady=10, expand=True)
ruw_data.place(y=10)


dict_box = GoogleTranslator().get_supported_languages(as_dict=True)
items = dict_box.keys()


show_label = tk.Label(root,text='',bg='black',fg='white',wraplength=250)
show_label.place(x=100,y=100)


def show_selection():
    try:
        index = box_list.curselection()[0]
        value = box_list.get(index)
        #messagebox.showinfo('info',f'you selected {value}')
        ttranslate = GoogleTranslator(source='auto',target=str(value))
        if not ruw_data.get("1.0","end-1c"):
            messagebox.askretrycancel('error','pls inter in first entry!!!!')
            return
        a = ttranslate.translate(ruw_data.get("2.0","end-1c"))

        show_label.config(text=a,font='arial 14 bold')


    except Exception as e:
        messagebox.showerror('error',str(e))
        print(e)
        pass


def search_by_key(event):
    key = event.char.lower()
    if not key.isalpha():
        return
    
    for indx,item in enumerate(items):
        if item.lower().startswith(key):
            box_list.selection_clear(0,tk.END)
            box_list.selection_set(indx)
            box_list.activate(indx)
            box_list.see(indx)
            break




frame = tk.Frame(root)
frame.place(x=400,y=80)


box_list = tk.Listbox(frame,width=30,height=5)
box_list.pack(side='left',fill='y')

scroll = tk.Scrollbar(frame,orient='vertical',command=box_list.yview)
scroll.pack(side='right',fill='y')

box_list.config(yscrollcommand=scroll.set)
for itms in items:
    box_list.insert(tk.END,itms)




translate_button = tk.Button(root,text='''tr
ans
la
te''',width=3,height=10,command=show_selection)
translate_button.place(x=360,y=60)

root.bind("<Return>", lambda event: show_selection())
box_list.bind("<Key>",search_by_key)


root.mainloop()