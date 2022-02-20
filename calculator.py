#потрачино 8 часов верніть їх будь ласка
from tkinter import*
from math import*
tk=Tk()
tk.geometry("260x370")
img=PhotoImage(file='radical.png')
Radical=Button(image=img)
#текстове поле
ent = Entry(justify="right",font="14")
ent.place(x=20, y=20, width=220, height=30)
#0 
def B0_click() :
    ent.insert(END, "0")
B0=Button(text="0",font="14",command=B0_click)
B0.place(x=20, y=310, width=100, height=40)
#1
def B1_click() :
    ent.insert(END, "1")
B1=Button(text="1",font="14",command=B1_click)
B1.place(x=20, y=250, width=40, height=40)
#2
def B2_click() :
    ent.insert(END, "2")
B2=Button(text="2",font="14",command=B2_click)
B2.place(x=80, y=250, width=40, height=40)
#3
def B3_click() :
    ent.insert(END, "3")
B3=Button(text="3",font="14",command=B3_click)
B3.place(x=140, y=250, width=40, height=40)
#4
def B4_click() :
    ent.insert(END, "4")
B4=Button(text="4",font="14",command=B4_click)
B4.place(x=20, y=200, width=40, height=40)
#5
def B5_click() :
    ent.insert(END, "5")
B5=Button(text="5",font="14",command=B5_click)
B5.place(x=80, y=200, width=40, height=40)
#6
def B6_click() :
    ent.insert(END, "6")
B6=Button(text="6",font="14",command=B6_click)
B6.place(x=140, y=200, width=40, height=40)
#7
def B7_click() :
    ent.insert(END, "7")
B7=Button(text="7",font="14",command=B7_click)
B7.place(x=20, y=150, width=40, height=40)
#8
def B8_click() :
    ent.insert(END, "8")
B8_click=Button(text="8",font="14",command=B8_click)
B8_click.place(x=80, y=150, width=40, height=40)
#9
def B9_click() :
    ent.insert(END, "9")
B9=Button(text="9",font="14",command=B9_click)
B9.place(x=140, y=150, width=40, height=40)
#C
def BC_click() :
    ent.delete(0,END)
BC=Button(text="C",font="14",command=BC_click)
BC.place(x=20, y=100, width=40, height=40)
#PLUS
def Plus_click():
    global a,b
    a=float(ent.get())
    b="+"
    ent.insert(END,"+")
    ent.delete(0,END)
plus=Button(text="+",font="14",command=Plus_click)
plus.place(x=200, y=310, width=40, height=40)
#MIN
def Min_click():
    global a,b
    a=float(ent.get())
    b="-"
    ent.insert(END, "-")
    ent.delete(0,END)
min=Button(text="-",font="14",command=Min_click)
min.place(x=200, y=250, width=40, height=40)
#Multi
def Multi_click() :
    global a,b
    a=float(ent.get())
    b="*"
    ent.insert(END, "*")
    ent.delete(0,END)
Multi=Button(text="*",font="14",command=Multi_click)
Multi.place(x=200, y=200, width=40, height=40)
#Division
def Division_click():
    global a,b
    a=float(ent.get())
    b="/"
    ent.insert(END, "/")
    ent.delete(0,END)
division=Button(text="/",font="14",command=Division_click)
division.place(x=200, y=150, width=40, height=40)
#Equal
def Equal_click():
    global a,b
    c=float(ent.get())
    ent.delete(0,END)
    if b=="+":
       a=a+c
       ent.insert(END,a)
    if b=="-":
       a=a-c
       ent.insert(END,a)
    if b=="*":
       a=a*c
       ent.insert(END,a)
    if b=="/":
        if c!=0:
            a=a/c
            ent.insert(END,a)
        else:
            ent.insert(END,"помилка")
Equal=Button(text="=",font="14",command=Equal_click)
Equal.place(x=200, y=100, width=40, height=40)
#Radical
def Radical_click() :
    global c
    a=float(ent.get())
    ent.delete(0,END)
    if a>=0:
        c=sqrt(a)
        ent.insert(END, c)
    else:
        ent.insert(0, "ПОМИЛКА")
img=PhotoImage(file='radical.png')
Radical=Button(image=img,command=Radical_click)
Radical.place(x=80, y=100, width=40, height=40)
#Modul
def Modul_click() :
    global c
    a=float(ent.get())
    ent.delete(0,END)
    c=abs(a)
    ent.insert(END, c)
Modul=Button(text="|x|",font="14",command=Modul_click)
Modul.place(x=140, y=100, width=40, height=40)
#.
def B11_click() :
    ent.insert(END, ".")
B11=Button(text=".",font="14",command=B11_click)
B11.place(x=140, y=310, width=40, height=40)
