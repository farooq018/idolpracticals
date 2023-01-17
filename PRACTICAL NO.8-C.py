"""Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a constructor which takes the parameters x and y (these should all be numbers).
i. Write a method called add which returns the sum of the attributes x and y.
ii. Write a class method called multiply, which takes a single number parameter a and returns the product of a and MULTIPLIER.
iii. Write a static method called subtract, which takes two number parameters, b and c, and returns b - c.
iv. Write a method called value which returns a tuple containing the values of x and y. Make this method into a property, and write a setter and a deleter for manipulating the values of x and y"""


class Numbers:
    multiplier = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return cls.multiplier * a

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    # create a setter and deleter for a value.

    def setX(self, value):
        self.x = value

    def deleteX(self):
        del self.x

    def setY(self, value):
        self.y = value

    def delete(self):
        del self.y


num = Numbers(5, 5)
print(num.add())
print(num.multiply(5))
print(num.subtract(9, 2))
print("This program is done by 'Farooq Hussain'")