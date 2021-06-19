import tkinter 
from tkinter import *
from tkinter import ttk
import currency_convert
import time_convert
import length_convert
import temperature_convert


class mc:
    converter = tkinter.Tk()
    converter.geometry("700x600+100+100")
    converter.title("All in Converter")
    converter.configure(bg='#7FFFD4')
    def oh():
        r=currency_convert.t()
        return
    def time():
        r=time_convert.t()
        return

    def oo():
        fd=temperature_convert.t()
        

    def ooc():
        rpw = length_convert.t()
        return


    l1 = Label(converter,text="Multi-Converter",font=("arial",25,"bold"),fg="dark red")
    l1.configure(bg='#7FFFD4')
    l1.pack(ipadx=180)
    im = PhotoImage(file="cc.png")
    butt1 = Button(converter, image=im, width=180, height=180 , bg ="dark red", command=oh)
    butt1.place(x = 60 , y = 80)

    im1 = PhotoImage(file="ttc.png")
    butt2 = Button(converter, image=im1, width=180, height=180 , bg ="dark red",command=oo)
    butt2.place(x = 450 , y = 80)

    im2 = PhotoImage(file="le.png")
    butt3 = Button(converter, image=im2, width=180, height=180 , bg ="dark red",command=ooc )
    butt3.place(x = 60 , y = 350)

    im3 = PhotoImage(file="it.png")
    butt4 = Button(converter, image=im3, width=180, height=180 , bg ="dark red",command=time )
    butt4.place(x = 450 , y = 350)

    l2 = Label(converter,text="Currncy Converter.",font=("arial",18,"bold"),fg="dark blue", bg="#7FFFD4")
    l2.place(x = 50 , y = 270)

    l3 = Label(converter,text="Temperture Converter.",font=("arial",18,"bold"),fg="dark blue", bg="#7FFFD4")
    l3.place(x = 410 , y = 270)

    l4 = Label(converter,text="Length Converter.",font=("arial",18,"bold"),fg="dark blue", bg="#7FFFD4")
    l4.place(x = 50 , y = 550)

    l5 = Label(converter,text="Time Converter.",font=("arial",18,"bold"),fg="dark blue", bg="#7FFFD4")
    l5.place(x = 450 , y = 550)

s = mc()
s
