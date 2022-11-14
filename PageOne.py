# -*- coding: utf-8 -*-

import hashlib
import binascii
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *


class PageOne(tk.Frame):
    """ Page with main functionalities class """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='black')
        self.notebook = ttk.Notebook(self)
        # Define tabs
        self.tab1 = tk.Frame(self.notebook, background='black')
        self.tab1.pack()
        self.tab2 = tk.Frame(self.notebook, background='black')
        self.tab2.pack()
        self.tab3 = tk.Frame(self.notebook, background='black')
        self.tab3.pack()
        self.other = tk.Frame(self.notebook, background='black')
        self.other.pack()
        # Add tabs to notebook instance
        self.notebook.add(self.tab3, text="SHA-256 Hashing")        
        self.notebook.pack(expand=1, fill="both")
        
        self.sha_hashing_tab()
        button = tk.Button(self, text="Exit",
                           command=lambda: self.controller.show_frame("ExitPage"))
        button.configure(foreground='black',background='orange',
                         activebackground='black',
                         activeforeground='black')
        button.pack(side=tk.RIGHT, padx=5, pady=5)
    
   
    # ------------------------------- tab3 ---------------------------------

    def sha_hashing_tab(self):
        self.input31 = tk.LabelFrame(self.tab3, background="black",
                                     foreground='white',
                                     text=" SHA-256 hashing intput ")
        self.input31.pack(expand=1, fill="both", padx=5, pady=5)
        self.textbox31 = tk.Text(self.input31, height=5, width=70,
                                 wrap='word', undo=True)
        self.textbox31.grid(row=0, column=0, columnspan=1)
        self.textbox31.pack(expand=1, fill="both")
        self.SHA_output = tk.StringVar()
        self.SHA_output.set('\nHash sum\n')
        self.input32 = tk.LabelFrame(self.tab3, background="black",
                                     foreground='white',
                                     text=" SHA-256 hashing output ")
        self.input32.pack(expand=1, fill="both", padx=5, pady=5)
        self.textwidget31 = tk.Label(self.input32,
                                     textvariable=self.SHA_output,
                                     background='black',
                                     foreground="white")
        self.textwidget31.pack(expand=1, fill="both", padx=5, pady=5)
        button31 = tk.Button(self.input31, text="Generate hash",
                             command=lambda: self.hash_sha256())
        button31.pack(side=tk.LEFT, padx=5, pady=5)
        button31.configure(background="black", foreground='white',
                           activebackground='#0080ff',
                           activeforeground='white')
    # ------------------------------- logic --------------------------------

    

    def hash_sha256(self):
        SHA_intput = self.textbox31.get("1.0", tk.END)
        hash_sum = hashlib.sha256(SHA_intput.encode('utf-8')).hexdigest()
        self.SHA_output.set(hash_sum)

    def active_tab(self):
        return self.notebook.index(self.notebook.select())
