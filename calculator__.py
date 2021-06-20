from tkinter import *
root = Tk()
root.geometry('360x480')
root.title('calculator')
root.resizable(0,0)
root.configure(background='navy')
a = StringVar()

def show(c):
    a.set(a.get()+c)
def clr():
    a.set("")
def execute():
    a.set(eval(a.get()))
def deleteLast():
    a.set(a.get()[:-1])

frame = Entry(root,font=('Algerian',25),justify='right',textvariable=a,relief=SUNKEN,bd='5')
frame.place(x='0',y='0',width=360,height=70)
a.set(0)

b1 = Button(text='AC',font=('',30))
b1.place(x='5',y='80',width=80,height=70)
b1.configure(command=clr)

b2 = Button(text='/',font=('',30))
b2.place(x='90',y='80',width=80,height=70)
b2.configure(command=lambda:show('/'))

b3 = Button(text='x',font=('',30))
b3.place(x='180',y='80',width=80,height=70)
b3.configure(command=lambda:show("*"))

b4 = Button(text='delete',font=('',20),bg='red')
b4.place(x='270',y='80',width=80,height=70)
b4.configure(command=deleteLast)

b5 = Button(text='7',font=('',30))
b5.place(x='5',y='160',width=80,height=70)
b5.configure(command=lambda:show("7"))

b6 = Button(text='8',font=('',30))
b6.place(x='90',y='160',width=80,height=70)
b6.configure(command=lambda:show("8"))

b7 = Button(text='9',font=('',30))
b7.place(x='180',y='160',width=80,height=70)
b7.configure(command=lambda:show("9"))

b8 = Button(text='+',font=('',30))
b8.place(x='270',y='160',width=80,height=70)
b8.configure(command=lambda:show("+"))

b9 = Button(text='4',font=('',30))
b9.place(x='5',y='240',width=80,height=70)
b9.configure(command=lambda:show("4"))

b10 = Button(text='5',font=('',30))
b10.place(x='90',y='240',width=80,height=70)
b10.configure(command=lambda:show("5"))

b11 = Button(text='6',font=('',30))
b11.place(x='180',y='240',width=80,height=70)
b11.configure(command=lambda:show("6"))

b12 = Button(text='-',font=('',30))
b12.place(x='270',y='240',width=80,height=70)
b12.configure(command=lambda:show("-"))

b13 = Button(text='1',font=('',30))
b13.place(x='5',y='320',width=80,height=70)
b13.configure(command=lambda:show("1"))

b14 = Button(text='2',font=('',30))
b14.place(x='90',y='320',width=80,height=70)
b14.configure(command=lambda:show("2"))

b15 = Button(text='3',font=('',30))
b15.place(x='180',y='320',width=80,height=70)
b15.configure(command=lambda:show("3"))

b16 = Button(text='=',font=('',30))
b16.place(x='270',y='320',width=80,height=150)
b16.configure(command=execute)

b17 = Button(text='0',font=('',30))
b17.place(x='5',y='400',width=160,height=70)
b17.configure(command=lambda:show("0"))

b18 = Button(text='.',font=('',30))
b18.place(x='180',y='400',width=80,height=70)
b18.configure(command=lambda:show("."))

root.mainloop()