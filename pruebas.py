from tkinter import *
from tkinter import ttk

root = Tk()
root.title ("Hola Mundo")
ttk.Label(root,text="Hola Mundo").grid()
ttk.Button(root,text="Presionar").grid()
root.mainloop()