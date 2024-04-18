"""
This file will be used to creating the GUI (Guided User Interface) of the program
so the user can visualize the original and corrected lines, invert the sense of 
lines or whatsoever within the main window.

It will call the functions created and implemented in "correct.py"
"""

from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


from tkinter import filedialog as fd

import correct

class WindowManage:
    __slots__ = [
        # OPERATIONAL
        "main", "correctobj", "root", "ttk_style",
        # FRAMES
        "frame1", "frame2", "frame3"
        # BUTTON

        # RADIOBUTTON

        # TEXT BOX

        # SIMPLE TEXT

    ]

    def __init__(self, main, correctobj) -> None:
        self.main = main
        self.correctobj = correctobj
        self.root = Tk()
        self.ttk_style = ttk.Style()
        self.set_styles()
        self.rows_columns_configure()
        self.generate_interface()
        self.root.mainloop()
        
    def generate_interface(self):
        """
        Creating the user interface layout
        """
        self.frame1 = ttk.Frame(self.root, 
                                width = 100, 
                                height = 100,
                                style="TFrame")
        self.frame2 = ttk.Frame(self.root, 
                                width = 100, 
                                height = 100,
                                style="TFrame")
        self.frame3 = ttk.Frame(self.root, 
                                width = 100, 
                                height = 100, 
                                borderwidth=50,
                                style="TFrame")
        self.frame1.grid(row=0, column=0, rowspan=15, columnspan=1, sticky="NESW")
        self.frame2.grid(row=15, column=0, rowspan=15, columnspan=1, sticky="NESW")
        self.frame3.grid(row=0, column=1, rowspan=30, columnspan=2, sticky="NESW")
        

    def set_styles(self):
        """
        Setting styles
        """
        self.ttk_style.configure("TFrame", relief="raised", background="white")

    def rows_columns_configure(self):
        for row in range(20):
            self.root.grid_rowconfigure(row, weight=1)
        for column in range(2):
            self.root.columnconfigure(column, weight=1)

if __name__ == "__main__":
    correctobj = correct.Correct()
    main = correct.Main(correctobj)
    WindowManage(main, correctobj)