from tkinter import *

window=Tk()

store=0
sum1=0
output=0

def Entered_Value(number):
    global store
    store=store*10 + number
    Displays.insert(END,number)

def show(operation):
    global sum1
    global store
    global operator
    Add["state"]=DISABLED
    Sub["state"]=DISABLED
    Mul["state"]=DISABLED
    Div["state"]=DISABLED
    operator = operation
    Displays.insert(END,operator)
    sum1=store
    store=0

def final():
    global sum1
    global store
    global operator
    global output
    if output!=0:
        sum1=sum1+output
    if operator=="+":
        output = sum1+store
    elif operator=="-":
        output = sum1-store
    elif operator=="*":
        output = sum1*store
    elif operator=="/":
        output = sum1/store
    store=0
    sum1=0
    Displays.delete(1.0,END)
    Displays.insert(END,output)
    Add["state"]=NORMAL
    Sub["state"]=NORMAL
    Mul["state"]=NORMAL
    Div["state"]=NORMAL

one=Button(window,text="1",width=4,command=lambda : Entered_Value(1))
one.grid(row=1,column=0)

two=Button(window,text="2",width=4,command=lambda : Entered_Value(2))
two.grid(row=1,column=1)

three=Button(window,text="3",width=4,command=lambda : Entered_Value(3))
three.grid(row=1,column=2)

four=Button(window,text="4",width=4,command=lambda : Entered_Value(4))
four.grid(row=2,column=0)

five=Button(window,text="5",width=4,command=lambda : Entered_Value(5))
five.grid(row=2,column=1)

six=Button(window,text="6",width=4,command=lambda : Entered_Value(6))
six.grid(row=2,column=2)

seven=Button(window,text="7",width=4,command=lambda : Entered_Value(7))
seven.grid(row=3,column=0)

eight=Button(window,text="8",width=4,command=lambda : Entered_Value(8))
eight.grid(row=3,column=1)

nine=Button(window,text="9",width=4,command=lambda : Entered_Value(9))
nine.grid(row=3,column=2)

zero=Button(window,text="0",width=4,command=lambda : Entered_Value(0))
zero.grid(row=4,column=0)

Add=Button(window,text="+",width=4,command=lambda : show("+"))
Add.grid(row=4,column=1)

Sub=Button(window,text="-",width=4,command=lambda : show("-"))
Sub.grid(row=4,column=2)

Mul=Button(window,text="*",width=4,command=lambda : show("*"))
Mul.grid(row=5,column=0)

Div=Button(window,text="/",width=4,command=lambda : show("/"))
Div.grid(row=5,column=1)

total=Button(window,text="=",width=4,command=final)
total.grid(row=5,column=2)


Displays=Text(window,height=1,width=20)
Displays.grid(row=0,column=0,columnspan=3)


window.mainloop()
