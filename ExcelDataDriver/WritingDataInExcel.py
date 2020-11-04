import openpyxl
path = "Excel file location"
work_book = openpyxl.load_workbook(path)
sheet = work_book.active

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row = r,column = c).value = "Welcome"

work_book.save(path)
print("succesfull")
