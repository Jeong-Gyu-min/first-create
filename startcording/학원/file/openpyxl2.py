import openpyxl
file = "C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/input/df.xlsx"

workbook = openpyxl.load_workbook(file)
print(workbook)
# print(type(workbook))
# print(workbook.sheetnames)

# worksheet = workbook["Sheet1"]
# print(worksheet)
# print(worksheet.title)

# active_sheet = workbook.active
# print(active_sheet)