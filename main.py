from students import Student
from openpyxl import Workbook, load_workbook
import subprocess
import os


# Reads txt file where pre-defined input and expected output is stored
def get_input_output(file):
    with open(file, "r") as f:
        for line in f.readlines():
            f, ip, op = line.split("|")
            inputs.append(ip)
            output.append(op)


# Load excel file where course roster and students' assignments are stored
wb = load_workbook("Final_Project_Roster.xlsx")
ws = wb.active

# Student objects created will be stored in a dictionary
students = {}

# Creates Student objects using data from each row of the excel file
for row in ws.values:
    first, last, id, folder = row
    student = Student(first, last, id, folder)
    # Keeps header names out of the student dictionary
    if type(student.id) == int:
        students[student.id] = student




inputs = []
output = []
get_input_output("io.txt")
ip1 = inputs[0]
op1 = output[0]

programs = int(input("Enter number of assignments to grade:"))

for id, student in students.items():
    result = subprocess.check_output(f'python {student.scripts} {ip1}')
    result = result.decode("UTF-8").strip().strip()

    print(result)
    print(op1)
    if result == op1:
        student.add_points(100/programs)

print(students[11007])

