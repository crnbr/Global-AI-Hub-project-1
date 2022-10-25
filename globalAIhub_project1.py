#Add the libraries you will use.
import pandas as pd

#Create a system where you can enter Student Information (Name, Surname, School Number, exam score) and keep this information.
class LectureStatus():
  def __init__(self, lecture, stu_name, stu_surname, stu_number, points):
    self.lecture = lecture
    self.stu_name = stu_name
    self.stu_surname = stu_surname
    self.stu_number = stu_number
    self.points = points
    self.grade = 0
    self.status = 0

#Converting scores to letter grades, determining pass/fail status
  def compute_grade(self):
    points = self.points
    if points >= 90:
      self.grade = 'A' 
      self.status = 'Passed'
    elif points >= 60:
      self.grade = 'B' 
      self.status = 'Passed'
    elif points >= 40:
      self.grade = 'C' 
      self.status = 'Passed'
    elif points >= 20:
      self.grade = 'D' 
      self.status = 'Failed'
    else:
      self.grade ='F'
      self.status = 'Failed'

#result message
  def result_message(self):
    if (self.grade <= 'C'):
      print(f"""Congratulations, you passed! {self.stu_name} scored {self.points}/100 points in {self.lecture} and got the letter {self.grade}.""")
    else:
      print(f""" You failed the {self.lecture}! Try again next semester {self.stu_name} scored {self.points}/100 points in {self.lecture} and got the letter {self.grade}.""")

#Result summary
  def results(self):
    
    results = []
    results.append((self.stu_name, self.lecture,self.grade, self.status))
    print(results)


#Creating Dataframe with Child class
class Students(LectureStatus):
    def __init__(self, student_list = []):
        self.student_list = student_list
    
    #Dataframe creation
    def df_create(self):
        student_dict = dict()
        id = 1
        for student in self.student_list:
            stu = [student.stu_name, student.stu_surname, student.stu_number, student.lecture, student.points, student.grade, student.status]
            student_dict[id] = stu
            id += 1
        df = pd.DataFrame.from_dict(student_dict, orient = 'index', columns = ['Name', 'Surname', 'Number', 'Lecture', 'Points', 'Grade', 'Status'])
        return df


#student 1
stu1 = LectureStatus('Math','Ben', 'Walt', 12345678, 16)
stu1.compute_grade()
stu1.result_message()
stu1.results()


#student 2
stu2 = LectureStatus('Math','John', 'Smith', 11234567, 66)
stu2.compute_grade()
stu2.result_message()
stu2.results()


#student 3
stu3 = LectureStatus('Chemistry','Anna', 'Barbez', 11123456, 88)
stu3.compute_grade()
stu3.result_message()
stu3.results()


#student 4
stu4 = LectureStatus('History','Ellen', 'Poet', 11112345, 26)
stu4.compute_grade()
stu4.result_message()
stu4.results()


#Keep students in array
student_arr = [stu1, stu2, stu3, stu4]
classroom = Students(student_arr)
df_classroom = classroom.df_create()
#Print dataframe
df_classroom


#Creating excel file for dataframe
writer = pd.ExcelWriter('status_excel.xlsx')



#Write dataframe to excel 
df_classroom.to_excel(writer)
 
#save excel file
writer.save()
print("DataFrame is exported successfully to 'converted-to-excel.xlsx' Excel File.")



