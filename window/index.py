import tkinter as tk

def get_names() -> list[str]: #區域變數
    with open('names.txt',encoding="utf-8") as file:
        content:str = file.read()
    names:list[str] = content.split()
    # for name in names:
    # print(name)
    return names

# names:list[str] = get_names()
if __name__ == "__main__": #文件變數
    names:list[str] = get_names()
    window:tk.Tk = tk.Tk()
    window.title("我的GUI程式")
    window.mainloop()