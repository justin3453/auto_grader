from students import Student
from openpyxl import Workbook, load_workbook
import subprocess
import os


# Reads txt file where pre-defined input and expected output is stored
# Creates a dictionary for the values
def get_input_output(file):
    d = {}
    with open(file, "r") as f:
        for line in f.readlines():
            f, ip, op = line.split("|")
            d[f] = (ip, op)
    return d


programs = int(input("Enter number of assignments to grade:"))

# Load excel file where course roster and students' assignments are stored
wb = load_workbook("Final_Project_Roster.xlsx")
ws = wb.active

# Student objects created will be stored in a dictionary
students = {}

# Input and output will be stored in a dictionary
io = get_input_output("io.txt")

# Creates Student objects using data from each row of the excel file
for row in ws.values:
    first, last, id, folder = row
    student = Student(first, last, id, folder)
    # Keeps header names out of the student dictionary
    if type(student.id) == int:
        students[student.id] = student

for s in students:
    assignments = os.listdir(students[s].scripts)
    path = os.path.abspath(students[s].scripts)
    for script in assignments:
        ip, op = io[script]
        result = subprocess.check_output(f'python {path}\\{script} {ip}')
        result = result.decode("UTF-8").strip().strip()
        print(result)
        print(op)
        if result == op:
            students[s].add_points(int(100 / programs))


print(students[11007])


