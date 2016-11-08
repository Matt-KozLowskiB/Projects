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
import FileMoveNCopy_main, FileMoveNCopy_funk
from tkinter import *





def Load_GUI(self, root):

        
        CopySelection=StringVar()
        Blarmee=StringVar()
        rootpath=StringVar()
        path=rootpath.get()       
        x=StringVar()
       

        ## Create and Configure parent frames for widgets:
        pane = ttk.Panedwindow(root, orient = VERTICAL)      
        pane.pack(fill=BOTH, expand=True)

        ## Customize the Upper User Pane Frame:
        self.userPane=ttk.Frame(pane, relief=RAISED)

        ## Customize Frame for TreeView Function:
        self.treePane=ttk.Frame(pane, relief = SUNKEN)

        ## Set Up Frames for Source and Auxiliary Folder Listboxes
        self.dispPane=ttk.Frame(pane, relief =GROOVE)
        self.horpane=ttk.Panedwindow(self.dispPane, orient = HORIZONTAL)
        self.destPane=ttk.Frame(self.horpane, relief = RIDGE)
        self.srcPane=ttk.Frame(self.horpane, relief = RIDGE)

        # Create, Define and synchronize Listbox Vertical Scrollbar Widgets:
        def libscroll(*args):
                sl_v.set(*args)
                dl_v.set(*args)
        def both(*args):                
                self.srcLB.yview(*args)
                self.destLB.yview(*args)                
        dl_v = tk.Scrollbar(self.destPane, orient = 'vertical')        
        sl_v = tk.Scrollbar(self.srcPane, orient = 'vertical')
        self.srcLB=tk.Listbox(self.srcPane, yscrollcommand= libscroll)
        self.destLB=tk.Listbox(self.destPane,yscrollcommand= libscroll)
        sl_v.config(command=both)
        dl_v.config(command=both)

        ## Create Source Folder Listbox Label & Pack in Frame:       
        self.srcLB_lbl = tk.Label(self.srcPane, text ='Source Folder Contents:')
        self.srcLB_lbl.pack(side='top', pady=(2,0))

        ## Create, define, Horizontal ScrollBar and Pack into Source Listbox
        sl_h = tk.Scrollbar(self.srcPane, orient = 'horizontal', command = self.srcLB.xview)      
        sl_v.pack(side='right',fill=BOTH )
        sl_h.pack(side='bottom',fill=BOTH)

        ## Create Default Label for Auxilliary Listbox & Pack into frame:        
        self.destLB_lbl = tk.Label(self.destPane, text ='Destination Folder Contents:')
        self.destLB_lbl.pack(side='top', pady=(2,0))
        dl_v.pack(side='right',fill=BOTH, padx=(0, 1 ), pady=(1,2))

        ## Pack Listboxes and SubFrames into Parent Frames 
        self.srcLB.pack(fill=BOTH, expand=True)
        self.destLB.pack(side='bottom', fill=BOTH, expand=True,)        
        self.srcPane.pack(side='left',fill=BOTH, expand=True)
        self.destPane.pack(side='left', fill=BOTH, expand=True, )
        self.horpane.pack(fill=BOTH, expand=True)
        
        ## Create Entry Widgets and Labels and Position using Grid Manager:
        self.src_lbl = tk.Label(self.userPane, text ='Source Folder:')
        self.src_lbl.grid(row = 0, column=0, padx=(10, 0), sticky='W')
        self.dest_lbl = tk.Label(self.userPane, text ='Destination Folder')
        self.dest_lbl.grid(row= 1, column=0, padx=(10,0), sticky='W')
        self.nav_lbl = tk.Label(self.userPane, text ='Navigation Root Directory:')
        self.nav_lbl.grid(row=2, column=0, padx=(10,0),pady=(0,10), sticky='W')
        self.src_text = tk.Entry(self.userPane, text='', width=33)
        self.src_text.grid(row=0, column=2,padx=(10,0), rowspan=1,columnspan=3)
        self.dest_text = tk.Entry(self.userPane, text='',width=33)
        self.dest_text.grid(row=1, column=2,padx=(10,0), rowspan=1,columnspan=3)
        self.nav_text = tk.Entry(self.userPane, text='',width=33)        
        self.nav_text.grid(row=2, column=2,padx=(10,0), columnspan=3 )

        ## Create RadioButton Widgets and Labels; Place using Grid Manager
        self.copy_Check = ttk.Radiobutton(self.userPane, text='Review Last Mod Check?',\
        value= 'Check', variable=CopySelection)
        self.copy_Check.grid(row=3, column=0, padx=(10,0),pady=(0,2), sticky='W')      
        self.copy_All = ttk.Radiobutton(self.userPane, text='Copy All?',\
        value= 'All', variable=CopySelection)
        self.copy_All.grid(row=4, column=0, padx=(10,0), sticky='W')
        self.copy_Mod = ttk.Radiobutton(self.userPane, text='Copy Modified Within Last', \
        variable=CopySelection,value= 'Mod')
        self.copy_Mod.grid(row=5, column=0, padx=(10,0),pady=(0,10), sticky='W')
        self.copymod_lbl = tk.Label(self.userPane, text ='Hours?')
        self.copymod_lbl.grid(row = 5, column=2, padx=(2, 0),pady=(0,10), sticky='W')
        self.copymod_text = tk.Entry(self.userPane,text='',width=5)
        self.copymod_text.grid(row=5, column=1,padx=(10,0),pady=(0,10), sticky='W')

        ## Bind Mouseclick to Mod Entry widget to ensure keyboard focus:
        self.copymod_text.bind('<ButtonPress>', lambda event: FileMoveNCopy_funk.BoxSelect)

        ## Create Button Widgets and Labels and Associated Function Calls:
        self.btn_srcselect=tk.Button(self.userPane, text='Select',\
        command=lambda: FileMoveNCopy_funk.src_select_funk(self, Blarmee, x))
        self.btn_srcselect.grid(row = 0, column = 1, padx=(10,0), pady=(2,0), sticky='W')
        self.btn_destselect=tk.Button(self.userPane, text='Select', \
        command=lambda: FileMoveNCopy_funk.dest_select_funk(self, Blarmee,x))
        self.btn_destselect.grid(row = 1, column = 1, padx=(10,0),pady=(2,0), sticky='w')
        self.btn_execute=tk.Button(self.userPane, text='Execute?',\
        command=lambda: FileMoveNCopy_funk.Execute_copy_funk(self, CopySelection))
        self.btn_execute.grid(row = 5, column = 3, padx=(0,5), pady=(0,10),sticky='W')
        self.btn_reset=tk.Button(self.userPane, text='Reset?',\
        command=lambda: FileMoveNCopy_funk.Reset_funk(self, Blarmee, CopySelection))
        self.btn_reset.grid(row = 5, column = 4, padx=(0,), pady=(0,10),sticky='w')

        ## Now that User Pane is configured, pack it into parent window frame:
        pane.add(self.userPane, weight = 0)

        ## Next call Function to Select Root Directory for Treeview Display:
        FileMoveNCopy_funk.root_dir_select_box(self)
        
        
        
        
        ## Configure the TreeView Widget for Root Directory Display:
        self.tree= ttk.Treeview(self.treePane)        
        sb_v = ttk.Scrollbar(self.treePane, orient = 'vertical', command = self.tree.yview)
        sb_h = ttk.Scrollbar(self.treePane, orient = 'horizontal', command = self.tree.xview)      
        self.tree.configure(yscroll=sb_v.set, xscroll=sb_h.set)
        self.tree.heading(column='#0', text='Root Directory',anchor=CENTER  )
        self.tree.column('#0', stretch=tk.YES,width=450 )
        sb_v.grid(row=0, column=23, sticky='NS')
        sb_h.grid(row=1, column=0, columnspan=3, sticky='EW')
        self.tree.grid(row=0, column=0, columnspan=22, sticky='nsew')
        pane.add(self.treePane, weight = 0)
        self.dispPane.pack(fill=BOTH, expand=True)
        pane.add(self.dispPane)
           
        ## Then Finally, call function to populate TreeView Widget:
        FileMoveNCopy_funk.start_tree(self)        
        
       

        ## Bind TreeView User Selection to Event
        self.tree.bind('<<TreeviewSelect>>', lambda event: \
        FileMoveNCopy_funk.treeselect(self, event, x, Blarmee))
                
        
        
        


if __name__ == "__main__":
        pass
