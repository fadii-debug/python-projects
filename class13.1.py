class Shape:
    def area():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return f"area of circle is  {3.14*self.radius*self.radius}"

class Rectangle(Shape):
    def __init__(self, length, wedth):
        self.wedth=wedth
        self.length=length
    def area(self):
        return self.wedth*self.length
    
list1=[Circle(5), Rectangle(2,3)]
for i in list1:
    print(i.area())