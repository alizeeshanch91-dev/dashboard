#first we added the libraries tkinter is the GUI library that we used
# from tkinter we imported filedialog which is the tool for file picking
# for reading and handling the csv files i used pandas

import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.title("CSV Explorer") # sets the window title bar
root.geometry("600x400") # width and height of window

#creatd the main app windoe

label = tk.Label(root, text="Welcome") # this is the text widget
label.pack(side="top", pady=10) # this is spacing and position


df = None # this is the place holder that will hold out loaded CSV data
def choose_file():
    global df # this will tell that donot make a new df use the outer one
    filepath = filedialog.askopenfile(filetypes=[("CSV files","*.csv")])
    #this is the file picker that is exclusive now for CSV file
    if filepath:
        df = pd.read_csv(filepath)
        print(df.head())


button = tk.Button(root,text="Load CSV",command=choose_file) #creates the click able button with choose_file funciton
button.pack(pady = 10) 

root.mainloop() # keeps the window open until the close button is clicked
