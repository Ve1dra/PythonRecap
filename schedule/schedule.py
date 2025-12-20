from openpyxl import load_workbook
# from time import ctime
def calender():pass

def schedule():
    file = "scheduleData.xlsx"
    wb = load_workbook(filename=file)
    sheet = wb.active
    # sheet['D1'] = 'Wednesday'
    # sheet.cell(row=2, column=2, value='Another Value')
    a=1
    while a:
        print("Enter 'done' to stop entering events")
        ent = str(input("Enter the event you plan to do: "))
        if ent == "exit".tolower():
            break
        elif '0' <= ent <= '9':
            print("Invalid Input")
        else:
            event = ent
            day = str(input("Enter the day this event would hold: "))
            time = day
            new_row_data = [time, event]
            sheet.append(new_row_data)
            wb.save("scheduleData.xlsx")
    wb.close()