class Employee():
    no_of_leave=10
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    @classmethod
    def change_in_leave(cls,newleave):
        cls.no_of_leave=newleave


p=Employee("Farooq",15000,"Executive Engineer")
p.change_in_leave(200)
print(p.no_of_leave)
