import tkinter
import webbrowser
from tkinter import *

root = Tk( ) 
root.title("Abrir o browser")
root.geometry("300x300")

def google():
    webbrowser.open("https://www.google.com")

my_google = Button(root, text="Abrir Google", command=google).pack(pady=20)
root.mainloop()