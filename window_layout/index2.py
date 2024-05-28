import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("pack")
        self.geometry('500x200')

        ttk.Button(self, text="Left").pack(side='left')
        ttk.Button(self, text="Center Button").pack(side='left')
        ttk.Button(self, text="Right").pack(side='left')
        
if __name__ == 'main':
    window:Window = Window()
    window.mainloop()