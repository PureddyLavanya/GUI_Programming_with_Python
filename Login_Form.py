import tkinter as k
from tkinter import *
from tkinter import messagebox,Text
def login():
    uname=e1.get(1.0,"end-1c")
    psw=e2.get(1.0,"end-1c")

    if (uname=="" or psw==""):
        messagebox.showinfo("Error","User Name And Password shouldnot be empty")
    elif (uname=="Lavanya" and psw=="Lavanya@p123"):
        messagebox.showinfo("Correct","Login Success")
        t.destroy()
    else:
        messagebox.showinfo('Error',"Incorrect User Name Or Password")

    
t=k.Tk()
t.title('LOGIN FORM')
t.geometry('700x700')
t.configure(bg='ivory')
global e1
global e2
l1=k.Label(t,text="User Name",font=('Arial',18),bg='pink')
l1.place(x=60,y=140)
e1=k.Text(t,width="40",bg='skyblue',height="2",font=('Arial',14))
e1.place(x=195,y=140)
l2=k.Label(t,text="Password",font=('Arial',18),bg='pink')
e2=k.Text(t,width="40",bg='skyblue',height="2",font=('Arial',14))
l2.place(x=60,y=220)
e2.place(x=195,y=220)
Button(t,text="Login",width=15,height=2,command=login,bg='red',font=('Arial',16)).place(x=270,y=350)
t.mainloop()
