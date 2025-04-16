import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("390x100")

entry1 = tk.Entry(window,text="enter")

entry2 = tk.Entry(window,text="text")

combo3 = ttk.Combobox(window,values=["1","2","3","4","5","6","7","8","9","10"])

entry4 = tk.Entry(window,text="or dont")

label1 = tk.Label(window,text="Principal")

label2 = tk.Label(window,text="Interest Rate")

label3 = tk.Label(window,text="Years")

label4 = tk.Label(window,text="-")

label5 = tk.Label(window,text="                      Amount")
                   
label1.grid(row=1,column=1)
label2.grid(row=1,column=2)
label3.grid(row=1,column=3)
label4.grid(row=3,column=1)
label5.grid(row=4,column=1)
entry1.grid(row=2,column=1)
entry2.grid(row=2,column=2)
combo3.grid(row=2,column=3)
entry4.grid(row=4,column=2)


window.mainloop()
