import re
import sys

def readfile(file_path):
    lst = []
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                words = re.sub(r"\((\w+)\)", r" \1 ", line.strip().replace(",", " "))
                words = re.sub(r"(\w+:)(\w+)", r"\1 \2", words).split()
                lst.append(words)
    
    return lst

def outputfile(file_path,list):
    with open(file_path, "w") as file:
        for line in list:
            if list.index(line) == len(list)-1:
                file.write(line.strip())
            else:
                file.write(line.strip() + "\n")
    return




def labelmaker(list):
    labels = {}
    pc = 0
    for i in range(len(list)):
        if len(list[i])>0 and ":" in list[i][0]:
            labels[list[i][0]] = pc
        pc = pc+ 1

    return labels


Dictionary_of_instruction = {
    "R-type": {
        "add": {"func7": "0000000", "func3": "000", "opcode": "0110011"},
        "sub": {"func7": "0100000", "func3": "000", "opcode": "0110011"},
        "slt": {"func7": "0000000", "func3": "010", "opcode": "0110011"},
        "srl": {"func7": "0000000", "func3": "101", "opcode": "0110011"},
        "or": {"func7": "0000000", "func3": "110", "opcode": "0110011"},
        "and": {"func7": "0000000", "func3": "111", "opcode": "0110011"},
        #BONUS
        #BONUS
        #BONUS
        "mul": {"func7": "0000001", "func3": "000", "opcode": "0110011"},
        #BONUS
        #BONUS
        #BONUS
    },
    "I-type": {
        "addi": {"func3": "000", "opcode": "0010011"},
        "lw": {"func3": "010", "opcode": "0000011"},
        "jalr": {"func3": "000", "opcode": "1100111"}
    },
    "S-type": {
        "sw": {"func3": "010", "opcode": "0100011"},
    },
    "B-type": {
        "beq": {"func3": "000", "opcode": "1100011"},
        "bne": {"func3": "001", "opcode": "1100011"},
        "blt": {"func3": "100", "opcode": "1100011"}
    },
    "J-type": {
        "jal": {"opcode": "1101111"}
    },
    #BONUS
    #BONUS
    #BONUS
    "Bonus-Type": {
        "rst": {"opcode": "0000000", "func3": "001", "func7": "0000000"},
        "halt": {"opcode": "0000000", "func3": "010", "func7": "0000000"}
    },

    "Reverse-Type": {
        "rvrs": {"opcode": "0000000", "func3": "011", "func7": "0000000"}
    }

    #BONUS
    #BONUS
    #BONUS
}

Register_dictionary = {
    "x0": "00000", "zero": "00000",
    "x1": "00001", "ra": "00001",
    "x2": "00010", "sp": "00010",
    "x3": "00011", "gp": "00011",
    "x4": "00100", "tp": "00100",
    "x5": "00101", "t0": "00101",
    "x6": "00110", "t1": "00110",
    "x7": "00111", "t2": "00111",
    "x8": "01000", "s0": "01000",
    "x9": "01001", "s1": "01001",
    "x10": "01010", "a0": "01010",
    "x11": "01011", "a1": "01011",
    "x12": "01100", "a2": "01100",
    "x13": "01101", "a3": "01101",
    "x14": "01110", "a4": "01110",
    "x15": "01111", "a5": "01111",
    "x16": "10000", "a6": "10000",
    "x17": "10001", "a7": "10001",
    "x18": "10010", "s2": "10010",
    "x19": "10011", "s3": "10011",
    "x20": "10100", "s4": "10100",
    "x21": "10101", "s5": "10101",
    "x22": "10110", "s6": "10110",
    "x23": "10111", "s7": "10111",
    "x24": "11000", "s8": "11000",
    "x25": "11001", "s9": "11001",
    "x26": "11010", "s10": "11010",
    "x27": "11011", "s11": "11011",
    "x28": "11100", "t3": "11100",
    "x29": "11101", "t4": "11101",
    "x30": "11110", "t5": "11110",
    "x31": "11111", "t6": "11111"
}

def decimaltobinary(number):
    number = int(number)
    if number<0:
        binary = format((1<<12)+number,"012b")
    else:
        binary = format(number, "012b")
    return binary

def decimaltobinaryforb(number):
    number = int(number)
    if number<0:
        binary = format((1<<12)+number,"012b")
    else:
        binary = format(number, "012b")
    return binary

def decimaltobinaryforbb(number):
    number = int(number)
    if number<0:
        binary = format((1<<13)+number,"013b")
    else:
        binary = format(number, "013b")
    return binary
def type_recognition(line,pc):
    strippedstring = ""
    for ch in line[0]:
        if ch.isalpha():
            strippedstring = strippedstring + ch

    if strippedstring in Dictionary_of_instruction["R-type"]:
        return binary_r(line)
    elif strippedstring in Dictionary_of_instruction["I-type"]:
        if strippedstring == "lw":
            return binary_i_normal(line)
        else:
            return binary_i_weird(line)
    elif strippedstring in Dictionary_of_instruction["S-type"]:
        return binary_s(line)
    elif strippedstring in Dictionary_of_instruction["B-type"]:
        return binary_b(line, pc)
    elif strippedstring in Dictionary_of_instruction["J-type"]:
        return binary_j(line, pc)
    #BONUS
    #BONUS
    #BONUS
    elif strippedstring in Dictionary_of_instruction["Bonus-Type"]:
        return binary_bonus(line)
    
    elif strippedstring in Dictionary_of_instruction["Reverse-Type"]:
        return binary_reversal(line)
    #BONUS
    #BONUS
    #BONUS
    elif ":" in strippedstring:
        return "label"
    else:
        
        return "error"



        
def binary_r(line):
    string = ""
    string = string + Dictionary_of_instruction["R-type"][line[0]]["func7"]
    string = string + Register_dictionary[line[3]]
    string = string + Register_dictionary[line[2]]
    string = string + Dictionary_of_instruction["R-type"][line[0]]["func3"]
    string = string + Register_dictionary[line[1]]
    string = string + Dictionary_of_instruction["R-type"][line[0]]["opcode"]
    return string

#BONUS
#BONUS
#BONUS
def binary_bonus(line):
    string = ""
    string = string + Dictionary_of_instruction["Bonus-Type"][line[0]]["func7"]
    string = string  + "00000"
    string = string + "00000"
    string = string + Dictionary_of_instruction["Bonus-Type"][line[0]]["func3"]
    string = string + "00000"
    string = string + Dictionary_of_instruction["Bonus-Type"][line[0]]["opcode"]
    return string

def binary_reversal(line):
    string = ""
    string = string + Dictionary_of_instruction["Reverse-Type"][line[0]]["func7"]
    string = string  + "00000"
    string = string + Register_dictionary[line[2]]
    string = string + Dictionary_of_instruction["Reverse-Type"][line[0]]["func3"]
    string = string + Register_dictionary[line[1]]
    string = string + Dictionary_of_instruction["Reverse-Type"][line[0]]["opcode"]
    return string

#BONUS
#BONUS
#BONUS

def binary_i_normal(line):
    string = ""
    string = string + decimaltobinary(line[2])
    string = string + Register_dictionary[line[3]]
    string = string + Dictionary_of_instruction["I-type"][line[0]]["func3"]
    string = string + Register_dictionary[line[1]]
    string = string + Dictionary_of_instruction["I-type"][line[0]]["opcode"]
    return string

def binary_i_weird(line):
    string = ""
    string = string + decimaltobinary(line[3])[-12:]
    string = string + Register_dictionary[line[2]]
    string = string + Dictionary_of_instruction["I-type"][line[0]]["func3"]
    string = string + Register_dictionary[line[1]]
    string = string + Dictionary_of_instruction["I-type"][line[0]]["opcode"]
    return string

def binary_s(line):
    string = ""
    imm = decimaltobinary(line[2])
    string = string + imm[0:7]
    string = string + Register_dictionary[line[1]]
    string = string + Register_dictionary[line[3]]
    string = string + Dictionary_of_instruction["S-type"][line[0]]["func3"]
    string = string + imm[7:12]
    string = string + Dictionary_of_instruction["S-type"][line[0]]["opcode"]
    return string

def binary_b(line,pc):
    string = ""
    if (line[3]+":") in labels:
        target_pc = labels[(line[3]+":")]
        current_pc = pc

        line[3] = 2*(target_pc - current_pc)
        imm = decimaltobinaryforb(line[3])
        string = string + imm[0] + imm[2:8]
        string = string + Register_dictionary[line[2]]
        string = string + Register_dictionary[line[1]]
        string = string + Dictionary_of_instruction["B-type"][line[0]]["func3"]
        string = string + imm[8:] + imm[1]
        string = string + Dictionary_of_instruction["B-type"][line[0]]["opcode"]
        return string
    else:
        line[3] = int(line[3])//2
        imm = decimaltobinaryforb(line[3])
        string = string + imm[0] + imm[2:8]
        string = string + Register_dictionary[line[2]]
        string = string + Register_dictionary[line[1]]
        string = string + Dictionary_of_instruction["B-type"][line[0]]["func3"]
        string = string + imm[8:] + imm[1]
        string = string + Dictionary_of_instruction["B-type"][line[0]]["opcode"]
        return string


def decimaltobinaryforj(number):
    number = int(number)
    if number<0:
        binary = format((1<<20)+number,"020b")
    else:
        binary = format(number, "020b")
    return binary


def binary_j(line,pc):
    if (line[2]+":") in labels:
        target_pc = labels[(line[2]+":")]
        current_pc = pc

        line[2] = 2*(target_pc - current_pc)
        string = ""
        imm = decimaltobinaryforj(line[2])
        string = string + imm[0]
        string = string + imm[10:] 
        string = string + imm[9]
        string = string + imm[1:9]
        string = string + Register_dictionary[line[1]]
        string = string + Dictionary_of_instruction["J-type"][line[0]]["opcode"]
        return string

    else:
        string = ""
        line[2] = int(line[2])//2
        imm = decimaltobinaryforj(line[2])

        string = string + imm[0] 
        string = string + imm[10:]
        string = string + imm[9]
        string = string + imm[1:9]
        string = string + Register_dictionary[line[1]]
        string = string + Dictionary_of_instruction["J-type"][line[0]]["opcode"]
        return string



def labelprocessor(list):
    for line in list:
        if len(line)>0 and line[0] in labels:
            line.remove(line[0])
    return list


def error(line):
    string = ""

    return string

def virtualhaultcheck(list):
    if list[-1]==['beq', 'zero', 'zero', '0']:
        return 0
    else:
        string = "Error: Last Line is not Virtual Hault\nErrorLocation: Line "
        return string
    
def instructionnameerror(list):
    for line in list:
        strippedstring = ""
        for ch in line[0]:
            if ch.isalpha():
                strippedstring = strippedstring + ch

        if strippedstring in Dictionary_of_instruction["R-type"]:
            if line[1] not in Register_dictionary or line[2] not in Register_dictionary or line[3] not in Register_dictionary:
                string = "Error: Incorrect Paramters Given(Check register name or position again)\nError Location: Line number "+ str(list.index(line)+1)
                return string
            else:
                continue
        elif strippedstring in Dictionary_of_instruction["I-type"]:
            if strippedstring == "lw":
                    if line[1] not in Register_dictionary or line[3] not in Register_dictionary:
                        string = "Error: Incorrect Paramters Given(Check register name or position again)\nError Location: Line number " + str(list.index(line)+1)
                        return string
                    else:
                        continue
                    
            else:
                    if line[1] not in Register_dictionary or line[2] not in Register_dictionary:
                        string = "Error: Incorrect Paramters Given(Check register name or position again)\nError Location: Line number " + str(list.index(line)+1)
                        return string
                    else:
                        continue



        elif strippedstring in Dictionary_of_instruction["S-type"]:
            if line[1] not in Register_dictionary or line[3] not in Register_dictionary:
                string = "Error: Incorrect Paramters Given(Check register name or position again)\nError Location: Line number " + str(list.index(line)+1)
                return string
            else:
                continue
        elif strippedstring in Dictionary_of_instruction["B-type"]:
            if line[1] not in Register_dictionary or line[2] not in Register_dictionary:
                string = "Error: Incorrect Paramters Given(Check register name or position again)\nError Location: Line number "+ str(list.index(line)+1)
                return string
            else:
                continue
        elif strippedstring in Dictionary_of_instruction["J-type"]:
            if line[1] not in Register_dictionary:
                string = "Error: Incorrect Paramters Given(Check register name or position again)\nError Location: Line number " + str(list.index(line)+1)
                return string
            else:
                continue
        #BONUS
        #BONUS
        #BONUS
        elif strippedstring in Dictionary_of_instruction["Bonus-Type"]:
            continue
        elif strippedstring in Dictionary_of_instruction["Reverse-Type"]:
            if line[1] not in Register_dictionary or line[2] not in Register_dictionary:
                string = "Error: Incorrect Paramters Given(Check register name or position again)\nError Location: Line number "+ str(list.index(line)+1)
                return string
            else:
                continue
        #BONUS
        #BONUS
        #BONUS
        elif ":" in strippedstring:
            continue
        else:
            string = "Error: Incorrect Paramters Given(Check register name or position again)\nError Location: Line number " + str(list.index(line)+1)
            return string
    return 0


if len(sys.argv) != 3:
    print("Usage: python Assembler.py <input_file> <output_file>")
    sys.exit(1)

file_path = sys.argv[1] 
outputfilepath = sys.argv[2]   


list = readfile(file_path)
labels = labelmaker(list)
list = labelprocessor(list)


error_message = instructionnameerror(list)
answer = []
if error_message != 0:
    answer.append(error_message)
else:
    
    halt_error_message = virtualhaultcheck(list)
    
    if halt_error_message == 0:
        pc = 0
        for line in list:
            answer.append(type_recognition(line, pc))
            pc += 1
    else:
        answer.append(halt_error_message, len(list))

outputfile(outputfilepath,answer)