import random
import string
import pyperclip
from tkinter import *
import tkinter.ttk

def creating_pass():
	gen_pass.set("")
	length = var1.get()
	special = " #@!^%&*?> "
	password = ""
	if var.get() == 1:
		password = ''.join([random.choice(string.ascii_lowercase + string.digits) for i in range(length)])
		return password

	elif var.get() == 2:
		password = ''.join([random.choice(string.ascii_uppercase + string.digits) for i in range(length)])
		return password

	elif var.get() == 3:
		password = ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + special) for n in range(length)])
		return password
	else:
		pass


#  generation of password
def generate():
	p = creating_pass()
	gen_pass.set(p)


# copying password to clipboard
def copy():
	generate_password = gen_pass.get()
	pyperclip.copy(generate_password)




"""
   
                                                             GUI window start here
"""
root = Tk()
var = IntVar()
var1 = IntVar()
root.geometry("650x265")
root.resizable(width=False ,height=False)
root.configure(background='#74B9FF')
root.title("Password Maker")

gen_pass = StringVar()


Label(root, text="Password", font="sans-serif",bg="#74B9FF").place(x=20, y=40, height=30)
Entry(root, textvariable=gen_pass, width=35,).place(x=110, y=40, height=30)


Label(root, text="Length",  font="sans-serif", bg="#74B9FF").place(x=20, y=90, height=30)

Button(root, text="Copy", bg="#45CE30", activebackground="#45CE30", font="sans-serif", command=lambda: copy()).place(x=420, y=40)
Button(root, text="Generate", bg="#45CE30", activebackground="#45CE30", font="sans-serif", command=lambda: generate()).place(x=520, y=40)


Label(root, text="Choose Level",  font="sans-serif", bg="#74B9FF").place(x=20, y=150, height=30)
Radiobutton(root, text="Low", variable=var, value=1, bg="#74B9FF", activebackground="#74B9FF", font="sans-serif", offrelief="ridge").place(x=160, y=150, height=30)
Radiobutton(root, text="Medium", variable=var, bg="#74B9FF", activebackground="#74B9FF", value=2, font="sans-serif", offrelief="ridge").place(x=250, y=150, height=30)
Radiobutton(root, text="Strong", variable=var, value=3, bg="#74B9FF", activebackground="#74B9FF",  font="sans-serif", offrelief="ridge").place(x=370, y=150, height=30)


combo = tkinter.ttk.Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21, 22, 23, 24, 25)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=110, y=90, height=30)


root.mainloop()
