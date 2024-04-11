import geopandas as gpd
import pandas as pd
import numpy as np
import tkinter.filedialog as fd
from shapely.geometry import LineString
import shapely

class App:
    def __init__(self, correctobj) -> None:
        self.correctobj = correctobj
        #self.shp_filepath = self.get_filepath(desc="Select the line shapefile", ftypes=[("shp", ".shp")])
        #self.xl_filepath = self.get_filepath(desc="Select the Excel file of GPR lines", ftypes=[("table", ".xlsx .csv")])
        self.shp_filepath = "input/example_gpr_lines.shp"
        self.xl_filepath = "input/example_excel.xlsx"

        self.line_shp = gpd.read_file(self.shp_filepath)
        self.line_shp = self.correct_format_df(self.line_shp)
        self.line_lengs = pd.read_excel(self.xl_filepath)
        self.line_lengs = self.correct_format_df(self.line_lengs)

        self.correct_lengs()

    def get_filepath(self, desc=str, ftypes=list):
        """
        Simple filedialog
        """
        return fd.askopenfilename(title=desc,
                                  filetypes=ftypes)
    
    def export_new_shp(self):
        pass

    def correct_format_df(self, df):
        df.columns = [column.lower() for column in df.columns]
        return df
    
    def correct_lengs(self):
        testdf = pd.merge(self.line_shp, self.line_lengs, how='inner', on="line")
        testdf["shp_len"] = np.round(testdf["geometry"].apply(shapely.length), 2)
        testdf = testdf.sort_values(by="line").reset_index(drop=True)
        print (testdf)
        
class Correct:
    def __init__(self) -> None:
        pass
    
if __name__ == "__main__":
    correctobj = Correct()
    app = App(correctobj)

    #print (app.line_lengs)
    #print (app.line_shp)