from abstract_class import Shape


# sub class1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    # # 사용 예시
    circle = Circle(3)

    print(f"Circle area: {circle.area()}")
    print(f"Circle perimeter: {circle.perimeter()}")
