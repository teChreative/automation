# See LinkedIn Learning
from multiprocessing.context import _default_context
import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('datafiles\regions.xlsx')
# df_csv = pd.read_csv('datafiles\Names.csv')
# df_txt = pd.read_csv('datafiles\data.txt')

print(df_excel)
