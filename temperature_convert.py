from tkinter import *
from tkinter import ttk
def t():
    root=Tk()
    root.geometry("700x600+100+100")
    root.title("Temperture Converter")
    root.configure(bg='#DDA0DD')
    OPTIONS = {
        "Celsius to Fahrenheit":33.8,
        "Celsius to kelvin":274.15,
        "Celsius to Rankine":493.47,
        "Celsius to Reaumur":0.8,

        "Fahrenheit to Celsius":-17.2222222,
        "Fahrenheit to kelvin":255.927778,
        "Fahrenheit to Rankine":460.67,
        "Fahrenheit to Reaumur":-13.7777778,

        "kelvin to Celsius":-272.15,
        "kelvin to Fahrenheit":-457.87,
        "kelvin to Rankine":1.8,
        "kelvin to Reaumur":-217.72,

        "Rankine to CelsiusFahrenheit":-272.594444,
        "Rankine to Fahrenheit":-458.67,
        "Rankine to kelvin":0.555555556,
        "Rankine to Reaumur":-218.075556,

        "Reaumur to Fahrenheit":34.25,
        "Reaumur to kelvin":274.4,
        "Reaumur to Celsius":1.25,
        "Reaumur to Rankine":493.92,


            }
    def ok():
        price = rup.get()
        print(price)
        ans = vi.get()
        print(ans)
        DICT = OPTIONS.get(ans,None)
        print()
        conv = int(price)*float(DICT)
        print(conv)
        res.delete(1.0,END)
        res.insert(INSERT,"Temperature In ",INSERT,ans,INSERT," = ",INSERT,conv)
    butt1 = Button(root,text = "Back",fg='#4B0082',bg='#F0F8FF',font=("Lucida Calligraphy",15,"bold"), command=root.destroy)
    butt1.place(x = 10 , y = 10)    
    l1 = Label(root,text="Temperature Converter.",font=("Lucida Calligraphy",25,"bold"),fg="dark red",bg='#DDA0DD')
    l1.place(x = 180 , y = 10)
    l2 = Label(root,text="Enter the Temperature.",font=("MV Boli",20,"bold"),fg="dark blue",bg='#DDA0DD') 
    l2.place(x = 50 , y = 109)
    res = Text(root,height=2, width=40,font=("MV Boli",14,"bold"),bd=5)
    res.place(x = 50 , y = 320)
    india = Label(root,text="In Integer Value",font=("MV Boli",16,"bold"),bg='#DDA0DD')
    india.place(x = 85 , y = 150)
    rup = Entry(root,font=("MV Boli",12,"bold"))
    rup.place(x = 100 , y = 200, width=150,height=25)
    cho = Label(root,text="Choice Temperature Type",font=("MV Boli",20,"bold"),bg='#DDA0DD')
    cho.place(x = 420 , y = 110)
    vi = StringVar(root)
    vi.set(None)
    opt = OptionMenu(root,vi,*OPTIONS)
    opt.place(x = 390 , y = 160, width=300,height=35)
    btn = Button(root,text="Convert",bg='#EEE8AA',font=("MV Boli",14,"bold"),height=1,bd=2, width=15,command=ok)
    btn.place(x = 80 , y = 250)


