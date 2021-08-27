from tkinter import *
import random as r

root = Tk()
root.title("Simple generator of password")
root['bg'] = 'blue'
e = Entry(root, width=50, borderwidth=3, bg='green')
e.grid(row=1, column=1, pady=10)

ser = IntVar()
ser1 = IntVar()
ser2 = IntVar()

checkbutton_lowercase_letters = Checkbutton(text="lowercase_letters/without", padx=10, pady=10, variable=ser)
checkbutton_lowercase_letters.grid(row=2, column=1)
checkbutton_uppercase_letters = Checkbutton(text="uppercase_letters/without", padx=9, pady=10, variable=ser1)
checkbutton_uppercase_letters.grid(row=3, column=1)
punctuation_letters = Checkbutton(text="punctuation/without", padx=22, pady=10, variable=ser2)
punctuation_letters.grid(row=4, column=1)


def generator_password(n=10):
    e.delete(0, END)
    digits = list('1234567890')
    lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    punctuation = list('!#$%&*+-=?@^_')
    if ser.get() == 1 and ser1.get() == 1 and ser2.get() == 1:
        e.insert(0, ''.join(r.sample(digits + lowercase_letters + uppercase_letters + punctuation, n)))
    elif ser.get() == 1 and ser1.get() == 1 and ser2.get() == 0:
        e.insert(0, ''.join(r.sample(digits + lowercase_letters + uppercase_letters, n)))
    elif ser.get() == 1 and ser1.get() == 0 and ser2.get() == 0:
        e.insert(0, ''.join(r.sample(digits + lowercase_letters, n)))
    elif ser.get() == 0 and ser1.get() == 0 and ser2.get() == 1:
        e.insert(0, ''.join(r.sample(digits + punctuation, n)))
    elif ser.get() == 0 and ser1.get() == 1 and ser2.get() == 1:
        e.insert(0, ''.join(r.sample(digits + punctuation + uppercase_letters, n)))
    elif ser.get() == 1 and ser1.get() == 0 and ser2.get() == 1:
        e.insert(0, ''.join(r.sample(digits + punctuation + lowercase_letters, n)))
    elif ser.get() == 0 and ser1.get() == 1 and ser2.get() == 0:
        e.insert(0, ''.join(r.sample(digits + uppercase_letters, n)))
    else:
        e.insert(0, ''.join(r.sample(digits, n)))


def save_password():
    text = e.get()
    with open("your_password.txt", "w") as f:
        f.write(text)


btn1 = Button(text='Cгенерировать', padx=10, pady=10, command=generator_password)
btn1.grid(row=6, column=0)
btn2 = Button(text='Сохранить пароль', padx=10, pady=10, command=save_password)
btn2.grid(row=6, column=2)

root.mainloop()
