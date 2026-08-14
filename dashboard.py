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
        listbox.delete(0,tk.END)
        for col in df.columns:
            listbox.insert(tk.END, col)

button = tk.Button(root,text="Load CSV",command=choose_file) #creates the click able button with choose_file funciton
button.pack(pady = 10) 

#list box on the screen
listbox = tk.Listbox(root)
listbox.pack(pady= 10)
listbox.insert(tk.END,"some item")

char_type = tk.StringVar(value= "bar")
dropdown = tk.OptionMenu(root, char_type,"bar","line","scatter")
dropdown.pack(pady= 10)

def plot_chart():
   selection = listbox.curselection()
   if selection:
        selected_col = listbox.get(selection[0])
        seleted_type = char_type.get()
        print(f"Column:{selected_col}, chart type:{seleted_type}")
   else:
       print("no column selected!")
plot_button = tk.Button(root,text="plot",command = plot_chart)
plot_button.pack(pady = 10)

root.mainloop() # keeps the window open until the close button is clicked
