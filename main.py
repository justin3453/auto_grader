import subprocess
from students import Student


def get_input_output(file):
    with open(file, "r") as f:
        for line in f.readlines():
            f, ip, op = line.split("|")
            inputs.append(ip)
            output.append(op)


inputs = []
output = []
get_input_output("io.txt")
ip1 = inputs[0]
op1 = output[0]

programs = int(input("Enter number of assignments to grade:"))

s1 = Student("Mark", "Williams", 1007, "C:\\Users\\Justi\\PycharmProjects\\EECE2140_Final\\script.py")
students = {s1.id: s1}

for id, student in students.items():
    result = subprocess.check_output(f'python {student.scripts} {ip1}')
    result = result.decode("UTF-8").strip().strip()

    print(result)
    print(op1)
    if result == op1:
        student.add_points(100/programs)

print(s1.grade)
