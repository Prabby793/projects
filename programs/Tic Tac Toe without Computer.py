from tkinter import *
from tkinter import font
import random
import time
tk = Tk()
title = tk.title('Tic Tac Toe')
custom_font = font.Font(size = 25)
crusty_font = font.Font(size = 50)
r = 1
g ={1:'0',2:'0',3:'0',4:'0',5:'0',6:'0',7:'0',8:'0',9:'0'}
def my_click(y,x,z):
    global g
    global r
    if r % 2 == 1:
        if g[z] == '0':
            my_label = Label(tk, text = 'X',padx=130,pady=130,font=custom_font, bg = 'yellow')
            my_label.grid(row=y,column=x)
            g[z] = 'X'
    else:
        if g[z] == '0':
            my_label30 = Label(tk, text = 'O',padx=130,pady=130,font=custom_font, bg = 'yellow')
            my_label30.grid(row=y,column=x)
        g[z] = 'O'
    r+=1
def game_over():
    global g
    win = None
    ci = []
    for n in g:
        ler = g[n]
        ci.append(str(ler))
    li = "".join(ci)
    if li[0:3]=='XXX':
        win = 'X'
    elif li[0:3] == "OOO":
        win = 'O'
    elif li[3:6]=='XXX' :
        win = 'X'
    elif li[3:6] == 'OOO':
        win = 'O'
    elif li[6:9] == 'XXX':
        win = 'X'
    elif li[6:9] == 'OOO':
        win = 'O'
    elif li[0:7:3] == "XXX":
        win = 'X'
    elif li[0:7:3] == 'OOO':
        win = 'O'
    elif li[1:8:3] == 'XXX':
        win = 'X'
    elif li[1:8:3] == 'OOO':
        win = 'O'
    elif li[2:9:3] == 'XXX':
        win = 'X'
    elif li[2:9:3] == 'OOO':
        win = 'O'
    elif li[0:9:4] == 'XXX':
        win = 'X'
    elif li[0:9:4] == 'OOO':
        win = 'O'
    elif li[2:7:2] == 'XXX':
        win = 'X'
    elif li[2:7:2] == 'OOO':
        win = 'O'
    if win == 'O':
        Label10 = Label(tk, text = 'O won!',padx=300, pady=300)
        Label10.grid(row=2,column=1)
        ri = False
    elif win == 'X':
        label11 = Label(tk, text = 'X won!',padx = 300, pady = 300)
        label11.grid(row=2,column=1)
        ri = False
win = None
def game():
    global my_label1,my_label2,my_label3,my_label4,my_label5,my_label6,my_label7,my_label8,my_label9,ri
    global ge
    global we
    global tk    
    
    if we.get().lower() == 'yes':
        we.destroy()
        ge.destroy()
        label = Label(tk, text = 'Tic Tac Toe')
        my_label1 = Button(tk, text = " ",command = lambda: my_click(1,0,1)+game_over(), padx=150,pady=150, bg = 'yellow').grid(row=1, column=0 )
        my_label2 = Button(tk, text = " ", command = lambda: my_click(1,1,2)+game_over, padx=150,pady=150, bg = 'yellow').grid(row=1,column=1)
        my_label3= Button(tk, text = " ",command = lambda: my_click(1,2,3)+game_over(), padx=150,pady=150, bg = 'yellow').grid(row=1,column=2)
        my_label4 = Button(tk, text = " ",command = lambda: my_click(2,0,4)+game_over(), padx=150,pady=150,bg = 'yellow').grid(row=2,column=0)
        my_label5 = Button(tk, text = " ", command = lambda: my_click(2,1,5)+game_over(), padx=150,pady=150, bg = 'yellow').grid(row=2,column=1)
        my_label6= Button(tk, text = " ",command = lambda: my_click(2,2,6)+game_over(), padx=150,pady=150, bg = 'yellow').grid(row=2,column=2)
        my_label7 = Button(tk, text = " ",command = lambda: my_click(3,0,7)+game_over(), padx=150,pady=150, bg = 'yellow').grid(row=3)
        my_label8 = Button(tk, text = " ", command = lambda: my_click(3,1,8)+game_over(), padx=150,pady=150, bg = 'yellow').grid(row=3,column=1)
        my_label9= Button(tk, text = " ",command = lambda: my_click(3,2,9)+game_over(), padx=150,pady=150, bg = 'yellow').grid(row=3,column=2)
        label.grid(row=0,column=1)
    

we = Entry(tk, borderwidth = 10,font=crusty_font)
we.grid()
ge = Button(tk, text = 'Tic Tac Toe?', command =game,borderwidth = 5,padx=50,pady=50)
ge.grid(row=1)
tk.mainloop()

