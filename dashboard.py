import tkinter as tk
from tkinter import filedialog
import pandas as pd
root = tk.Tk()
root.title("CSV Explorer")
root.geometry("600x400")

label = tk.Label(root, text="Welcome")
label.pack(side="top", pady=10)
df = None
def choose_file():
    global df
    filepath = filedialog.askopenfile(filetypes=[("CSV files","*.csv")])
    if filepath:
        df = pd.read_csv(filepath)
        print(df.head())


button = tk.Button(root,text="Load CSV",command=choose_file)
button.pack(pady = 10)

root.mainloop()