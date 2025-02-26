# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:21:09 2025

@author: Isabelly
"""

import tkinter as tk
from tkinter import ttk, messagebox

class BaseApp(tk.Tk):
    """Classe base para todas as janelas"""
    def __init__(self, title, size="800x600"):
        super().__init__()
        self.title(title)
        self.geometry(size)
        self.configure(bg="#f8f9fa")

        # Adicionando compatibilidade de ícone para Linux
        try:
            self.iconphoto(False, tk.PhotoImage(file="software_assistant_icon.png"))
        except Exception as e:
            print("Ícone não carregado:", e)
