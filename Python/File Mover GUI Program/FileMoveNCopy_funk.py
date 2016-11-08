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
import FileMoveNCopy_main, FileMoveNCopy_GUI
from tkinter import *
dt = time.time()



def root_dir_select_box(self):
    
    ## Prompt User to Select a Root Directory Using Directory Widget:
    rootpath=StringVar()
    directory=(filedialog.askdirectory(title= 'Please Select The Directory Containing Your Target Folders'))
    rootpath.set(os.path.abspath(directory))
    
    
    ## Populate Nav Root Directory with User's Selection from Dir Widget:
    self.nav_text.insert(0, rootpath.get())
    return rootpath.get
        
def src_select_funk(self, Blarmee, x655556):
    
    ## On Select Source Buttonpress, Erase Contents of Source Library, 
    self.srcLB.delete(0, END)
    
    ## Get Selected Folder Path and Copy into Source Text Entry box:
    self.src_text.insert(0, Blarmee.get())
    
    ## If no Source Selected, generate error on Select Buttonpress:
    if self.src_text.get()=="":
        messagebox.showerror(title='Unexpected Error!',
        message='Please Select a Source Folder First! You can do this by clicking on it in the Root Directory, then pressing SELECT')
        return
    
    ## Otherwise, Update Secondary Listbox Title to 'Last Modified':
    self.destLB_lbl.config(justify=CENTER,text='Last Modified:')
    i=0
    for p in os.listdir(self.src_text.get()):        
        contents=os.path.join(self.src_text.get(), p)
        
        ## Create filestats variable and set equal to stat result dictionary: 
        filestats= os.stat(contents)
        date = str(datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S'))
        
        ## Get and Convert Last Modification Datestamp to Intelligible Format and set = variable modDate:
        modDate=str(datetime.datetime.fromtimestamp(filestats[8]).strftime('%Y-%m-%d %H:%M:%S'))
        
        ## Display Last Modification Result for each file in Secondary Listbox:
        self.srcLB.insert(i, p )
        self.destLB.insert(i, modDate)
        i +=1
        
    ## When All Files Processed, Disable Source Select Button & Entry Box:              
    self.src_text.config(state='disabled')
    self.btn_srcselect.config(state='disabled')
                    
                    
                    
                    
            
def dest_select_funk(self, Blarmee, x):
    
    ## Empty Existing Contents of Destination Listbox, if necessary:
    self.destLB.delete(0, END)
    self.destLB_lbl.config(text='Destination Folder Contents')
    
    ## If no Destination folder selected by user, generate error on Select Buttonpress:
    if self.src_text.get() == '':
        messagebox.showerror(title='Unexpected Error!',
        message='Please Select a Source Folder First! You can do this by clicking on it in the Root Directory, then pressing SELECT')
        return
               
    else:
        ## Otherwise, Get User Destination Folder Selection & Disable Select Button:
        x=self.dest_text.insert(0, Blarmee.get())
        self.dest_text.config(state='disabled')
        self.btn_destselect.config(state='disabled')
        
        ## Get files from selected folder and display in Destination Listbox:
        for p in os.listdir(Blarmee.get()):            
            contents=os.path.join(Blarmee.get(), p)            
            i=1
            self.destLB.insert(i, p)
            i +=1
            
def Reset_funk(self, Blarmee, CopySelection):
    ## Reset Text Entry Widgets to Default:       
    self.src_text.config(state='normal')
    self.src_text.delete(0, END)
    self.dest_text.config(state='normal')
    self.dest_text.delete(0, END)
    self.copymod_text.delete(0, END)
    self.nav_text.delete(0, END)
    
    ## Reset & Enable Selection Buttons:
    self.btn_destselect.config(state='normal')
    self.btn_srcselect.config(state='normal')
    
    ## Empty and Reset Both Listboxes:
    self.srcLB.delete(0, END)
    self.destLB.delete(0, END)
    self.destLB_lbl.config(text='Destination Folder Contents')
    
    ## Reset Treeselection Event Variable:
    Blarmee.set('')
    CopySelection.set('')
    
    ## Delete Current Root Dir Treeview & Reset:
    self.tree.parent('')
    for i in self.tree.get_children(''):
        self.tree.delete(i)
        
    ## Re-Initiate Program by Asking User for New Root Directory Selection:
    root_dir_select_box(self)
    
    ## Re-Populate Treeview with User Selected Root Directory:
    start_tree(self)
            
def Copy_All_funk(self):
    ## Update Listbox Title to fit Move Function:
    self.destLB_lbl.config(text='Destination Folder Contents')
    ##Get Selected Source and Destination Folders:
    source=self.src_text.get()
    destination=self.dest_text.get()
    for file in os.listdir(source):        
        target=(os.path.join(source, file))
        destiny=(os.path.join(destination, file))
        ## Delete File from Source Folder Listbox & display in Destination Folder Listbox:
        for i in range(0, self.srcLB.size()):
                  
            if self.srcLB.get(i)==file:
                self.srcLB.delete(i, i)
                self.destLB.insert(END, file)
        ## Finally, Move the file to Destination Folder:        
        shutil.move(target, destiny)

        
def Copy_Mod_funk(self, Modtime):
    ##Update Listbox to Fit Copy Modified Function:
    self.destLB_lbl.config(text='Destination Folder Contents')
   
    ## Get selected source & destination folders:
    source=self.src_text.get()
    destination=self.dest_text.get()
    
    ## Identify each file in target folder
    for file in os.listdir(source):        
        target=(os.path.join(source, file))
        destiny=(os.path.join(destination, file))
       

        ## Get file attribute tuple, assign to var filestats
        filestats = os.stat(target)
        
        ## Compare last modification time to current time; check if< User Entered Elapsed ModTime:        
        if ((int(dt) - int(filestats[8]))/3600)<float(Modtime):
            
            ## If True, Copy File to Destination Listbox & Copy To Selected Destination Folder:
            for i in range(0, self.srcLB.size()):
                if self.srcLB.get(i)==file:                        
                    self.destLB.insert(END, file)                     
                    shutil.copy2(os.path.join(source, file), os.path.join(destination, file))
                    
    
                    
                    
                #
            
            
def Execute_copy_funk(self, CopySelection):
    ## Collect User Selected Parameters & assign to variables
    source=(self.src_text.get())
    destination=(self.dest_text.get())
    selection=(CopySelection.get())
    Modtime=(self.copymod_text.get())
    
    ## Test & Function Call for Review Last Mod Check Log in database:
    if selection=='Check'   :
        Check_last_mod_funk(self, source)
        
    ## Test to make sure Source & Destination Folders Selected
    elif ((self.src_text.get()=="") or (self.dest_text.get()== (''))) :
        
        ## If False, Generate Error Message & DisplayL
        messagebox.showerror(title='Unexpected Error!',
        message='Both Destination and Source Folder must be Selected Prior to Execution..!')
        return
    
    ## Test to ensure User hasn't selected same Folder for source & destination:    
    elif (self.src_text.get())==(self.dest_text.get()):
        messagebox.showerror(title='Unexpected Error!',
        message='Use You Head!  Source and Destination folders cannot be identical..')
        return
    
    ## If Selections OK, then Call function according to user selection:
    else:
        ## Function Call to Copy ALL files regardless:
        if selection =='All':
            Copy_All_funk(self)
        
        elif selection=='Mod':
            if Modtime=='':
                Copy_All_funk(self)
                
            ## Function to  Copy only those within User Specified Elapsed time since Last Modification:
            else:
                Copy_Mod_funk(self, Modtime)
   


def center_window(self, w, h): # Courtesy of Daniel A. Christie (Phonebook Drill Program):
    ## get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    ## calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
    
def start_tree(self):
    ## Generate Parent Root Node Directory for Treeview Widget:
    wholepath=(os.path.abspath(self.nav_text.get()))   
    father=self.tree.insert('', 'end', text=wholepath,open=True)
    child_proc_dir(self, father, wholepath)
           
def child_proc_dir(self, parent, path):
    ## Process Child Folders of Root Node & Display in TreeView, Except files in Root Node:
    for p in os.listdir(path):            
        if path==os.path.abspath(self.nav_text.get()):             
            if os.path.isfile(os.path.join(path, p)):
                continue
        wholepath=os.path.join(path, p)
        isdir = os.path.isdir(wholepath)                
        old=self.tree.insert(parent, 'end', text=p, open=False)
        
        ## Re-Run Folder Processing until all Folders in Root are Completed:
        if isdir:
            child_proc_dir(self, old, wholepath)

def Check_last_mod_funk(self, source):
    ## Update Destination Listbox Title to fit current function & Delete Contents:
    self.destLB_lbl.config(text='Last Modification Check')
    self.destLB.delete(0, END)
    
    ## Process Each file in Source Folder:
    for file in os.listdir(source):
        contents=os.path.join(source, file)
        
        ## Get stats on each file and set to variable:
        filestats= os.stat(contents)    
        
        ## Get current date & time from time() module & format so Intelligible to User:
        date = str(datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S'))
        
        ## Get Last Modified Date for each file & format so intelligible to User:
        modDate=str(datetime.datetime.fromtimestamp(filestats[8]).strftime('%Y-%m-%d %H:%M:%S'))

        ## Determine Elapsed time (in hours) from Last Modified date to Current time/date:
        ModDelta=(int(round(int(dt) - int(filestats[8]))/3600))
      
        ## Connect to Sqlite Database:
        conn=sqlite3.connect('test_database.db')
        c=conn.cursor()
        ## Create Table if needed 'checkstats' and declare columns for filename, last mod date, and time logged:
        c.execute("CREATE TABLE IF NOT EXISTS checkstats(Filename TEXT, Modtime INT, ModDelta INT, LogTime TEXT)")
        conn.commit()
        
        ## for each file, check database for last Logtime entry:
        c.execute("SELECT MAX(Logtime) FROM checkstats WHERE Filename='{m}'".format(m=contents))
        conn.commit()
       
        ## Get each Logtime from Database & Display in Seconday Listbox:
        for row in c.fetchone():                      
            self.destLB.insert(END, row)
          
        ## Once Last Logtime displayed for each file, add new data with current Logtime in DB:
        c.execute("INSERT INTO checkstats(Filename, Modtime, ModDelta, Logtime) VALUES(?,?, ?, ?)",(contents, filestats[8], ModDelta, date))
        conn.commit()    
        conn.close()

def BoxSelect(event):
    ## Ensure Keyboard focus set to Hours since modified entry widget on mouseclick:
    self.copymod_text.config(state='normal')
    self.copymod_text.focus_displayof()

if __name__ == "__main__":
    pass                    
