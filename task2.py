import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("POKEMON ADVENTURE")
window.geometry("650x550")

label1 = tk.Label(window,text="MINI MAP")

bigmap = PhotoImage(file="main.png")
label2 = tk.Label(window, image=bigmap)

minimap = PhotoImage(file="minimap.png")
label3 = tk.Label(window, image=minimap)

compass = PhotoImage(file="compass.png")
label4 = tk.Label(window, image=compass)

nintendo = PhotoImage(file="logo.png")
label5 = tk.Label(window, image=nintendo)

button1 = tk.Button(window,text="MAP",height=2,width=13,relief="raised")

button2 = tk.Button(window,text="INVENTORY",height=2,width=13,relief="raised")

button3 = tk.Button(window,text="POKEDEX",height=2,width=13,relief="raised")

button4 = tk.Button(window,text="ROSTER",height=2,width=13,relief="raised")

button5 = tk.Button(window,text="JOURNAL",height=2,width=13,relief="raised")

button6 = tk.Button(window,text="HELP",height=2,width=13,relief="raised")

button7 = tk.Button(window,text="SHOP",height=2,width=13,relief="raised")

label1.place(x=540,y=25)
label2.place(x=1,y=1)
label3.place(x=520,y=50)
label4.place(x=1,y=440)
label5.place(x=250,y=470)
button1.place(x=520,y=150)
button2.place(x=520,y=190)
button3.place(x=520,y=230)
button4.place(x=520,y=270)
button5.place(x=520,y=310)
button6.place(x=520,y=350)
button7.place(x=520,y=390)

window.mainloop()