import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        self.geometry('300x200')
        
        ttk.Button(self,text="Top").pack(side='top', expand=1,fill='both')  

        ttk.Button(self,text="Middle").pack(side='top', expand=1,fill='both')  

        ttk.Button(self,text="Bottom").pack(side='top', expand=1,fill='both')
        


if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()