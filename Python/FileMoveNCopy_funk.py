#!/usr/bin/python
import os
from tkinter import *
import tkinter as tk
import shutil
from tkinter import ttk
import sys
import datetime
import time
import sqlite3

dt = time.time()


import FileMoveNCopy1_main
import FileMoveNCopy_GUI



def root_dir_select_box(self):
    rootpath=StringVar()
    directory=(filedialog.askdirectory())
    rootpath.set(os.path.abspath(directory))
    self.nav_text.insert(0, rootpath.get())
    return rootpath.get()
        
def src_select_funk(self, Blarmee, x, z):
    
    self.srcLB.delete(0, END)
    self.src_text.insert(0, Blarmee.get())
    n=x.get()
    zz=z.get()
    print(x)
    print(z)
    print(n)
    print(zz)
    
    if self.src_text.get()=="":
        messagebox.showerror(title='Unexpected Error!',
        message='Please Select a Source Folder First! You can do this by clicking on it in the Root Directory, then pressing SELECT')
        return    
    for p in os.listdir(Blarmee.get()):
        
        
        
        contents=os.path.join(Blarmee.get(), p)
        
        
        print((self.tree.focus()))
        print(contents)
        i=0
        filestats= os.stat(contents)
        date = str(datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S'))
        print('/n')
        conn=sqlite3.connect('test_database.db')
        c=conn.cursor()

        #c.execute("CREATE TABLE filestats(Filename TEXT, Modtime INT, Filesize INT, Createtime INT, LogTime TEXT)")
##        c.execute("INSERT INTO filestats(Filename, Modtime, Filesize, Createtime, Logtime) VALUES(?, ?, ?, ?, ?)",(contents, filestats[8], filestats[6], filestats[9],date))
##        conn.commit()
        c.execute("SELECT min(Modtime) FROM filestats WHERE Filename='{m}'".format(m=contents))
        conn.commit()
        for info in c.fetchall():
            print (info)
        print('/n')
            
        print(int(round(int(dt) - int(filestats[8]))/3600))
        print(filestats)
       
        print(date)
        modDate=str(datetime.datetime.fromtimestamp(filestats[8]).strftime('%Y-%m-%d %H:%M:%S'))
        print(modDate)
        
        self.srcLB.insert(i, p )
        self.destLB.insert(i, modDate)
        i +=1
        
    c.execute("SELECT * FROM filestats")
    conn.commit()
    for row in c.fetchall():
        print(row)
        
    
    self.src_text.config(state='disabled')
    self.btn_srcselect.config(state='disabled')
                    
                    
                    
                    
            
def dest_select_funk(self, Blarmee, x, z):
    self.destLB.delete(0, END)
    if self.src_text.get() == '':
        messagebox.showerror(title='Unexpected Error!',
        message='Please Select a Source Folder First! You can do this by clicking on it in the Root Directory, then pressing SELECT')
        return
               
    else:
        x=self.dest_text.insert(0, Blarmee.get())
        self.dest_text.config(state='disabled')
        self.btn_destselect.config(state='disabled')
        for p in os.listdir(Blarmee.get()):
            
            contents=os.path.join(Blarmee.get(), p)
            
            i=1
            self.destLB.insert(i, p)
            i +=1
            
def Reset_funk(self, Blarmee):
            
    self.src_text.config(state='normal')
    self.src_text.delete(0, END)
    self.dest_text.config(state='normal')
    self.dest_text.delete(0, END)
    self.copymod_text.delete(0, END)
    self.btn_destselect.config(state='normal')
    self.btn_srcselect.config(state='normal')
    self.srcLB.delete(0, END)
    self.destLB.delete(0, END)
    self.nav_text.delete(0, END)
    Blarmee.set('')
    self.tree.parent('')
    for i in self.tree.get_children(''):
        self.tree.delete(i)
    root_dir_select_box(self)
    wholepath=(os.path.abspath(self.nav_text.get()))
    father=self.tree.insert('', 'end', text=wholepath,open=True)
    child_proc_dir(self, father, wholepath)
            
def Copy_All_funk(self):
    
    source=self.src_text.get()
    destination=self.dest_text.get()
    for file in os.listdir(source):        
        target=(os.path.join(source, file))
        destiny=(os.path.join(destination, file))      
        for i in range(0, self.srcLB.size()):
                  
            if self.srcLB.get(i)==file:
                self.srcLB.delete(i, i)
                self.destLB.insert(END, file)
                
        shutil.move(target, destiny)

        
def Copy_Mod_funk(self, modtime, selection):
    print(modtime)
    source=self.src_text.get()
    destination=self.dest_text.get()
    # Identify each file in target folder
    for file in os.listdir(source):        
        target=(os.path.join(source, file))
        destiny=(os.path.join(destination, file))
       

        # Get file attribute tuple, assign to var filesstats
        filestats = os.stat(target)   
        print(((int(dt) - int(filestats[8]))/3600))
        # compare last modification time to current time; check if< 24 HR        
        if ((int(dt) - int(filestats[8]))/86400)<float(modtime):
            for i in range(0, self.srcLB.size()):
                if self.srcLB.get(i)==file:
                        
                    self.destLB.insert(END, file)
                     # If < 24 HR, copy file to dest folder 
                    shutil.copy2(os.path.join(source, file), os.path.join(destination, file))
                    
    
                    
                    
                #
            
            
def Execute_copy_funk(self, CopySelection):
    selection=(CopySelection.get())
    if selection=='Check'   :
        Check_last_mod_funk(self)
    
    if ((self.src_text.get()=="") or (self.dest_text.get()== (''))) :
        messagebox.showerror(title='Unexpected Error!',
        message='Both Destination and Source Folder must be Selected Prior to Execution..!')
        return
        
    elif (self.src_text.get())==(self.dest_text.get()):
        messagebox.showerror(title='Unexpected Error!',
        message='Use You Head!  Source and Destination folders cannot be identical..')
        return
    else:    
        source=(self.src_text.get())
        destination=(self.dest_text.get())
        selection=(CopySelection.get())
        modtime=(self.copymod_text.get())
    
    if selection =='All':
        Copy_All_funk(self)
    elif selection=='Mod':
        if modtime=='':
            Copy_All_funk(self)
        else:
            Copy_Mod_funk(self, modtime, selection)


def treeselect(event):
    self=self.parent           
    x=(selection())             
    vary=(self.tree.item(x, option='text'))      
    foofoo=(os.path.join(selectpath, vary))
    Blarmee.set(foofoo)                            
    return str(foofoo)
    
def start_tree(self, path):
    wholepath=(os.path.abspath(self.nav_text.get()))   
    father=self.tree.insert('', 'end', text=wholepath,open=True)
    child_proc_dir(self, father, wholepath)
           
def child_proc_dir(self, parent, path):
  
    for p in os.listdir(path):            
        if path==os.path.abspath(self.nav_text.get()):             
            if os.path.isfile(os.path.join(path, p)):
                continue
        wholepath=os.path.join(path, p)
        isdir = os.path.isdir(wholepath)                
        old=self.tree.insert(parent, 'end', text=p, open=False)
        if isdir:
            child_proc_dir(self, old, wholepath)
            

if __name__ == "__main__":
    pass                    
