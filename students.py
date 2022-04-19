class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.grade = 100
        self.scripts = []

    def deduct_points(self, amount):
        self.grade -= amount
        