from tkinter import *

from _ast import Lambda
root=Tk()
root.maxsize(width=500, height=600)
root.minsize(width=500, height=600)
root.configure(bg='lavender')
root.title('Simple Calculator')
Label(root,text='SIMPLE CALCULATOR',font=('Arial bold',10),bg='lavender').grid(row=0,column=1)



e=Entry(root,width=15,borderwidth=5,font=('Arial bold',30))
e.grid(row=1,column=0,columnspan=3, padx=10,pady=10)


def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) +str(number))

def Button_num(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)



def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_square():
    global math
    global f_num
    first_number = e.get()
    f_num = int(first_number)
    math="square"
    current=e.get()
    e.delete(0, END)
    e.insert(0,int(current) ^ int(first_number))

def button_equal():
    global f_num
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "square":
        e.insert(0, f_num ** int(2))

def button_delete():
    current = e.get()
    lenght = len(current) - 1
    e.delete(lenght, END)

def button_exit():
    root.destroy()
Button(root,text="Remove",padx=30,pady=15,command=button_delete,border="4",bg='indianred').grid(row=1,column=3,)
b1=Button(root,text="1",padx=40,pady=20, command=lambda :button_click(1),border="4",bg='silver',)
b2=Button(root,text="2",padx=40,pady=20,command=lambda :button_click(2),border="4",bg='silver')
b3=Button(root,text="3",padx=40,pady=20,command=lambda :button_click(3),border="4",bg='silver')
b4=Button(root,text="4",padx=40,pady=20,command=lambda :button_click(4),border="4",bg='silver')
b5=Button(root,text="5",padx=40,pady=20,command=lambda :button_click(5),border="4",bg='silver')
b6=Button(root,text="6",padx=40,pady=20,command=lambda :button_click(6),border="4",bg='silver')
b7=Button(root,text="7",padx=40,pady=20,command=lambda :button_click(7),border="4",bg='silver')
b8=Button(root,text="8",padx=40,pady=20,command=lambda :button_click(8),border="4",bg='silver')
b9=Button(root,text="9",padx=40,pady=20,command=lambda :button_click(9),border="4",bg='silver')
b0=Button(root,text="0",padx=40,pady=20,command=lambda :button_click(0),border="4",bg='silver')
b_dot=Button(root,text='.',padx=40,pady=20,command=lambda:Button_num("."),border="4",)
b_add=Button(root,text="+",padx=39,pady=20,command=button_add,border="4",bg='lightblue')
b_sub=Button(root,text="-",padx=39,pady=20,command=button_sub,border="4",bg='lightblue')
b_mul=Button(root,text="x",padx=39,pady=20,command=button_mul,border="4",bg='lightblue')
b_div=Button(root,text="/",padx=39,pady=20,command=button_div,border="4",bg='lightblue')
b_square=Button(root,text="^",padx=40,pady=20,command=button_square,border="4",bg='lightblue')
b_equal=Button(root,text="=",padx=85,pady=20,command=button_equal,border="4",width=25,bg='linen')
b_clear=Button(root,text="Clear",padx=45,pady=20,command=button_clear,border="4",bg='indianred')
b_exit=Button(root,text="Exit",padx=45,pady=10,command=button_exit,border="4",bg='black',fg='white')

b1.grid(row=4,column=0,padx=5,pady=10)
b2.grid(row=4,column=1,padx=5,pady=10)
b3.grid(row=4,column=2,padx=5,pady=10)
b4.grid(row=3,column=0,padx=5,pady=10)
b5.grid(row=3,column=1,padx=5,pady=10)
b6.grid(row=3,column=2,padx=5,pady=10)
b7.grid(row=2,column=0,padx=5,pady=10)
b8.grid(row=2,column=1,padx=5,pady=10)
b9.grid(row=2,column=2,padx=5,pady=10)
b0.grid(row=5,column=1,padx=5,pady=10)
b_dot.grid(row=5,column=2,padx=5,pady=10)
b_add.grid(row=5,column=3)
b_sub.grid(row=4,column=3)
b_mul.grid(row=3,column=3)
b_div.grid(row=2,column=3)
b_square.grid(row=5,column=0)
b_equal.grid(row=6,column=0,columnspan=3)
b_clear.grid(row=6,column=3,)
b_exit.grid(row=7,column=1,columnspan=2,padx=5,pady=10)
root.mainloop()