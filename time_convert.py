from tkinter import *
from tkinter import ttk
def t():
    root=Tk()
    root.geometry("700x600+100+100")
    root.title("Time Converter")
    root.configure(bg='#F08080')
    OPTIONS = {
        "Hours to Minutes":60,
        "Hours to Seconds":3600,
        "Minutes to Seconds":60,
        "Minutes to Hours":0.0166667,
        "Seconds to Minutes":0.0166667,
        "Seconds to Hours":0.000277778
            }
    def ok():
        price = rup.get()
        print(price)
        ans = vi.get()
        print(ans)
        DICT = OPTIONS.get(ans,None)
        conv = int(price)*float(DICT)
        print(conv)
        res.delete(1.0,END)
        res.insert(INSERT,"Time In ",INSERT,ans,INSERT," = ",INSERT,conv)
    butt1 = Button(root,text = "Back",fg='#4B0082',bg='#F0F8FF',font=("Lucida Calligraphy",15,"bold"), command=root.destroy)
    butt1.place(x = 10 , y = 10)    
    l1 = Label(root,text="Time Converter.",font=("Lucida Calligraphy",25,"bold"),fg="dark red",bg='#F08080')
    l1.place(x = 180 , y = 10)
    l2 = Label(root,text="Enter the Time.",font=("MV Boli",20,"bold"),fg="dark blue",bg='#F08080') 
    l2.place(x = 50 , y = 109)
    res = Text(root,height=2, width=40,font=("MV Boli",14,"bold"),bd=5)
    res.place(x = 50 , y = 320)
    india = Label(root,text="In Integer Value",font=("MV Boli",16,"bold"),bg='#F08080')
    india.place(x = 85 , y = 150)
    rup = Entry(root,font=("MV Boli",12,"bold"))
    rup.place(x = 100 , y = 200, width=150,height=25)
    cho = Label(root,text="Choice Time Type",font=("MV Boli",20,"bold"),bg='#F08080')
    cho.place(x = 420 , y = 110)
    vi = StringVar(root)
    vi.set(None)
    opt = OptionMenu(root,vi,*OPTIONS)
    opt.place(x = 390 , y = 160, width=300,height=35)
    btn = Button(root,text="Convert",bg='#EEE8AA',font=("MV Boli",14,"bold"),height=1,bd=2, width=15,command=ok)
    btn.place(x = 80 , y = 250)


