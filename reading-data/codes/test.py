## Assignment3 Solution
""" 
Author Name: Anbara Al-Jamal
Author ID: 150107
This code is available as an open-source file

"""
import csv_files_handler as cfh


## Testing for reading the files!

path =  "..\Data\Ch1\jump-olympics.csv"
df = cfh.read_csv_file(path)
print(df)

first = cfh.first_n_dps(df, 5)
print(first)

path1 =  "..\Data\Ch1\powerGain.xls"
df1 = cfh.read_excel_file(path1)
print(df1)

last = cfh.last_n_dps(df1, 5)
print(last)
 
path2 = "..\Data\Ch1\GLM_data.zip"
file_name = "GLM_data/Table 4.5 AIDS cases.xls"
df2 = cfh.read_from_zip(path2, file_name)
print(df2) 


path = "../Data/Ch1/test_matlab.mat"
data = cfh.read_mat(path)
outFile = "shape.png"
outDir = "..\Data\Ch1\shapes"


cfh.display_mat_plot(data, outDir, outFile)