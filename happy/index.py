import pandas as pd
from tkinter import ttk
import tkinter as tk

mywin=tk.Tk()
mywin.geometry('300x300')

df=pd.read_csv('HUH_window\happy\World Happiness Report.csv')
df_list=list(df.columns.values)
df_rset=df.to_numpy().tolist()
df_tree=ttk.Treeview(mywin,columns=df_list).pack()
                                     
for i in df_list:
    df_tree.column(i,width=100,anchor='c')
    df_tree.heading(i,text=i)
for dt in df_rset:
    v=[r for r in dt]
    df_tree.insert('','end',iid=v[0], values=v)
df_tree=ttk.Treeview(mywin,columns=df_list)
df_tree.pack()
mywin.mainloop()