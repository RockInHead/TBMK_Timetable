import openpyxl
from Сlasses.DayOfWeek import Day #Импортируем класс Дней недели
from Сlasses.Lessons import Lesson

Monday = Day("Понедельник",Lesson("12:45",'Какой-то урок',"Петрович"))



print(Monday.lesson.name)

#file=openpyxl.open("Расписание.xlsx",read_only=True)
#sheet=file.active

# days_row=26
# for i in range(1,50):
#     print(sheet[i][days_row].value)
#     for j in range(0,27):
#         if(sheet[i][j].value=="дни"):
#             days_row=j
        


#Сначала строка, потом столбец
#Строки считаются с 1, а ряды с 0!!!