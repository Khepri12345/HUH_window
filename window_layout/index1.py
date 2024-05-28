import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("pack")
        self.geometry('300x200')

        ttk.Button(self, text="Top").pack()
        ttk.Button(self, text="Middle").pack()
        ttk.Button(self, text="Bottom").pack()
        
if __name__ == 'main':
    window:Window = Window()
    window.mainloop()