import tkinter 
from tkinter import *
from tkinter import ttk
def t():
    root=Tk()
    root.geometry("700x600+100+100")
    root.title("Currency Converter")
    root.configure(bg='#FAEBD7')
    OPTIONS = {
        "Euro":77.85,
        "US Dollar":69.32,
        "British Pound":90.92,
        "Japanese Yen":0.628
            }
    def ok():
        price = rup.get()
        ans = vi.get()
        DICT = OPTIONS.get(ans,None)
        conv = float(price)/float(DICT)
        res.delete(1.0,END)
        res.insert(INSERT,"Price In ",INSERT,ans,INSERT," = ",INSERT,conv)

    im = PhotoImage(file="bk.png")
    butt1 = Button(root,text = "Back",fg='#4B0082',bg='#F0F8FF',font=("Lucida Calligraphy",15,"bold"), command=root.destroy)
    butt1.place(x = 10 , y = 10)    
    l1 = Label(root,text="Currency Converter.",font=("Lucida Calligraphy",25,"bold"),fg="dark red",bg='#FAEBD7')
    l1.place(x = 180 , y = 10)
    #l1.grid(row=1,column=0,ipadx=180)
    l2 = Label(root,text="Enter the Currency.",font=("MV Boli",20,"bold"),fg="dark blue",bg='#FAEBD7') 
    l2.place(x = 50 , y = 109)
    #l2.grid(row=2,column=0, ipadx=20)
    res = Text(root,height=2, width=40,font=("MV Boli",14,"bold"),bd=5)
    res.place(x = 50 , y = 320)    #res.grid(row=3,column=0, padx=12, pady=40)
    india = Label(root,text="In Indian Rupee",font=("MV Boli",16,"bold"),bg='#FAEBD7')
    india.place(x = 85 , y = 150)
    #india.grid(row=4,column=0)
    rup = Entry(root,font=("MV Boli",12,"bold"))
    rup.place(x = 100 , y = 200, width=150,height=25)
    #rup.place(x = 200 , y = 200)
    #rup.grid(row=5,column=0)
    cho = Label(root,text="Choice Country",font=("MV Boli",20,"bold"),bg='#FAEBD7')
    cho.place(x = 420 , y = 110)
    #cho.grid(row=6,column=0)
    vi = StringVar(root)
    vi.set(None)
    opt = OptionMenu(root,vi,*OPTIONS)
    opt.place(x = 390 , y = 160, width=300,height=35)
    #opt.grid(row=7,column=0)
    btn = Button(root,text="Convert",bg='#EEE8AA',font=("MV Boli",14,"bold"),height=1,bd=2, width=15,command=ok)
    btn.place(x = 80 , y = 250)
    #btn.grid(row=8,column=0)
    
    




