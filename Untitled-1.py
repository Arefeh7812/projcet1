from tkinter import*
from tkinter import messagebox
import database1
win=Tk()
win.geometry("600x400")
win.title("Login Form")
db=database1.Database('d:/Arefeh malk abady/database.db')
###########funcoin#######
def Clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_password.delete(0,END)
    ent_fname.focus_set()

def siginUp():
    fname=ent_fname.get()
    lname=ent_lname.get()
    email=ent_email.get()
    password=ent_password.get()
    if email=="" or password=="":
        messagebox.showerror("error","email and password are empty")
        return
    else:
        data=db.find_users(email,password)
        if data:
             messagebox.showinfo("welcome"f"{data[0]} {data[1]},welcome")
             Clear()
        else:
            messagebox.showerror("error","invalid email or password")

        







lbl_fname=Label(win,text="fname:",font=("bell MT",14))
lbl_fname.place(x=80,y=40)
ent_fname=Entry(win,font=("Bell MT",14))
ent_fname.place(x=140,y=40)

lbl_lname=Label(win,text="lname:",font=("bell MT",14))
lbl_lname.place(x=80,y=80)
ent_lname=Entry(win,font=("Bell MT", 14))
ent_lname.place(x=140,y=80)

lbl_email=Label(win,text="*email:",font=("Bell MT",14))
lbl_email.place(x=80,y=150)
ent_email=Entry(win,font=("Bell MT",14))
ent_email.place(x=140,y=150)

lbl_password=Label(win,text="*password:",font=("Bell MT",14))
lbl_password.place(x=65,y=200)
ent_password=Entry(win,font=("Bell MT",14))
ent_password.place(x=160,y=200)

btn_signUp=Button(win,text="signUp",font=("Bell MT",14))
btn_signUp.place(x=120,y=300)

btn_signIn=Button(win,text="signIN",font=("Bell MT",14))
btn_signIn.place(x=240,y=300)





























win.mainloop()