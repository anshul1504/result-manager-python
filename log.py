from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
 
t=Tk()
t.title("Student manger")
t.resizable(0,0)
w=700
h=600
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))
f55=None


def logout(n):
    f8=Frame(bg="pink")
    f8.pack()
    n.add(f8,text="Logout")

def delete(n):
    f7=Frame(bg="black")
    f7.pack()
    n.add(f7,text="Delete")
    d1=StringVar()
    u6=Label(f7,text="EnRoll",font=("",15),bg="cyan",fg="black")
    u6.place(x=130,y=80,width=100,height=25)
    e1=Entry(f7,font=("",15),textvariable=d1)
    e1.place(x=260,y=80,width=200,height=25)
    def de1():
        import sqlite3
        db=sqlite3.connect("regis.db")
        cr=db.cursor()
        cr.execute("delete from ins where EnRoll='"+d1.get()+"'")
        db.commit()
        db.close()
        show1(f55)
        messagebox.showinfo("Delete","Sucess")
        d1.set("")
        
        
    b1=Button(f7,text="Delete",font=("",15),bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=de1)
    b1.place(x=497,y=80,width=130,height=25)
    

def update(n):
    f6=Frame(bg="black")
    f6.pack()
    n.add(f6,text="Update")
    s1=StringVar()
    u6=Label(f6,text="EnRoll",font=("",15),bg="cyan",fg="black")
    u6.place(x=130,y=80,width=100,height=25)
    e1=Entry(f6,font=("",15),textvariable=s1)
    e1.place(x=260,y=80,width=200,height=25)
    def update1():
        import sqlite3
        db=sqlite3.connect("regis.db")
        cr=db.cursor()
        r=cr.execute("select * from ins where EnRoll='"+s1.get()+"'")
        
        for r1 in r:
            s2=StringVar()
            s3=StringVar()
            s4=StringVar()
            s5=StringVar()
            s6=StringVar()
   
            u2=Label(f6,text="Control",font=("",15),bg="cyan",fg="black")
            u2.place(x=240,y=150,width=90,height=25)
            u3=Entry(f6,font=("",15),textvariable=s2)
            u3.insert(0,r1[1])
            u3.place(x=380,y=150,width=90,height=25)
            u4=Label(f6,text="Dastr",font=("",15),bg="cyan",fg="black")
            u4.place(x=240,y=200,width=90,height=25)
            u5=Entry(f6,font=("",15),textvariable=s3)
            u5.insert(0,r1[2])
            u5.place(x=380,y=200,width=90,height=25)
            u6=Label(f6,text="LIC",font=("",15),bg="cyan",fg="black")
            u6.place(x=240,y=250,width=90,height=25)
            u7=Entry(f6,font=("",15),textvariable=s4)
            u7.insert(0,r1[3])
            u7.place(x=380,y=250,width=90,height=25)
            u8=Label(f6,text="Sensor",font=("",15),bg="cyan",fg="black")
            u8.place(x=240,y=300,width=90,height=25)
            u9=Entry(f6,font=("",15),textvariable=s5)
            u9.insert(0,r1[4])
            u9.place(x=380,y=300,width=90,height=25)
            u10=Label(f6,text="Digital",font=("",15),bg="cyan",fg="black")
            u10.place(x=240,y=350,width=90,height=25)
            u11=Entry(f6,font=("",15),textvariable=s6)
            u11.insert(0,r1[5])
            u11.place(x=380,y=350,width=90,height=25)
            def update2():
                db=sqlite3.connect("regis.db")
                cr=db.cursor()
                cr.execute("update ins set Control='"+s2.get()+"',Dastr='"+s3.get()+"',Ulic='"+s4.get()+"',Sensor='"+s5.get()+"',Digital='"+s6.get()+"' where EnRoll='"+s1.get()+"'")
                db.commit()
                db.close()
                show1(f55)
                messagebox.showinfo("Update","Sucess")
                s2.set("")
                s3.set("")
                s4.set("")
                s5.set("")
                s6.set("")
            
            
            b1=Button(f6,text="Update",font=("",15),bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=update2)
            b1.place(x=280,y=400,width=130,height=25)
            
            break
            
        else:
            f10=Frame(bg="black")
            f10.place(x=0,y=140,width=700,height=600)
            
            messagebox.showinfo("EnRoll","Not Found")
            
        db.commit()
        db.close()
    
    
    b1=Button(f6,text="Update",font=("",15),bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=update1)
    b1.place(x=497,y=80,width=130,height=25)




def search(n):
    f5=Frame(bg="black")
    f5.pack()
    n.add(f5,text="Search")
    s1=StringVar()
    u6=Label(f5,text="EnRoll",font=("",15),bg="cyan",fg="black")
    u6.place(x=130,y=80,width=100,height=25)
    e1=Entry(f5,font=("",15),textvariable=s1)
    e1.place(x=260,y=80,width=200,height=25)
    
    def search1():
        import sqlite3
        db=sqlite3.connect("regis.db")
        cr=db.cursor()
        r=cr.execute("select * from ins where EnRoll='"+s1.get()+"'")
        
        for r1 in r:
            u2=Label(f5,text="Control",font=("",15),bg="cyan",fg="black")
            u2.place(x=240,y=150,width=90,height=25)
            u3=Label(f5,text=r1[1],font=("",15),bg="gold",fg="black")
            u3.place(x=380,y=150,width=90,height=25)
            u4=Label(f5,text="Dastr",font=("",15),bg="cyan",fg="black")
            u4.place(x=240,y=200,width=90,height=25)
            u5=Label(f5,text=r1[2],font=("",15),bg="gold",fg="black")
            u5.place(x=380,y=200,width=90,height=25)
            u6=Label(f5,text="LIC",font=("",15),bg="cyan",fg="black")
            u6.place(x=240,y=250,width=90,height=25)
            u7=Label(f5,text=r1[3],font=("",15),bg="gold",fg="black")
            u7.place(x=380,y=250,width=90,height=25)
            u8=Label(f5,text="Sensor",font=("",15),bg="cyan",fg="black")
            u8.place(x=240,y=300,width=90,height=25)
            u9=Label(f5,text=r1[4],font=("",15),bg="gold",fg="black")
            u9.place(x=380,y=300,width=90,height=25)
            u10=Label(f5,text="Digital",font=("",15),bg="cyan",fg="black")
            u10.place(x=240,y=350,width=90,height=25)
            u11=Label(f5,text=r1[5],font=("",15),bg="gold",fg="black")
            u11.place(x=380,y=350,width=90,height=25)
            break
        else:
            u2=Label(f5,text="Control",font=("",15),bg="black")
            u2.place(x=240,y=150,width=1000,height=25)
            u4=Label(f5,text="Dastr",font=("",15),bg="black")
            u4.place(x=240,y=200,width=1000,height=25)
            u6=Label(f5,text="LIC",font=("",15),bg="black")
            u6.place(x=240,y=250,width=1000,height=25)
            u8=Label(f5,text="Sensor",font=("",15),bg="black")
            u8.place(x=240,y=300,width=1000,height=25)
            u10=Label(f5,text="Digital",font=("",15),bg="black")
            u10.place(x=240,y=350,width=1000,height=25)
            messagebox.showinfo("Search","Not Found")
            
        db.commit()
        db.close()
        
        s1.set("")
        
    b1=Button(f5,text="Search",font=("",15),bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=search1)
    b1.place(x=497,y=80,width=130,height=25)
    
def show1(f4):
    for w in f4.winfo_children():
        w.destroy()
    u1=Label(f4,text="EnRoll",font=("",15),bg="cyan",fg="black")
    u1.place(x=50,y=50,width=90,height=25)
    u2=Label(f4,text="Control",font=("",15),bg="cyan",fg="black")
    u2.place(x=150,y=50,width=90,height=25)
    u3=Label(f4,text="Dastr",font=("",15),bg="cyan",fg="black")
    u3.place(x=250,y=50,width=90,height=25)
    u4=Label(f4,text="LIC",font=("",15),bg="cyan",fg="black")
    u4.place(x=350,y=50,width=90,height=25)
    u5=Label(f4,text="Sensor",font=("",15),bg="cyan",fg="black")
    u5.place(x=450,y=50,width=90,height=25)
    u6=Label(f4,text="Digital",font=("",15),bg="cyan",fg="black")
    u6.place(x=550,y=50,width=90,height=25)
    import sqlite3
    db=sqlite3.connect("regis.db")
    cr=db.cursor()
    r=cr.execute("select * from ins")
    x=50
    y=100
    for r1 in r:
        Label(f4,text=r1[0],font=("",11),bg="gold",fg="black").place(x=x,y=y,width=90,height=20)
        x+=100
        Label(f4,text=r1[1],font=("",11),bg="gold",fg="black").place(x=x,y=y,width=90,height=20)
        x+=100
        Label(f4,text=r1[2],font=("",11),bg="gold",fg="black").place(x=x,y=y,width=90,height=20)
        x+=100
        Label(f4,text=r1[3],font=("",11),bg="gold",fg="black").place(x=x,y=y,width=90,height=20)
        x+=100
        Label(f4,text=r1[4],font=("",11),bg="gold",fg="black").place(x=x,y=y,width=90,height=20)
        x+=100
        Label(f4,text=r1[5],font=("",11),bg="gold",fg="black").place(x=x,y=y,width=90,height=20)
        y+=40
        x=50
    db.commit()
    db.close()


def show(n):
    f4=Frame(bg="black")
    f4.pack()
    n.add(f4,text="Show")
    global f55
    f55=f4
    show1(f4)
    
    
def ins1():
    db=sqlite3.connect("regis.db")
    cr=db.cursor()
    cr.execute("insert into ins values('"+a1.get()+"','"+a2.get()+"','"+a3.get()+"','"+a4.get()+"','"+a5.get()+"','"+a6.get()+"')")
    db.commit()
    db.close()
    messagebox.showinfo("Insert","Sucess")
    a1.set("")
    a2.set("")
    a3.set("")
    a4.set("")
    a5.set("")
    a6.set("")
    show1(f55)

a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()
a6=StringVar()

def insert(n):
    f3=Frame(bg="black")
    f3.pack()
    n.add(f3,text="Insert")
    u1=Label(f3,text="EnRoll",font=("",15),bg="cyan",fg="black")
    u1.place(x=200,y=100,width=100,height=25)
    u2=Label(f3,text="Control",font=("",15),bg="cyan",fg="black")
    u2.place(x=200,y=150,width=100,height=25)
    u3=Label(f3,text="Dastr",font=("",15),bg="cyan",fg="black")
    u3.place(x=200,y=200,width=100,height=25)
    u4=Label(f3,text="LIC",font=("",15),bg="cyan",fg="black")
    u4.place(x=200,y=250,width=100,height=25)
    u5=Label(f3,text="Sensor",font=("",15),bg="cyan",fg="black")
    u5.place(x=200,y=300,width=100,height=25)
    u6=Label(f3,text="Digital",font=("",15),bg="cyan",fg="black")
    u6.place(x=200,y=350,width=100,height=25)
    e1=Entry(f3,font=("",15),textvariable=a1)
    e1.place(x=350,y=100,width=180,height=25)
    e2=Entry(f3,font=("",15),textvariable=a2)
    e2.place(x=350,y=150,width=180,height=25)
    e3=Entry(f3,font=("",15),textvariable=a3)
    e3.place(x=350,y=200,width=180,height=25)
    e4=Entry(f3,font=("",15),textvariable=a4)
    e4.place(x=350,y=250,width=180,height=25)
    e5=Entry(f3,font=("",15),textvariable=a5)
    e5.place(x=350,y=300,width=180,height=25)
    e6=Entry(f3,font=("",15),textvariable=a6)
    e6.place(x=350,y=350,width=180,height=25)
    b1=Button(f3,text="Insert",font=("",13),bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=ins1)
    b1.place(x=280,y=400,width=130,height=30)

p=StringVar()
q=StringVar()

def menu():
    n=ttk.Notebook()
    n.place(x=0,y=0,width=700,height=600)
    def demo(a):
        if(n.index("current")==5):
            login()
    n.bind("<<NotebookTabChanged>>",demo)        
    insert(n)
    show(n)
    search(n)
    update(n)
    delete(n)
    logout(n)
    
def login1():
    import sqlite3
    db=sqlite3.connect("regis.db")
    cr=db.cursor()
    r=cr.execute("select * from regis where Uname='"+p.get()+"' AND Password='"+q.get()+"'")
    for r1 in r:
        menu()
        break
    else:
        messagebox.showinfo("LOGIN","Failed")
    
    
    db.commit()
    db.close()
    p.set("")
    q.set("")

a=StringVar()
b=StringVar()
c=StringVar()

def regis1():
    import sqlite3
    db=sqlite3.connect("regis.db")
    cr=db.cursor()
    cr.execute("insert into regis values('"+a.get()+"','"+b.get()+"','"+c.get()+"')")
    db.commit()
    db.close()
    messagebox.showinfo("REGISTER","Sucess")
    a.set("")
    b.set("")
    c.set("")

def login():
    f2=Frame(bg="black")
    f2.place(x=0,y=0,width=700,height=600)
    u3=Label(f2,text="Name",font=("arial",15,"underline"),bg="cyan",fg="black")
    u3.place(x=150,y=200,width=150,height=25)
    u4=Label(f2,text="Password",font=("arial",15,"underline"),bg="cyan",fg="black")
    u4.place(x=150,y=250,width=150,height=25)
    e1=Entry(f2,font=("",15),textvariable=p)
    e1.place(x=350,y=200,width=250,height=25)
    e2=Entry(f2,font=("",15),textvariable=q,show="*")
    e2.place(x=350,y=250,width=250,height=25)
    b1=Button(f2,text="Login",font=("",15),bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=login1)
    b1.place(x=260,y=310,width="110",height="35")
    b2=Button(text="Register",font=("",15),bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=regis)
    b2.place(x=560,y=540,width="110",height="35")

def regis():
    f1=Frame(bg="black")
    f1.place(x=0,y=0,width=700,height=600)
    u3=Label(f1,text="Name",font=("arial",15,"underline"),bg="cyan",fg="black")
    u3.place(x=150,y=200,width=150,height=25)
    u4=Label(f1,text="Email",font=("arial",15,"underline"),bg="cyan",fg="black")
    u4.place(x=150,y=250,width=150,height=25)
    u5=Label(f1,text="Password",font=("arial",15,"underline"),bg="cyan",fg="black")
    u5.place(x=150,y=300,width=150,height=25)
    e1=Entry(f1,font=("",11),textvariable=a)
    e1.place(x=350,y=200,width=250,height=25)
    e2=Entry(f1,font=("",11),textvariable=b)
    e2.place(x=350,y=250,width=250,height=25)
    e3=Entry(f1,font=("",11),textvariable=c,show="*")
    e3.place(x=350,y=300,width=250,height=25)
    b1=Button(text="Login",font=("",15),bg="GOLD",fg="black",activebackground="CYAN",activeforeground="black",command=login)
    b1.place(x=580,y=540,width="90",height="35")
    b2=Button(text="Register",font=("",15),bg="gold",fg="black",activebackground="cyan",activeforeground="black",command=regis1)
    b2.place(x=250,y=360,width="150",height="35")


f0=Frame(bg="lavender")
f0.place(x=0,y=0,width=700,height=600)
u2=Label(text="Student management system",font=("arial",15,"underline"),bg="yellow",fg="lightgreen")
u2.place(x=50,y=110,width=600,height=30)
b1=Button(text="Login",font=("",15),bg="black",fg="gold",activebackground="gold",activeforeground="black",command=login)
b1.place(x=180,y=160,width="90",height="35")
b2=Button(text="Register",font=("",15),bg="black",fg="gold",activebackground="gold",activeforeground="black",command=regis)
b2.place(x=410,y=160,width="100",height="35")
b3=Button(text="Exit",bg="black",fg="gold",activebackground="gold",activeforeground="black",command=t.destroy)
b3.place(x=0,y=0,width=10,height=10)
t.mainloop()