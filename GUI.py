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
        "main", "correctobj", "root", "style",
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
        self.set_styles()
        self.generate_interface()
        self.root.mainloop()
        
    def generate_interface(self):
        """
        Creating the user interface layout
        """
        self.frame1 = ttk.Frame(self.root, 
                                width = 200, 
                                height = 300)
        self.frame2 = ttk.Frame(self.root, 
                                width = 400, 
                                height = 300,)
        self.frame3 = ttk.Frame(self.root, 
                                width = 400, 
                                height = 300, 
                                borderwidth=5)
        self.frame1.grid(row=0, column=0, rowspan=15, columnspan=2)
        self.frame2.grid(row=2, column=0, rowspan=15, columnspan=2)
        self.frame3.grid(row=0, column=0, rowspan=30, columnspan=2)
        pass

    def set_styles(self):
        """
        Setting styles
        """
        ttk.Style().configure("TFrame", relief="flat", background="white")

if __name__ == "__main__":
    correctobj = correct.Correct()
    main = correct.Main(correctobj)
    WindowManage(main, correctobj)