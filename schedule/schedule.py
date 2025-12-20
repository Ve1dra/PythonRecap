from openpyxl import load_workbook

def calender():pass

file = "schedule_template_file.xlsx"
wb = load_workbook(filename=file)
sheet = wb.active
sheet['A1'] = 'New Value'
sheet.cell(row=2, column=2, value='Another Value')
new_roww_data = [1,2,3,4]
sheet.append(new_roww_data)
wb.save("schdule_template_file.xlsx")
