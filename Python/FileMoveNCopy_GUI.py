#!/usr/bin/python
import os
from tkinter import *
import tkinter as tk
import shutil
from tkinter import ttk
import sys
import datetime
import time
rootpath= 'c:\\users\\matt\\desktop'
dt = time.time()


import FileMoveNCopy1_main
import FileMoveNCopy_funk









def Load_GUI(root, self):

        
        CopySelection=StringVar()
        Blarmee=StringVar()
        rootpath=StringVar()
        path=rootpath.get()
        IndexSelected=StringVar()
        z=StringVar()
        x=StringVar()
        y=StringVar()
        pane = ttk.Panedwindow(root, orient = VERTICAL)      
        pane.pack(fill=BOTH, expand=True)

        
        self.userPane=ttk.Frame(pane, relief=RAISED)

        
        self.treePane=ttk.Frame(pane, relief = SUNKEN)

        
        self.dispPane=ttk.Frame(pane, relief =GROOVE)
        self.horpane=ttk.Panedwindow(self.dispPane, orient = HORIZONTAL)

        
        self.destPane=ttk.Frame(self.horpane, relief = RIDGE)
        self.srcPane=ttk.Frame(self.horpane, relief = GROOVE)
        
        
        self.srcLB=tk.Listbox(self.srcPane)
        self.srcLB_lbl = tk.Label(self.srcPane, text ='Source Folder Contents:')
        self.srcLB_lbl.pack(side='top', pady=(2,0))
        sl_v = tk.Scrollbar(self.srcLB, orient = 'vertical', command = self.srcLB.yview)
        sl_h = tk.Scrollbar(self.srcLB, orient = 'horizontal', command = self.srcLB.xview)      
        self.srcLB.configure(yscrollcommand=sl_v.set, xscrollcommand=sl_h.set)
        sl_v.pack(side='right',fill=BOTH )
        sl_h.pack(side='bottom',fill=BOTH)
        
        
        self.destLB=tk.Listbox(self.destPane)
        self.destLB_lbl = tk.Label(self.destPane, text ='Destination Folder Contents:')
        self.destLB_lbl.pack(side='top', pady=(2,0))
        self.dl_v = tk.Scrollbar(self.destPane, orient = 'vertical', command = self.destLB.yview)
        self.dl_h = tk.Scrollbar(self.destPane, orient = 'horizontal', command = self.destLB.xview)      
        self.destLB.configure(yscrollcommand=self.dl_v.set, xscrollcommand=self.dl_h.set)
        self.dl_v.pack(side='right',fill=BOTH, padx=(0, 1 ), pady=(1,2))
        self.dl_h.pack(side='bottom',fill=BOTH, padx=(1, 1 ), pady=(0,2))
        
        
        self.srcLB.pack(fill=BOTH, expand=True)
        self.destLB.pack(side='bottom', fill=BOTH, expand=True,anchor='se')        
        self.srcPane.pack(side='left',fill=BOTH, expand=True)
        self.destPane.pack(side='left', fill=BOTH, expand=True, anchor='se')
        self.horpane.pack(fill=BOTH, expand=True)
        

        self.src_lbl = tk.Label(self.userPane, text ='Source Folder:')
        self.src_lbl.grid(row = 0, column=0, padx=(10, 0), sticky='W')
        self.dest_lbl = tk.Label(self.userPane, text ='Destination Folder')
        self.dest_lbl.grid(row= 1, column=0, padx=(10,0), sticky='W')
        self.nav_lbl = tk.Label(self.userPane, text ='Navigation Root Directory:')
        self.nav_lbl.grid(row=2, column=0, padx=(10,0),pady=(0,10), sticky='W')
        self.src_text = tk.Entry(self.userPane, text='', width=33)
        self.src_text.grid(row=0, column=2, rowspan=1,columnspan=3)
        self.dest_text = tk.Entry(self.userPane, text='',width=33)
        self.dest_text.grid(row=1, column=2, rowspan=1,columnspan=3)
        self.nav_text = tk.Entry(self.userPane, text='',width=33)        
        self.nav_text.grid(row=2, column=2, columnspan=3 )

        
        self.copy_Check = ttk.Radiobutton(self.userPane, text='Review Last Mod Check?', value= 'Check', variable=CopySelection)
        self.copy_Check.grid(row=3, column=0, padx=(10,0),pady=(0,2), sticky='W')
        
        self.copy_All = ttk.Radiobutton(self.userPane, text='Copy All?', value= 'All', variable=CopySelection)
        self.copy_All.grid(row=4, column=0, padx=(10,0), sticky='W')
        self.copy_Mod = ttk.Radiobutton(self.userPane, text='Copy Modified?', variable=CopySelection,value= 'Mod')
        self.copy_Mod.grid(row=5, column=0, padx=(10,0),pady=(0,10), sticky='W')
        self.copymod_lbl = tk.Label(self.userPane, text =':Hours Since Modified?')
        self.copymod_lbl.grid(row = 5, column=1, padx=(10, 0),pady=(0,10), sticky='W')
        self.copymod_text = tk.Entry(self.userPane, text='',width=5)
        self.copymod_text.grid(row=5, column=0,padx=(10,0),pady=(0,10), sticky='E')

       
        self.btn_srcselect=tk.Button(self.userPane, text='Select',command=lambda: FileMoveNCopy_funk.src_select_funk(self, Blarmee, x, z))
        self.btn_srcselect.grid(row = 0, column = 1, padx=(10,0), pady=(2,0), sticky='W')
        self.btn_destselect=tk.Button(self.userPane, text='Select'  ,command=lambda: FileMoveNCopy_funk.dest_select_funk(self, Blarmee,x, z))
        self.btn_destselect.grid(row = 1, column = 1, padx=(10,0),pady=(2,0), sticky='w')
        self.btn_execute=tk.Button(self.userPane, text='Execute Copy?',command=lambda: FileMoveNCopy_funk.Execute_copy_funk(self, CopySelection))
        self.btn_execute.grid(row = 5, column = 2, padx=(10,0), pady=(0,10),sticky='W')
        self.btn_reset=tk.Button(self.userPane, text='Reset?',command=lambda: FileMoveNCopy_funk.Reset_funk(self, Blarmee))
        self.btn_reset.grid(row = 5, column = 3, padx=(10,0), pady=(0,10),sticky='W')

        
        pane.add(self.userPane, weight = 0)

        
        FileMoveNCopy_funk.root_dir_select_box(self)
        
        
        
        
        
        self.tree= ttk.Treeview(self.treePane)        
        sb_v = ttk.Scrollbar(self.treePane, orient = 'vertical', command = self.tree.yview)
        sb_h = ttk.Scrollbar(self.treePane, orient = 'horizontal', command = self.tree.xview)      
        self.tree.configure(yscroll=sb_v.set, xscroll=sb_h.set)
        self.tree.heading(column='#0', text='Root Directory',  )
        self.tree.column('#0', stretch=tk.YES,width=500 )
        sb_v.grid(row=0, column=23, sticky='NS')
        sb_h.grid(row=1, column=0, columnspan=3, sticky='EW')
        self.tree.grid(row=0, column=0, columnspan=22, sticky='nsew')
        pane.add(self.treePane, weight = 0)
        self.dispPane.pack(fill=BOTH, expand=True)
        pane.add(self.dispPane)
              
        
        FileMoveNCopy_funk.start_tree(self, path)        
        
        
        def treeselect(event):
            selectpath=(os.path.abspath(self.nav_text.get()))
##            z=StringVar()
            z.set(self.tree.selection())
            
##            
            print(z.get())
            
##            x=StringVar()
            x.set(self.tree.focus())
            y=   (x.get())
            print(y)
           
            print(self.tree.get_children(y))
            print(self.tree.item(y))
            
            vary=(self.tree.item(y, option='text'))
            print(vary)
            foofoo=(os.path.join(selectpath, vary))
            Blarmee.set(foofoo)                
            return self, Blarmee, x, z
        
        
        a=(self.tree.bind('<<TreeviewSelect>>', treeselect))
        
        
        
        


if __name__ == "__main__":
    pass
