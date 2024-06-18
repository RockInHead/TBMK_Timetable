# from Lessons import Lesson

# class Lesson:
#     # def __init__(self):
#     #     pass
#     def __init__(self,time="время по умолч",name="название по умолч",teacher="препод по умолч"):
#         self.time=time
#         self.name=name
#         self.teacher=teacher
#     # def __init__(self):
#     #     self.time='время по умолч'
#     #     self.name="название по умолч"
#     #     self.teacher="препод по умолч"
        
        
class Day:
    
    # def __init__(self):
    #     self.name="Любой день недели"
    #     self.lesson=("12:45","микробиология","Петрович")
    def __init__(self,name="День недели по умолчанию", lesson=None):
        self.name=name
        self.lesson=lesson