# Implement the concept of inheritance using python.

class Base:
    def displayBase(self):
        print("Base Class")

class Derived(Base):
    def displayDerived(self):
        print("Derived Class")

obj=Derived()
obj.displayBase()
obj.displayDerived()

print("This program is done by 'Farooq Hussain'")