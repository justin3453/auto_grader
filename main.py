import os
import subprocess

file = "C:\\Users\\Justi\\PycharmProjects\\EECE2140_Final\\script.py"
# os.system(f"python {file} Justin")
result = subprocess.check_output(f'python {file} Justin')
a = [elm for elm in result.decode("UTF-8")]
result = result.decode("UTF-8").strip().strip()
print(result)

if result == "Hello my name is Justin.":
    print("Good")
else:
    print("Nope")

