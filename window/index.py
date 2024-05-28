import tkinter as tk

def get_names() -> list[str]: #區域變數
    with open('names.txt',encoding="utf-8") as file:
        content:str = file.read()
    names:list[str] = content.split()
    # for name in names:
    # print(name)
    return names

class Window(tk.Tk): #自定義
    def __init__(self):
        super().__init__()
        self.title("我的GUI程式")

# names:list[str] = get_names()
if __name__ == "__main__": #文件變數
    names:list[str] = get_names()
    window:Window = Window() #繼承
    window.mainloop()