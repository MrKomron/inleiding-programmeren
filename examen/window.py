# Dit bestand hoef je niet te begrijpen/lezen

import tkinter as tk
from tkinter import messagebox

def display(message):
    messagebox.showinfo("Message", message)

class rowColException(Exception):
    def __init__(self, row,col):
        super().__init__()
        self.row=row
        self.col=col

    def __str__(self):
        return f"Position ({self.row},{self.col}) is invalid."


class window(tk.Tk):
    def __init__(self,nr,nc):
        # Create the main window
        super().__init__()
        self.title("Speelveld")

        # Dictionary to hold button references
        self.buttons = {}
        self.newCanvas(nr,nc)

        # Create a menu bar
        menu_bar = tk.Menu(self)

        # Create a "File" menu with a command
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Validate", command=self.validate)
        help_menu.add_command(label="Autofill", command=self.autofill)

        # Adding the "File" menu to the menu bar
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Create a "Load" menu with a command
        load_menu = tk.Menu(menu_bar, tearoff=0)
        for i in range(1,5):
            load_menu.add_command(label="opgave "+str(i), command=lambda opg=i : self.load(opg))
        # Adding the "File" menu to the menu bar
        menu_bar.add_cascade(label="Load", menu=load_menu)

        self.config(menu=menu_bar)


    def newCanvas(self,nr,nc):
        # remember number of rows and columns
        self.nr=nr
        self.nc=nc

        # Destroy existing buttons
        for (rows, col) in list(self.buttons.keys()):
            self.buttons[(rows, col)].destroy()
            del self.buttons[(rows, col)]

        # Creating a 10x10 grid of buttons
        for row in range(nr):
            for col in range(nc):
                button = tk.Button(self, width=4, height=2, text="", command=lambda r=row, c=col : self.button_clicked(r, c))
                button.grid(row=row, column=col, sticky="nsew")
                # Store the button in the dictionary
                self.buttons[(row, col)] = button

        # Making the grid expandable
        for i in range(nr):
            self.grid_rowconfigure(i, weight=1)
        for i in range(nc):
            self.grid_columnconfigure(i, weight=1)

    def load(self,i):
        print("Load opgave",i)

    def validate(self):
        print("validate")

    def autofill(self):
        print("autofill")

    # Function to handle button click
    def button_clicked(self, row, col):
        print(f"Button clicked at Row: {row}, Column: {col}")
        # Example of changing the label of the button at (row, col)
        self.change_button_label(row, col, "Clicked")

    # Function to change button label
    def change_button_label(self,row, col, new_label):
        if not(0<=row<self.nr) or not(0<=col<self.nc):
            raise(rowColException(row,col))
        self.buttons[(row, col)].config(text=new_label)

    # Function to get the button label
    def get_button_label(self,row, col):
        if not(0<=row<self.nr) or not(0<=col<self.nc):
            raise(rowColException(row,col))
        return self.buttons[(row, col)].cget('text')

    def disable_button(self,row, col):
        if not(0<=row<self.nr) or not(0<=col<self.nc):
            raise(rowColException(row,col))
        button = self.buttons[(row, col)]
        button.config(bg="lightgrey", state=tk.DISABLED)

    def enable_button(self,row, col):
        if not(0<=row<self.nr) or not(0<=col<self.nc):
            raise(rowColException(row,col))
        button = self.buttons[(row, col)]
        button.config(bg='SystemButtonFace', state=tk.NORMAL)

    def red_button(self,row,col):
        if not(0<=row<self.nr) or not(0<=col<self.nc):
            raise(rowColException(row,col))
        button = self.buttons[(row, col)]
        button.config(bg='red')

    def normalColor_button(self,row,col):
        if not(0<=row<self.nr) or not(0<=col<self.nc):
            raise(rowColException(row,col))
        button = self.buttons[(row, col)]
        button.config(bg='SystemButtonFace')