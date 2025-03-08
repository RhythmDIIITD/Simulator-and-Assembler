inputfile = "bruh.txt"
outputfile = "C:/Users/Rhythm/Desktop/Group_071/automatedTesting/tests/traces/simple/simple_1.txt"

def files_are_identical(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line_number, (line1, line2) in enumerate(zip(f1, f2), start=1):
            if line1 != line2:
                print(f"Difference found at line {line_number}")
                print(f"{file1}: {line1.strip()}")
                print(f"{file2}: {line2.strip()}")
                return False
        return True

if files_are_identical(inputfile, outputfile):
    print("The files have the exact same content.")
else:
    print("The files do not have the same content.")
