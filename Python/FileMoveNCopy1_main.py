import os
from tkinter import *
import tkinter as tk
import shutil
from tkinter import ttk
import sys
import datetime
import time

import FileMoveNCopy_funk
import FileMoveNCopy_GUI

dt = time.time()


class Window_Main(tk.Frame):
    def __init__(self, parent,  *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.master.title("File Move and Copy Program")
        
        self.parent = parent
        self.parent.maxsize(500,600)
               
        FileMoveNCopy_GUI.Load_GUI(root, self)
        
        
        
        
        
        
    


if __name__ == "__main__":
    root = tk.Tk()
    app=Window_Main(root)
    root.mainloop()
