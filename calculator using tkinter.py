#simple addition cal
from tkinter import *
s=Tk()
s.title('sample additon calculator')
e=Entry(s,width=40,borderwidth=5,fg='blue')
e.pack()
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def myclick(num):
    cu=e.get()
    e.delete(0,END)
    e.insert(0,str(cu)+str(num))
def add():
    t=e.get()
    global a,c
    a=int(t)
    c='add'
    e.delete(0,END)
def sub():
    t=e.get()
    global a,c
    a=int(t)
    c='sub'
    e.delete(0,END)
def mul():
    t=e.get()
    global a,c
    a=int(t)
    c='mul'
    e.delete(0,END)

def div():
    t=e.get()
    global a,c
    a=int(t)
    c='div'
    e.delete(0,END)
def square():
    t=e.get()
    global a,c
    a=int(t)
    c='square'
    #e.delete(0,END)
def cube():
    t=e.get()
    global a,c
    a=int(t)
    c='cube'
    #e.delete(0,END)

def equalto():
    if c!='square' or c!='cube':
        b=e.get()
        e.delete(0,END)
    if c=='add':
        e.insert(0,int(a)+int(b))
    if c=='sub':
        e.insert(0,int(a)-int(b))
    if c=='mul':
        e.insert(0,int(a)*int(b))
    if c=='div':
        e.insert(0,int(a)+int(b))
    if c=='square':
        e.delete(0,END)
        e.insert(0,int(a)**2)
    if c=='cube':
        e.delete(0,END)
        e.insert(0,int(a)**3)
        
def clear():
    e.delete(0,END)
    
b1=Button(s,text='1',padx=40,pady=20,command=lambda:myclick(1),fg='blue').grid(row=4,column=0)
b2=Button(s,text='2',padx=40,pady=20,command=lambda:myclick(2),fg='blue').grid(row=4,column=1)
b3=Button(s,text='3',padx=40,pady=20,command=lambda:myclick(3),fg='blue').grid(row=4,column=2)
b4=Button(s,text='4',padx=40,pady=20,command=lambda:myclick(4),fg='blue').grid(row=3,column=0)
b5=Button(s,text='5',padx=40,pady=20,command=lambda:myclick(5),fg='blue').grid(row=3,column=1)
b6=Button(s,text='6',padx=40,pady=20,command=lambda:myclick(6),fg='blue').grid(row=3,column=2)
b7=Button(s,text='7',padx=40,pady=20,command=lambda:myclick(7),fg='blue').grid(row=2,column=0)
b8=Button(s,text='8',padx=40,pady=20,command=lambda:myclick(8),fg='blue').grid(row=2,column=1)
b9=Button(s,text='9',padx=40,pady=20,command=lambda:myclick(9),fg='blue').grid(row=2,column=2)
b10=Button(s,text='0',padx=40,pady=20,command=lambda:myclick(0),fg='blue').grid(row=1,column=0)
b11=Button(s,text='+',padx=40,pady=20,command=add,fg='blue').grid(row=1,column=1)
b12=Button(s,text='-',padx=40,pady=20,command=sub,fg='blue').grid(row=1,column=2)
b13=Button(s,text='*',padx=50,pady=20,command=mul,fg='blue').grid(row=1,column=3)
b14=Button(s,text='/',padx=50,pady=20,command=div,fg='blue').grid(row=3,column=3)
b15=Button(s,text='X^2',padx=43,pady=20,command=square,fg='blue').grid(row=2,column=3)
b16=Button(s,text='X^3',padx=43,pady=20,command=cube,fg='blue').grid(row=4,column=3)
b17=Button(s,text='clear',padx=80,pady=20,command=clear,fg='blue').grid(row=5,column=0,columnspan=2)
b18=Button(s,text='=',padx=100,pady=20,command=equalto,fg='blue').grid(row=5,column=2,columnspan=2)
s.mainloop()
