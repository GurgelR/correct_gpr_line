import geopandas as gpd
import pandas as pd
import numpy as np
import tkinter.filedialog as fd
from shapely.geometry import LineString
import shapely

class App:
    """
    Designed for, in some future, create a GUI.
    """
    def __init__(self, correctobj) -> None:
        self.correctobj = correctobj
        #self.shp_filepath = self.get_filepath(desc="Select the line shapefile", ftypes=[("shp", ".shp")])
        #self.xl_filepath = self.get_filepath(desc="Select the Excel file of GPR lines", ftypes=[("table", ".xlsx .csv")])
        self.shp_filepath = "input/example_gpr_lines.shp"
        self.xl_filepath = "input/example_excel.xlsx"

        self.line_shp = gpd.read_file(self.shp_filepath)
        self.line_shp = self.correctobj.correct_format_df(self.line_shp)
        self.line_lengs = pd.read_excel(self.xl_filepath)
        self.line_lengs = self.correctobj.correct_format_df(self.line_lengs)

        self.correctobj.correct_lengs(self.line_shp, self.line_lengs)

    def get_filepath(self, desc=str, ftypes=list):
        """
        Simple filedialog
        """
        return fd.askopenfilename(title=desc,
                                  filetypes=ftypes)
    
    def export_new_shp(self):
        pass
        
class Correct:
    """
    Operations for correcting the shape lengths.
    """
    def __init__(self) -> None:
        pass

    def correct_format_df(self, df) -> gpd.GeoDataFrame:
        """
        Operations for formatting the pd.DataFrame and reduce the errors after this step
        """
        df.columns = [column.lower() for column in df.columns]
        return df

    def expand_line(self, expand_df, line_shp):
        """
        Operation for expanding the line, if it is smaller then the GPR section
        """
        pass

    def reduce_line(self, reduce_df, line_shp):
        """
        Operation for reducing the line, if it is bigger then the GPR section 
        """
        pass

    def check_lens(self, df):

        print (df["line"])

        pass

    def correct_lengs(self, line_shp=gpd.GeoDataFrame, line_lengs=pd.DataFrame):
        
        testdf = pd.merge(line_shp, line_lengs, how='inner', on="line")
        testdf["or_shp_len"] = np.round(testdf["geometry"].apply(shapely.length), 2)
        testdf = testdf.sort_values(by="line").reset_index(drop=True)
        
        testdf.apply(self.check_lens)

if __name__ == "__main__":
    correctobj = Correct()
    app = App(correctobj)

    #print (app.line_lengs)
    #print (app.line_shp)