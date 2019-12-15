from tkinter import *
from decimal import *


root = Tk()
root.title("Calculator")
root.minsize(285, 292)
root.maxsize(285, 292)

e = Entry(root, width=30)
e.place(height=30)
e.insert(0, 0)
e.grid(row = 0, column = 0, columnspan=4, padx=1, pady=1)

def button_click(num):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
    #return

def button_clear():
    e.delete(0, END)

def button_add():
    fnum = e.get()
    global f_num
    global math
    math = "addition"
    f_num = Decimal(fnum)
    e.delete(0, END)


def button_sub():
    fnum = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = Decimal(fnum)
    e.delete(0, END)

def button_mul():
    fnum = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = Decimal(fnum)
    e.delete(0, END)

def button_div():
    fnum = e.get()
    global f_num
    global math
    math = "division"
    f_num = Decimal(fnum)
    e.delete(0, END)

def button_decimal():
    decimal = e.get() + "".join(".")
    e.delete(0, END)
    e.insert(0, decimal)

def button_mod():
    fnum = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = Decimal(fnum)
    e.delete(0, END)

def button_del():
    delete = e.get()
    e.delete(0, END)
    e.insert(0, delete[:-1])

def button_neg():
    neg = e.get()
    e.delete(0, END)
    e.insert(0, Decimal(neg) * -1)

def button_equal():
    snum = e.get()
    if snum == "":
        snum = 0
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + Decimal(snum))

    if math == "subtraction":
        e.insert(0, f_num - Decimal(snum))

    if math == "multiplication":
        e.insert(0, f_num * Decimal(snum))

    if math == "division":
        try:
            e.insert(0, f_num / Decimal(snum))
        except:
            e.insert(0, "Not Defined!")

    if math == "modulus":
        e.insert(0, f_num % Decimal(snum))

#Defining Buttons
button_1 = Button(root, text="1", width = 7, height = 3, command=lambda: button_click(1))
button_2 = Button(root, text="2", width = 7, height = 3, command=lambda: button_click(2))
button_3 = Button(root, text="3", width = 7, height = 3, command=lambda: button_click(3))
button_4 = Button(root, text="4", width = 7, height = 3, command=lambda: button_click(4))
button_5 = Button(root, text="5", width = 7, height = 3, command=lambda: button_click(5))
button_6 = Button(root, text="6", width = 7, height = 3, command=lambda: button_click(6))
button_7 = Button(root, text="7", width = 7, height = 3, command=lambda: button_click(7))
button_8 = Button(root, text="8", width = 7, height = 3, command=lambda: button_click(8))
button_9 = Button(root, text="9", width = 7, height = 3, command=lambda: button_click(9))
button_0 = Button(root, text="0", width = 7, height = 3, command=lambda: button_click(0))

#Defining Operators
button_add = Button(root, text="+", fg="blue", width = 7, height = 3, command=button_add)
button_sub = Button(root, text="-", fg="blue", width = 7, height = 3, command=button_sub)
button_mul = Button(root, text="*", fg="blue", width = 7, height = 3, command=button_mul)
button_div = Button(root, text="/", fg="blue", width = 7, height = 3, command=button_div)
button_equal = Button(root, text="=", fg="blue", width = 7, height = 3, command=button_equal)
button_clear = Button(root, text="AC", fg="blue", width = 7, height = 3, command=button_clear)
button_decimal = Button(root, text=".", fg="blue", width = 7, height = 3, command=button_decimal)
button_negate = Button(root, text="+/-", fg="blue", width = 7, height = 3, command=button_neg)
button_mod = Button(root, text="%", fg="blue", width = 7, height = 3,  command=button_mod)
button_del = Button(root, text="Del", fg="blue", width = 7, height = 3,  command=button_del)

#Configuring buttons


#Defining Layout
button_clear.grid(row = 1, column=0)
button_negate.grid(row = 1, column=1)
button_mod.grid(row = 1, column=2)

button_7.grid(row = 2, column=0)
button_8.grid(row = 2, column=1)
button_9.grid(row = 2, column=2)

button_4.grid(row = 3, column=0)
button_5.grid(row = 3, column=1)
button_6.grid(row = 3, column=2)

button_1.grid(row = 4, column=0)
button_2.grid(row = 4, column=1)
button_3.grid(row = 4, column=2)

button_0.grid(row = 5, column=0)
button_decimal.grid(row = 5, column=1)
button_del.grid(row = 5, column=2)

button_add.grid(row = 1, column=3)
button_sub.grid(row = 2, column=3)
button_mul.grid(row = 3, column=3)
button_div.grid(row = 4, column=3)
button_equal.grid(row = 5, column=3)

root.mainloop()