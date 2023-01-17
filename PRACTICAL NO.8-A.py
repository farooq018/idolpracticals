# Design a class that store the information of student and display the same.

class Student:
    def studentinfo(self,name,rollno,address):
        print("Name=",name)
        print("Roll no=",rollno)
        print("Address=",address)

obj=Student()
obj.studentinfo("Farooq Hussain","0786","Jogeshwari")