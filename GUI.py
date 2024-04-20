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
import pyautogui

class WindowManage:
    __slots__ = [
        # OPERATIONAL
        "main", "correctobj", "root", "ttk_style", "screensize",
        # FRAMES
        "frame1", "frame2", "frame3",
        # BUTTON
        "import_shp_button", "import_table_button"
        # RADIOBUTTON

        # TEXT BOX

        # SIMPLE TEXT

    ]

    def __init__(self, main) -> None:
        self.screensize = pyautogui.size()
        self.main = main
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
        self.root.title("GPR Correct Lines")
        self.root.wm_state("zoom")

        self.frame1 = ttk.Frame(self.root, 
                                width = self.screensize.width*.20, 
                                height = 50,
                                style="TFrame")
        self.frame2 = ttk.Frame(self.root, 
                                width = self.screensize.width*.20, 
                                height = 50,
                                style="TFrame")
        self.frame3 = ttk.Frame(self.root, 
                                width=self.screensize.width*.80,
                                height = 100,
                                style="TFrame")


        self.import_shp_button = ttk.Button(self.root,
                                            width=self.screensize.width*.20,
                                            text="Import line",
                                            command=lambda: self.main.get_shp_filepath(),
                                            style="Fun.TButton")
        self.import_table_button = ttk.Button(self.root,
                                              width=self.screensize.width*.20,
                                              text="Import data table",
                                              command=lambda: self.main.get_xl_filepath(),
                                              style="Fun.TButton")
        
        # gridding frames
        self.frame1.grid(row=0, column=0, rowspan=2, sticky="NESW")
        self.frame2.grid(row=2, column=0, rowspan=2, sticky="NESW")
        self.frame3.grid(row=0, column=1, rowspan=4, sticky="NESW")

        # gridding buttons
        self.import_shp_button.grid(row=0, column=0)
        self.import_table_button.grid(row=1, column=0)

    def set_styles(self):
        """
        Setting styles
        """
        self.ttk_style.configure("TFrame", relief="raised", background="white")
        self.ttk_style.configure("Fun.TButton", font="garamond 12")

    def rows_columns_configure(self):
        """
        for row in range(20):
            self.root.grid_rowconfigure(row, weight=1)
        for column in range(2):
            self.root.grid_columnconfigure(column, weight=1)"""
        self.root.grid_rowconfigure([0,1,2,3], weight=1)
        #self.root.grid_rowconfigure([2,3], weight=1)
        self.root.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    main = correct.Correct()
    WindowManage(main)