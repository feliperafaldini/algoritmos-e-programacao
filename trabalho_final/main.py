import tkinter as tk
import os
from os import listdir
from os.path import isfile, join

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        path = os.getcwd()
        print(path)
        self.title("Gerenciador de Softwares")
        self.geometry("800x600")

        self.frame = tk.Frame(self)
        self.frame.pack(padx = 10)

        self.list = tk.Listbox(self.frame, width = 50, height = 200)
        self.list.pack(side = "left")

if __name__ == "__main__":
    root = Main()
    root.mainloop()