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

        self.correctobj.correct_lines(self.line_shp, self.line_lengs)

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

    def get_az(self, line):
        """
        Probably will not be used in this code, but its goal is to calculate the
        azimuth of a line.
        """
        pass

    def correct_format_df(self, df) -> gpd.GeoDataFrame:
        """
        Operations for formatting the pd.DataFrame and reduce the errors after this step
        """
        df.columns = [column.lower() for column in df.columns]
        return df

    def expand_reduce(self, line, length, or_shp_len):
        vertex_coords = [shapely.get_point(line, n) for n in range(shapely.get_num_points(line))] # store the vertices coordinates
        vertex_positions = [np.round(line.line_locate_point(vertex_point), 2) for vertex_point in vertex_coords]
        vertex_array = np.array(list(zip(vertex_coords, vertex_positions)))

        if length > or_shp_len: # expand the shp line

            return line

        elif length < or_shp_len: # reduce the shp line -> ok
            
            new_final_point = line.interpolate(length)
            new_vertex_array = vertex_array[vertex_array[:,1] < length] # excluding vertices after the disered final point
            new_vertex_array = np.vstack([new_vertex_array, np.array((new_final_point, length))])

            return LineString(new_vertex_array[:,0])

        else: # keep the line length
            return line

        pass

    def correct_lines(self, line_shp=gpd.GeoDataFrame, line_lengs=pd.DataFrame):
        
        testdf = pd.merge(line_shp, line_lengs, how='inner', on="line")
        testdf["or_shp_len"] = np.round(testdf["geometry"].apply(shapely.length), 2)
        
        testdf = testdf.sort_values(by="line").reset_index(drop=True)
        #print (testdf["geometry"])
        print (np.vectorize(self.expand_reduce)(testdf["geometry"], testdf["length (m)"], testdf["or_shp_len"]))
        #testdf.apply(self.check_lens)


if __name__ == "__main__":
    correctobj = Correct()
    app = App(correctobj)