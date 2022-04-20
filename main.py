from students import Student
from openpyxl import load_workbook
import subprocess
import os


# Reads txt file where pre-defined input and expected output is stored
# Creates a dictionary for the values
def get_input_output(file):
    d = {}
    with open(file, "r") as f:
        for line in f.readlines():
            script, ip, op = line.split("|")
            d[script] = (ip, op)
    return d


programs = int(input("Enter number of assignments to grade:"))

# Load Excel file where course roster and students' assignments are stored
wb = load_workbook("Final_Project_Roster.xlsx")
ws = wb.active

# Student objects created will be stored in a dictionary
students = {}

# Input and output will be stored in a dictionary
io = get_input_output("io.txt")

# Creates Student objects using data from each row of the Excel file
for row in ws.values:
    first, last, id, folder, *data = row
    student = Student(first.strip(), last.strip(), id, folder)
    # Keeps header names out of the student dictionary
    if type(student.id) == int:
        students[student.id] = student


with open("output.txt", 'w') as f_out:
    # Iterates over student dictionary
    for s in students:
        assignments = os.listdir(students[s].scripts)  # List of programs
        path = os.path.abspath(students[s].scripts)  # File path for folder
        f_out.write(f'{students[s].first} {students[s].last}:\n')
        # Executes each one of the students' scripts
        for script in assignments:
            ip, op = io[script]
            result = subprocess.check_output(f'python {path}\\{script} {ip}')  # Runs command in the terminal
            result = result.decode("UTF-8").strip()  # Formats the script's output
            f_out.write(f'{script}: {ip} >>> {result}\n')

            # If the output matches the desired result, points are added to grade
            if result in op:
                students[s].add_points(round(100 / programs))
            f_out.write(f"{students[s].grade}\n")
        f_out.write("\n")

# Adds new column that contains all grades to spreadsheet
i = 2
ws["E1"] = "Grades"
for s in students:
    ws["E" + str(i)] = students[s].grade
    i += 1

# Save the Excel file
wb.save("Final_Project_Roster.xlsx")


