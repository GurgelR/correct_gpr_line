import geopandas as gpd
import pandas as pd
import numpy as np
import tkinter.filedialog as fd
from shapely.geometry import LineString
import shapely

class Main:
    """
    Designed for, in some future, create a GUI.
    """
    def __init__(self, correctobj) -> None:
        self.correctobj = correctobj
        self._main_init_()

    def _main_init_(self):
        if __name__ == "__main__":
           #self.correctobj = correctobj
            self.shp_filepath = self.get_filepath(desc="Select the line shapefile", ftypes=[("shp", ".shp")])
            self.xl_filepath = self.get_filepath(desc="Select the Excel file of GPR lines", ftypes=[("table", ".xlsx .csv")])
            self.exportpath = fd.askdirectory(title="Select the export location")
            #self.shp_filepath = "input/example_gpr_lines.shp"
            #self.xl_filepath = "input/example_excel.xlsx"

            self.line_shp = gpd.read_file(self.shp_filepath)
            self.line_shp = self.correctobj.correct_format_df(self.line_shp)
            self.line_lengs = self.read_table()
            self.line_lengs = self.correctobj.correct_format_df(self.line_lengs)

            self.new_lines = self.correctobj.correct_lines(self.line_shp, self.line_lengs)

            self.export_new_shp()

    def get_filepath(self, desc=str, ftypes=list):
        """
        Simple filedialog
        """
        return fd.askopenfilename(title=desc,
                                  filetypes=ftypes)
    
    def read_table(self):
        table_format = self.xl_filepath.split(".")[-1].upper()
        if table_format == "CSV":
            return pd.read_csv(self.xl_filepath, sep=";")
        elif table_format == "XLSX":
            return pd.read_excel(self.xl_filepath)
    
    def export_new_shp(self):
        """
        Exporting the corrected lines shape.
        """
        filename = self.shp_filepath.split("/")[-1].split(".")[-2] + "_RECTIF.shp"
        self.new_lines.to_file(self.exportpath + "/" + filename);

    def show_lines(self):
        """
        After all the correction operations, this will plot (matplotlib) everything and 
        show the original and corrected lines.

        Possibly, in some future, you'll be able to click on the line and see
        the actual changes, etc.
        """
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
        """
        Function to be applied within Correct.correct_lines in order to expand or reduce the GPR line.

        As it is intended to be used as np.vectorize function, it is recommended to be used as such,
        but can be edited.

        Input formats:
            pd.Series
        """
        vertex_coords = [shapely.get_point(line, n) for n in range(shapely.get_num_points(line))] # store the vertices coordinates
        vertex_positions = [np.round(line.line_locate_point(vertex_point), 2) for vertex_point in vertex_coords]
        vertex_array = np.array(list(zip(vertex_coords, vertex_positions)))

        if length > or_shp_len: # expand the shp line

            aux_line = LineString((vertex_coords[-2], vertex_coords[-1])) # auxiliar line to determine the position
                                                                          # where the extended line should be
            aux_line_len = shapely.length(aux_line)
            aux_line = shapely.affinity.scale(aux_line, xfact=10, yfact=10, origin=shapely.get_point(aux_line, 0))
            new_final_point = aux_line.interpolate(aux_line_len + (length - or_shp_len))
            
            new_vertex_array = np.vstack([vertex_array, np.array((new_final_point, length))])
            
            
            new_line = LineString(new_vertex_array[:,0])

            return new_line
        
        elif length < or_shp_len: # reduce the shp line -> ok
            
            new_final_point = line.interpolate(length) # getting the position along the line of the desired length
            new_vertex_array = vertex_array[vertex_array[:,1] < length] # excluding vertices after the disered final point
            new_vertex_array = np.vstack([new_vertex_array, np.array((new_final_point, length))]) # adding the last point
            new_line = LineString(new_vertex_array[:,0])

            return new_line

        else: # keep the line length
            return line

    def correct_lines(self, line_shp=gpd.GeoDataFrame, line_lengs=pd.DataFrame):

        
        or_df = pd.merge(line_shp, line_lengs, how='inner', on="line")
        or_df["or_shp_len"] = np.round(or_df["geometry"].apply(shapely.length), 2)
        
        or_df = or_df.sort_values(by="line").reset_index(drop=True)
        new_df = or_df # duplicate the df so the changes after the correction can be seen
        
        new_df["geometry"] = np.vectorize(self.expand_reduce)(or_df["geometry"], 
                                                              or_df["length (m)"], or_df["or_shp_len"])
        new_df["new_len"] = np.round(shapely.length(new_df["geometry"]), 2)
        #print (new_df[["length (m)", "or_shp_len", "new_len"]])
        return new_df

    def reverse_line (self, line):
        """
        If there is need to reverse the sense of some lines
        """
        return line.reverse()

if __name__ == "__main__":
    correctobj = Correct()
    main = Main(correctobj)