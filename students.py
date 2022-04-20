class Student:
    def __init__(self, first, last, id, scripts=""):
        """Initializes Student object"""
        self.first = first
        self.last = last
        self.id = id
        self.scripts = scripts
        self.grade = 0

    def add_points(self, amount):
        """Adds points to students' grade"""
        self.grade += amount

    def __str__(self):
        """Returns students' name and grade in string format"""
        return f"Name: {self.first} {self.last}\n" \
               f"Student ID: {self.id}\n" \
               f"Grade: {self.grade}\n\n"
    
    
