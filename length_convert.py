from tkinter import *
from tkinter import ttk
def t():
    root=Tk()
    root.geometry("700x600+100+100")
    root.title("Length Converter")
    root.configure(bg='#66CDAA')    
    OPTIONS = {
        "Metre to Centimetre":100,
        "Metre to Kilometer":0.001,
        "Metre to Millimetre":1000,
        "Metre to Yard":1.09361,
        "Metre to Foot":3.28084,
        "Metre to Inch":39.3701,

        "Kilometer to Centimetre":100000,
        "Kilometer to Meter":1000,
        "Kilometer to Millimetre":1000000,
        "Kilometer to Yard":1093.6133,
        "Kilometer to Foot":3280.8399,
        "Kilometer to Inch":39370.0787,

        "Centimetre to Meter":0.01,
        "Centimetre to Kilometer":0.00001,
        "Centimetre to Millimetre":10,
        "Centimetre to Yard":0.0109361,
        "Centimetre to Foot":0.0328084,
        "Centimetre to Inch":0.393701,

        "Millimetre to Centimetre":0.1,
        "Millimetre to Kilometer":0.000001,
        "Millimetre to Meter":0.001,
        "Millimetre to Yard":0.00109361,
        "Millimetre to Foot":0.00328084,
        "Millimetre to Inch":0.0393701,

        "Yard to Centimetre":91.44,
        "Yard to Kilometer":0.0009144,
        "Yard to Millimetre":914.4,
        "Yard to Meter":0.9144,
        "Yard to Foot":3,
        "Yard to Inch":36,

        "Foot to Centimetre":30.48,
        "Foot to Kilometer":0.0003048,
        "Foot to Millimetre":304.8,
        "Foot to Yard":0.333333,
        "Foot to Meter":0.3048,
        "Foot to Inch":12,

        "Inch to Centimetre":2.54,
        "Inch to Kilometer":0.0000254,
        "Inch to Millimetre":25.4,
        "Inch to Yard":0.277778,
        "Inch to Foot":0.083333,
        "Inch to Mter":0.0254,

        
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
        res.insert(INSERT,"Length In ",INSERT,ans,INSERT," = ",INSERT,conv)
    butt1 = Button(root,text = "Back",fg='#4B0082',bg='#F0F8FF',font=("Lucida Calligraphy",15,"bold"), command=root.destroy)
    butt1.place(x = 10 , y = 10)
    l1 = Label(root,text="Length Converter.",font=("Lucida Calligraphy",35,"bold"),fg="dark red",bg='#66CDAA')
    l1.place(x = 180 , y = 10)
    l2 = Label(root,text="Enter the Length.",font=("MV Boli",20,"bold"),fg="dark blue",bg='#66CDAA') 
    l2.place(x = 50 , y = 109)
    res = Text(root,height=2, width=40,font=("MV Boli",14,"bold"),bd=5)
    res.place(x = 50 , y = 320)
    india = Label(root,text="In Integer Type",font=("MV Boli",16,"bold"),bg='#66CDAA')
    india.place(x = 85 , y = 150)
    rup = Entry(root,font=("MV Boli",12,"bold"))
    rup.place(x = 100 , y = 200, width=150,height=25)
    cho = Label(root,text="Choice Length.",font=("MV Boli",20,"bold"),bg='#66CDAA')
    cho.place(x = 420 , y = 110)
    vi = StringVar(root)
    vi.set(None)
    opt = OptionMenu(root,vi,*OPTIONS)
    opt.place(x = 390 , y = 160, width=300,height=35)
    btn = Button(root,text="Convert",bg='#EEE8AA',font=("MV Boli",14,"bold"),height=1,bd=2, width=15,command=ok)
    btn.place(x = 80 , y = 250)


