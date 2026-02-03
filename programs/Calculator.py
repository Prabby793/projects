from tkinter import *
from tkinter import font

def oper(num1,num2,operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/': 
        return num1 / num2
    elif operator == '=':
        return num1
    else:
        return num2
calculator = Tk()
title = calculator.title('Calculator')
num1 = 0
num2 = ''
operator = ''


def num(x):
    global num2
    global num1 
    global label1
    global operator
    if x == '+' or x == '-' or x == '*' or x == '/':
        num1 = oper(num1,float(num2),operator)
        operator = x
        num2 = ''
        label1 = Label(calculator, text =num1, padx = 50,pady = 50)
        label1.grid(row=0,column=3)
    elif x == '=':
        num1 = oper(num1,float(num2),operator)
        operator = ''
        num2 = num1
        label1 = Label(calculator, text = num1, padx = 50,pady = 50)
        label1.grid(row=0,column=3)
    else:
        num2 += str(x)
        label1 = Label(calculator, text = num2, padx=50,pady=50)
        label1.grid(row=0,column=3)



one = Button(text = '1', padx = 50, pady = 50, command = lambda: num(1))
two = Button(text = '2', padx=50, pady = 50, command =lambda: num(2))
three = Button(text = '3', padx=50, pady = 50, command =lambda: num(3))
four = Button(text = '4', padx=50, pady = 50, command =lambda: num(4))
five = Button(text = '5', padx=50, pady = 50, command = lambda:num(5))
six = Button(text = '6', padx=50, pady = 50, command =lambda: num(6))
seven = Button(text = '7', padx=50, pady = 50, command =lambda: num(7))
eight = Button(text = '8', padx=50, pady = 50, command =lambda: num(8))
nine = Button(text = '9', padx=50, pady = 50, command =lambda: num(9))
zero = Button(text = '0', padx = 50, pady = 50, command =lambda: num(0))
plus = Button(calculator, text = '+', padx = 50, pady = 50, command =lambda: num('+'))
minus = Button(calculator, text = '-',padx = 50, pady = 50, command =lambda: num("-"))
multiply = Button(calculator, text = '*',padx = 50, pady = 50, command =lambda: num('*'))
divide = Button (calculator, text = '/',padx = 50, pady = 50, command =lambda: num('/'))
zero1 = Button(calculator, text = ' ',padx = 50, pady = 50, command = lambda: num(0))
zero2 = Button(calculator, text = '.',padx = 50, pady = 50, command = lambda: num('.'))
equal = Button(calculator, text = '=', padx = 50,pady = 50, command = lambda: num('='))

one.grid(row = 1,column=0)
two.grid(row=1,column=1)
three.grid(row=1,column=2)
four.grid(row=2,column=0)
five.grid(row=2,column = 1)
six.grid(row=2,column=2)
seven.grid(row=3,column=0)
eight.grid(row=3,column=1)
nine.grid(row=3,column=2)
zero1.grid(row=4,column=0)
zero.grid(row=4,column=1)
zero2.grid(row=4,column=2)
plus.grid(row=1,column=3)
minus.grid(row=2,column=3)
multiply.grid(row=3,column=3)
divide.grid(row=4,column=3)
equal.grid(row=5,column=3)

mainloop()
