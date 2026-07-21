class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius


# take radius from user
r = float(input("Please enter the radius of the circle: "))
c = Circle(r)

print("Area:", c.area())
print("Perimeter:", c.perimeter())
