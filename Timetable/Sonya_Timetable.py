import openpyxl

file=openpyxl.open("Расписание.xlsx",read_only=True)
sheet=file.active

days_row=26
for i in range(1,50):
    print(sheet[i][days_row].value)
    for j in range(0,27):
        if(sheet[i][j].value=="дни"):
            days_row=j
        
        

#Сначала строка, потом столбец
#Строки считаются с 1, а ряды с 0!!!