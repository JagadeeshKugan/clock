from tkinter import *
from tkinter.ttk import *
from datetime import date
from time import strftime
 

root = Tk()
root.title('Clock')
#root.geometry("300x300")
today = date.today()
 
def time():
    string = "Time:"+strftime('%H:%M:%S %p')+" Date: "+str(today)
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='white')
# Placing clock at the centre

lbl.pack(anchor='center')
time()

mainloop()
