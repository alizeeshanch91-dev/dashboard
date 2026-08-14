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

stats_label = tk.Label(root, text="")
stats_label.pack(pady=10)

# later, to update its text:
stats_label.config(text="new text here")

def plot_chart():
   selection = listbox.curselection()
   if selection:
        selected_col = listbox.get(selection[0])
        selected_type = char_type.get()
        print(f"Column:{selected_col}, chart type:{selected_type}")
        try:
            mean_val = df[selected_col].mean()
            min_val = df[selected_col].min()
            max_val = df[selected_col].max()
            count_val = df[selected_col].count()
            stats_label.config(text=f"Mean: {mean_val:.2f}  Min: {min_val}  Max: {max_val}  Count: {count_val}")
        except:
             stats_label.config(text="Stats not available for this column (non-numeric)")
   else:
       print("no column selected!")
   ax.clear()
   if selected_type == "bar":
       ax.bar(df.index,df[selected_col])
   elif selected_type == "line":
       ax.plot(df.index,df[selected_col])
   elif selected_type == "scatter":
       ax.scatter(df.index,df[selected_col])

   canvas.draw()

plot_button = tk.Button(root,text="plot",command = plot_chart)
plot_button.pack(pady = 10)

from matplotlib.figure import Figure
fig = Figure(figsize=(5, 4))
ax = fig.add_subplot(111) 

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

ax.bar(["a","b","c"], [1,2,3])
canvas.draw()
ax.clear()

root.mainloop() # keeps the window open until the close button is clicked
