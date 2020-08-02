from tabula import convert_into
from tabula import read_pdf
import pandas as pd
import re 



def extractTable(f_path, filename):    
    filepath = f_path + filename
    # convert the pdf into comma separted file (CSV) using tabula's method.
    convert_into(filepath, "createFiles/data.csv", output_format="csv", pages = "all")

    # read same csv file as pandas dataframe.
    df = pd.read_csv("createFiles/data.csv")

    # remove all the columns having all the values as NULL.
    df1 = df.dropna(axis="columns", how = "all")

    # remove all the rows having any value as NULL.
    df2 = df1.dropna(axis="rows", how = "any")

    # drop first column names as '# Questions'.
    df3 = df2.drop("# Questions", axis = 1)

    # reset index to start from 0.
    df3.reset_index(drop=True, inplace=True)

    df4 = df3    
    df4['A'] = df4['A'].apply(lambda x:re.sub(r'\([^)]*\)', "", x)) 
    df4['B'] = df4['B'].apply(lambda x:re.sub(r'\([^)]*\)', "", x)) 
    df4['C'] = df4['C'].apply(lambda x:re.sub(r'\([^)]*\)', "", x)) 
    df4['D'] = df4['D'].apply(lambda x:re.sub(r'\([^)]*\)', "", x)) 
    df4['E'] = df4['E'].apply(lambda x:re.sub(r'\([^)]*\)', "", x))

    df4.index = df4.index + 1
    df4_out = df4.stack()
    df4_out.index = df4_out.index.map('{0[1]}_{0[0]}'.format)
    df5 = df4_out.to_frame().T


    df5.to_csv('createFiles/'+filename+'.csv', index= False, header = False)