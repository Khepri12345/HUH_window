import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("pack")
        self.geometry('500x200')

        ttk.Button(self, text="Left").pack(side='left', expand=1,fill='both')
        ttk.Button(self, text="Center Button").pack(side='left', expand=1,fill='both')
        ttk.Button(self, text="Right").pack(side='left', expand=1,fill='both')
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()