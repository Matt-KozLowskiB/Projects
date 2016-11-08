#!/usr/bin/python
# -*- coding: utf-8 -*-


## Program Title:      FileCopyNMove_Main.py (with associated linked GUI and Function Modules)
## Purpose:            To Construct a Python-based GUI using tkinter, and employing various other
##                     Python modules to effectuate otherwise tedious file operations, and
##                     Interfacing with a database to keep records these operations for later review.
## Program Language:   Python
## Language Version:   3.5.2
## Platform Tested:    Windows 8.1 on x86 OS
## Author:             Matt Kozlowski
## Date Created:       November 7, 2016


import os, sys, time, datetime, shutil, sqlite3
from tkinter import ttk
import tkinter as tk
import FileMoveNCopy_GUI, FileMoveNCopy_funk
from tkinter import *
dt = time.time()


class Window_Main(tk.Frame):
    def __init__(self, parent,  *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.master.title("File Move and Copy Program")
      
        self.master = parent
        ## Set Parent window size limitations:
        self.master.maxsize(450,600)
        
        ## Call center parent window function (courtesy Daniel A. Christie)
        FileMoveNCopy_funk.center_window(self, 450, 600)       
        FileMoveNCopy_GUI.Load_GUI(self, root, *args)

        ## Make sure application window has keyboard focus:
        root.focus_force()
        
        
        
        
    


if __name__ == "__main__":
    root = tk.Tk()
    app=Window_Main(root)
    root.mainloop()
