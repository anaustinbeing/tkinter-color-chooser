import tkinter as tk
from tkinter import colorchooser

if __name__ == '__main__':
    root = tk.Tk()
    color = colorchooser.askcolor()
    root.configure(background=color[1])
    tk.mainloop()