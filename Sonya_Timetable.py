import openpyxl #Импортируем библиотеку для чтения эксель файлов
from Сlasses.DayOfWeek import Day #Импортируем класс Дней недели
from Сlasses.Lessons import Lesson #Импортируем класс Уроков недели

#Monday = Day("Понедельник",Lesson("12:45",'Какой-то урок',"Петрович"))
#print(Monday.lesson.teacher)

file=openpyxl.open("Data\Расписание.xlsx",read_only=True) # Считываем эксель файл
sheet=file.active #Выбираем актвну страницу по умолчанию

def CreateDate(day_line,day_column):
   
    for i in range(day_line,day_line+6):
        for d in range(day_column,27):
            if(sheet[i][d].value)==None:
                return "Смотри прошлый месяц"
                
            elif  "июня" in str(sheet[i][d].value) and ("-" in str(sheet[i][d].value))!=True:
                return sheet[i][d].value

Week=[]
Lessons=[]
day=[]
time=[]



# days_row=26
# for i in range(1,50):
#     if(sheet[i][days_row].value)!=None:
        
#         for t in range(i,i+6):
#             if(sheet[t][days_row+1].value)!=None:
#                 time.append(sheet[t][days_row+1].value)
#             else:
#                 time.append(sheet[t+1][days_row+1].value)
       
#         day.append(sheet[i][days_row].value)
#         day.append(CreateDate(i,days_row+22))
#         # day.append(sheet[i][days_row+22].value)
#         day.append(time)
        
#         Week.append(day)
#         day=[]
#         time=[]
#     for j in range(0,27):
#         if(sheet[i][j].value=="дни"):
#             days_row=j
#             break

# for someDay in Week:
#     for times in someDay:
#         print(times)

WeekDays =[]

days_row=26
days_line=50
for i in range(1,50):
    for j in range(0,27):
        if(sheet[i][j].value=="дни"):
            dayOfWeek_row_start=j+1
            dayOfWeek_line_start=i+1
            break

dictinory={1:"A",2:"B",3:"C",4:'D',5:"E",6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
weekDaysCell=sheet[f"{dictinory[dayOfWeek_row_start]}{dayOfWeek_line_start}":"B49"]

for name,time in weekDaysCell:
    print(name.value,time.value)


# for i in range(1,50):
#     day = Day()
#     if(sheet[i-days_line][days_row].value)!=None:
#         day.name=sheet[days_line][days_row].value
#         WeekDays.append(day)

        





# print(CreateDate(44,8))

# for i in range(1,50):
#     print(sheet[i][days_row].value)
        


#Сначала строка, потом столбец
#Строки считаются с 1, а ряды с 0!!!