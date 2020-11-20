import xlrd
import pandas as pd
# import xlrd
#
# loc = "E:\dirc\Book1.xlsx"
# wb = xlrd.open_workbook(loc)
# sheet1 = wb.sheet_by_index(0)
# # cell1 = sheet1.cell_value(0, 0)
# # print(cell1)
# i = 0
# f = open("abc1.txt", "w")
# for i in range(0, 5):
#     cell1 = sheet1.cell_value(i, 0)
#     print(cell1)
#     f.write(cell1)
#
# f.close()
# print(sheet1.ncols)
# print(sheet1.nrows)

# loc = "F:\Exam\digikull_class\Files\Student_list.xlsx"
# wb = xlrd.open_workbook(loc)
# sheet_1 = wb.sheet_by_index(0)
# file1=open("exelfile.txt","w")
# i=2
# for i in range(2,8):
#     j=1
#     for j in range(1,4):
#         cell_content = sheet_1.cell_value(i, j)
#         print(cell_content)
#         file1.write(str(cell_content)+ "\t \t")
#     file1.write("\n")
# #df = pd.read_csv('exelfile.txt', sep='\s{1,}')
# #file1.writable('exelfile.txt')
# #print(df)
# file1.close()
# #print(sheet_1.nrows)
# #print(sheet_1.ncols)

loc = "E:\dirc\Book2.xlsx"
wb = xlrd.open_workbook(loc)
sheet1 = wb.sheet_by_index(0)
f = open("exelfile.txt","w")
# df = pd.read_excel("E:\dirc\Book2.xlsx")
# str_1 = "abc"
for i in range(0, sheet1.nrows):
    cell1 = sheet1.cell_value(i, 0)
    if "abc" in cell1:
       print(cell1)
       print(cell1.index("abc"))
       f.write(cell1 + "\n")

f.close()

