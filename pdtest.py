import pandas as pd

file = 'C:/Users/lixin-lc/Desktop/新建文件夹/昆区第二轮.xlsx'
data = pd.read_excel(file)
# data = pd.read_csv( my_file.csv , sep= ; , encoding= latin-1 , nrows=1000, skiprows=[2,5])
print(data)
