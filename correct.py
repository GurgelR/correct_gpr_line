import geopandas as gpd
import pandas as pd
import numpy as np
import tkinter.filedialog as fd 

class App:
    def __init__(self, correctobj) -> None:
        self.shp_filepath = self.get_filepath(desc="Select the line shapefile", ftypes=[("shp", ".shp")])
        self.xl_filepath = self.get_filepath(desc="Select the Excel file of GPR lines", ftypes=[("table", ".xlsx .csv")])

    def get_filepath(self, desc=str, ftypes=list):
        """
        Simple filedialog
        """
        return fd.askopenfilename(title=desc,
                                  filetypes=ftypes)
    
    def export_new_shp(self):
        pass
        
class Correct:
    def __init__(self) -> None:
        pass

    def read_shp(self,shp_filepath):
        return gpd.read_file(shp_filepath)

    def read_xl(self,filepath):
        return pd.read_excel(filepath)
    


if __name__ == "__main__":
    correctobj = Correct()
    app = App(correctobj)