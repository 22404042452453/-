from tkinter import *

root = Tk()
root.title("Simple Calculator")
root['bg'] = 'blue'

e = Entry(root, width=40, borderwidth=3, bg='blue')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
e.insert(0, "Enter your numbers")


# first function
def buttom_add(number):
    curent = e.get()
    e.delete(0, END)
    e.insert(0, str(curent) + str(number))


# 2 funtion
def buttom_delete():
    e.delete(0, END)


# 3
def sum_buttom():
    first_number = e.get()
    global f_num
    global math
    math = '+'
    f_num = float(first_number)
    e.delete(0, END)


# 4
def minus_buttom():
    first_number = e.get()
    global f_num
    global math
    math = '-'
    f_num = float(first_number)
    e.delete(0, END)


# 5
def sqr_buttom():
    first_number = e.get()
    global f_num
    global math
    math = '*'
    f_num = float(first_number)
    e.delete(0, END)


def div_buttom():
    first_number = e.get()
    global f_num
    global math
    math = '/'
    f_num = float(first_number)
    e.delete(0, END)


def q_buttom():
    second_number = float(e.get())
    e.delete(0, END)
    if math == '+':
        e.insert(0, f_num + second_number)
    elif math == '-':
        e.insert(0, f_num - second_number)
    elif math == '*':
        e.insert(0, f_num * second_number)
    else:
        e.insert(0, f_num / second_number)


# my buttom
btn1 = Button(root, text='1', padx=30, pady=30, command=lambda: buttom_add(1))
btn2 = Button(root, text='2', padx=32, pady=30, command=lambda: buttom_add(2))
btn3 = Button(root, text='3', padx=30, pady=30, command=lambda: buttom_add(3))
btn4 = Button(root, text='4', padx=30, pady=30, command=lambda: buttom_add(4))
btn5 = Button(root, text='5', padx=32, pady=30, command=lambda: buttom_add(5))
btn6 = Button(root, text='6', padx=30, pady=30, command=lambda: buttom_add(6))
btn7 = Button(root, text='7', padx=30, pady=30, command=lambda: buttom_add(7))
btn8 = Button(root, text='8', padx=32, pady=30, command=lambda: buttom_add(8))
btn9 = Button(root, text='9', padx=30, pady=30, command=lambda: buttom_add(9))
btn0 = Button(root, text='0', padx=30, pady=30, command=lambda: buttom_add(0))
# function
btnq = Button(root, text='=', padx=29, pady=30, command=q_buttom)
btnsum = Button(root, text='+', padx=31, pady=30, command=sum_buttom)
btnmin = Button(root, text='-', padx=32, pady=30, command=minus_buttom)
btnsqr = Button(root, text='*', padx=32, pady=30, command=sqr_buttom)
btndiv = Button(root, text='/', padx=32, pady=30, command=div_buttom)
btndelete = Button(root, text='delete', padx=19, pady=30, command=buttom_delete)

# place of buttom
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)

btn0.grid(row=4, column=0)
btnsum.grid(row=1, column=3)
btnmin.grid(row=2, column=3)
btnsqr.grid(row=3, column=3)
btndiv.grid(row=4, column=3)
btndelete.grid(row=4, column=1)
btnq.grid(row=4, column=2)

root.mainloop()
