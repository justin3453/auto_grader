from students import Student
from openpyxl import load_workbook
import subprocess
import os


# Reads txt file where pre-defined input and expected output is stored
# Creates a dictionary for the values
def get_input_output(file):
    d = {}
    with open(file, "r") as f:
        lines = 0
        for line in f.readlines():
            script, ip, op = line.split("|")
            d[script] = (ip, op)
            lines += 1
    return d, lines


# User must enter the complete file path
spreadsheet = input("Enter Excel file:")
io_file = input("Enter text file with i/o data:")

# Load Excel file where course roster and students' assignments are stored
wb = load_workbook(spreadsheet)
ws = wb.active

# Student objects created will be stored in a dictionary
students = {}

# Input and output will be stored in a dictionary
# The weight of each assignment is calculated dynamically
io, programs = get_input_output(io_file)

# Creates Student objects using data from each row of the Excel file
for row in ws.values:
    # Unpacks each row 
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
        correct = 0  # Counter for correctly made programs
        for script in assignments:
            # Name of each script must match the name written in the i/o txt file
            # Student will not receive credit if the file is named incorrectly
            try:
                ip, op = io[script]
            except:
                students[s].add_points(round(0))

            result = subprocess.check_output(f"python {path}\\{script} {ip}")  # Runs command in the terminal
            result = result.decode("UTF-8").strip()  # Formats the script's output
            f_out.write(f'{script}: {ip} >>> {result}\n')

            # If the output matches the desired result, points are added to grade
            if result in op:
                correct += 1
        students[s].add_points(round(100 * correct / programs))
        f_out.write("\n")

# Adds new column that contains all grades to spreadsheet
i = 2
ws["E1"] = "Grades"
for s in students:
    ws["E" + str(i)] = students[s].grade
    i += 1

# Save the Excel file
wb.save("roster.xlsx")
