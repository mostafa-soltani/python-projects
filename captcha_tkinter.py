import tkinter as tk
from tkinter import messagebox
from PIL import Image as PILImage
from PIL import ImageTk
from captcha.image import ImageCaptcha
import random

root = tk.Tk()
root.title('captcha')
root.geometry('400x300')

# مقدار کپچای فعلی را نگه می‌داریم
current_code = random.randint(1000, 999999)

captcha_gen = ImageCaptcha()

def generate_captcha_image(code):
    data = captcha_gen.generate(str(code))
    img = PILImage.open(data)
    return ImageTk.PhotoImage(img)

# اولین کپچا
tk_img = generate_captcha_image(current_code)

lbl = tk.Label(root, image=tk_img, bg="white")
lbl.image = tk_img
lbl.pack(pady=20)

captcha_entry = tk.Entry(root, width=50)
captcha_entry.place(x=50, y=100)
captcha_entry.bind('<Return>', lambda event: check())

def check():
    global current_code1, tk_img
    if captcha_entry.get() == str(current_code) or captcha_entry.get() == str(current_code1):
        messagebox.askokcancel('allright', 'correct!!!', icon='info')
    
        # تولید عدد جدید
        current_code1 = random.randint(1000, 999999)

        # ساخت عکس جدید
        tk_img = generate_captcha_image(current_code1)

        # آپدیت لیبل
        lbl.configure(image=tk_img)
        lbl.image = tk_img

        captcha_entry.delete(0, tk.END) 
    else:
        messagebox.showerror('error', 'incorrect')

def change_captcha():
    global current_code, tk_img

    # تولید عدد جدید
    current_code = random.randint(1000, 999999)

    # ساخت عکس جدید
    tk_img = generate_captcha_image(current_code)

    # آپدیت لیبل
    lbl.configure(image=tk_img)
    lbl.image = tk_img

    captcha_entry.delete(0, tk.END)  # پاک کردن ورودی

button = tk.Button(root, text='enter', fg='black', bg='white', command=check)
button.place(x=50, y=150)

button1 = tk.Button(root, text='change captcha', command=change_captcha)
button1.place(x=150, y=150)

root.mainloop()
