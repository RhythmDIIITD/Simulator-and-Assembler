
def readfile(file_path):
    list = []
    with open(file_path, "r") as file:
        for line in file:
            list.append(line.strip())
    
    return list

Binary_Address_to_CommonName_Dic = {
    "00000" : "x0",
    "00001" : "x1",
    "00010" : "x2",
    "00011" : "x3",
    "00100" : "x4",
    "00101" : "x5",
    "00110" : "x6",
    "00111" : "x7",
    "01000" : "x8",
    "01001" : "x9",
    "01010" : "x10",
    "01011" : "x11",
    "01100" : "x12",
    "01101" : "x13",
    "01110" : "x14",
    "01111" : "x15",
    "10000" : "x16",
    "10001" : "x17",
    "10010" : "x18",
    "10011" : "x19",
    "10100" : "x20",
    "10101" : "x21",
    "10110" : "x22",
    "10111" : "x23",
    "11000" : "x24",
    "11001" : "x25",
    "11010" : "x26",
    "11011" : "x27",
    "11100" : "x28",
    "11101" : "x29",
    "11110" : "x30",
    "11111" : "x31"}

Register_Value_Dictionary = {
    "x0" : "0",
    "x1" : "0",
    "x2" : "0",
    "x3" : "0",
    "x4" : "0",
    "x5" : "0",
    "x6" : "0",
    "x7" : "0",
    "x8" : "0",
    "x9" : "0",
    "x10" : "0",
    "x11" : "0",
    "x12" : "0",
    "x13" : "0",
    "x14" : "0",
    "x15" : "0",
    "x16" : "0",
    "x17" : "0",
    "x18" : "0",
    "x19" : "0",
    "x20" : "0",
    "x21" : "0",
    "x22" : "0",
    "x23" : "0",
    "x24" : "0",
    "x25" : "0",
    "x26" : "0",
    "x27" : "0",
    "x28" : "0",
    "x29" : "0",
    "x30" : "0",
    "x31" : "0"
}

Data_Memory_Dictionary = {
    "0x00010000" : "0",
    "0x00010004" : "0",
    "0x00010008" : "0",
    "0x0001000C" : "0",
    "0x00010010" : "0",
    "0x00010014" : "0",
    "0x00010018" : "0",
    "0x0001001C" : "0",
    "0x00010020" : "0",
    "0x00010024" : "0",
    "0x00010028" : "0",
    "0x0001002C" : "0",
    "0x00010030" : "0",
    "0x00010034" : "0",
    "0x00010038" : "0",
    "0x0001003C" : "0",
    "0x00010040" : "0",
    "0x00010044" : "0",
    "0x00010048" : "0",
    "0x0001004C" : "0",
    "0x00010050" : "0",
    "0x00010054" : "0",
    "0x00010058" : "0",
    "0x0001005C" : "0",
    "0x00010060" : "0",
    "0x00010064" : "0",
    "0x00010068" : "0",
    "0x0001006C" : "0",
    "0x00010070" : "0",
    "0x00010074" : "0",
    "0x00010078" : "0",
    "0x0001007C" : "0"
}

def Identify_Intrusction_Dictionary(string):
    func3 = string[17:20]
    opcode = string[25:32] 

    if func3 == "000" and opcode == "0110011":
        if string[0:7] == "0000000":
            return "add"
        elif string[0:7] == "0100000":
            return "sub"
    elif func3 == "010" and opcode == "0110011":
        return "slt"
    elif func3 == "101" and opcode == "0110011":
        return "srl"
    elif func3 == "110" and opcode == "0110011":
        return "or"
    elif func3 == "111" and opcode == "0110011":
        return "and"
    elif func3 == "000" and opcode == "0010011":
        return "addi"
    elif func3 == "010" and opcode == "0000011":
        return "lw"
    elif func3 == "000" and opcode == "1100111":
        return "jalr"
    elif func3 == "010" and opcode == "0100011":
        return "sw"
    elif func3 == "000" and opcode == "1100011":
        return "beq"
    elif func3 == "001" and opcode == "1100011":
        return "bne"
    elif func3 == "100" and opcode == "1100011":
        return "blt"
    elif opcode == "1101111":
        return "jal"
    else:
        return "error"
    
def instructioncreation(list):
    Instructionrecognised = []
    for instruction in list:
        Instructionrecognised.append(Identify_Intrusction_Dictionary(instruction))
    return Instructionrecognised
    
Trace_list = []
instruction_list = readfile("simple_5.txt")
print(instruction_list)

Written_Instruction_List = instructioncreation(instruction_list)
print(Written_Instruction_List)

def decimaltobinary(number):
    number = int(number)
    if number<0:
        binary = format((1<<32)+number,"032b")
    else:
        binary = format(number, "032b")
    return binary

def PC_dictionary(listwritten):
    PC = 0
    PC_Dictionary = {}
    for i in range(len(listwritten)):
        PC_Dictionary[i] = PC
        PC = PC + 4
    return PC_Dictionary

def Instruction_Executor(listbinary, listwritten):
    for i in range(len(listbinary)):

        if listwritten[i] == "add":
            PC = PC_list[i]
            add(listbinary[i])
        elif listwritten[i] == "sub":
            PC = PC_list[i]
            sub(listbinary[i])
        elif listwritten[i] == "slt":
            PC = PC_list[i]
            slt(listbinary[i])
        elif listwritten[i] == "srl":
            PC = PC_list[i]
            srl(listbinary[i])
        elif listwritten[i] == "or":
            PC = PC_list[i]
            orfunction(listbinary[i])
        elif listwritten[i] == "and":
            PC = PC_list[i]
            andfunction(listbinary[i])
        elif listwritten[i] == "addi":
            PC = PC_list[i]
            addi(listbinary[i])
        elif listwritten[i] == "lw":
            PC = PC_list[i]
            lw(listbinary[i])
        elif listwritten[i] == "jalr":
            PC = PC_list[i]
            jalr(listbinary[i])
        elif listwritten[i] == "sw":
            PC = PC_list[i]
            sw(listbinary[i])
        elif listwritten[i] == "beq":
            PC = PC_list[i]
            beq(listbinary[i])
        elif listwritten[i] == "bne":
            PC = PC_list[i]
            bne(listbinary[i])
        elif listwritten[i] == "blt":
            PC = PC_list[i]
            blt(listbinary[i])
        elif listwritten[i] == "jal":
            PC = PC_list[i]
            jal(listbinary[i])
        else:
            errorinstructionnotfound()

        Trace_list.append(display_register_values(PC, Register_Value_Dictionary))

PC_list = PC_dictionary(Written_Instruction_List)
print(PC_list)
def display_register_values(PC, Register_Value_Dictionary):
    string = "0b" + decimaltobinary(PC) + " "
    count = 2
    for key, value in Register_Value_Dictionary.items():
        if count == 4:
            string = string + "0b" + decimaltobinary(value) + "\n"
            count = 1
        else:
            string = string + "0b" + decimaltobinary(value) + " "
            count = count+1

    string = string + "\n"
    return string

def add(string):
    rd = Binary_Address_to_CommonName_Dic[string[20:25]]
    rs1 = Binary_Address_to_CommonName_Dic[string[12:17]]
    rs2 = Binary_Address_to_CommonName_Dic[string[7:12]]
    rd_value = int(Register_Value_Dictionary[rs1]) + int(Register_Value_Dictionary[rs2])
    Register_Value_Dictionary[rd] = str(rd_value)
    Register_Value_Dictionary["x0"] = "0"
    return

def sub(string):
    rd = Binary_Address_to_CommonName_Dic[string[20:25]]
    rs1 = Binary_Address_to_CommonName_Dic[string[12:17]]
    rs2 = Binary_Address_to_CommonName_Dic[string[7:12]]
    rd_value = int(Register_Value_Dictionary[rs1]) - int(Register_Value_Dictionary[rs2])
    Register_Value_Dictionary[rd] = str(rd_value)
    Register_Value_Dictionary["x0"] = "0"
    return

def slt(string):
    rd = Binary_Address_to_CommonName_Dic[string[20:25]]
    rs1 = Binary_Address_to_CommonName_Dic[string[12:17]]
    rs2 = Binary_Address_to_CommonName_Dic[string[7:12]]
    if int(Register_Value_Dictionary[rs1]) < int(Register_Value_Dictionary[rs2]):
        rd_value = 1
    else:
        rd_value = 0
    Register_Value_Dictionary[rd] = str(rd_value)
    Register_Value_Dictionary["x0"] = "0"
    return

def srl(string):
    rd = Binary_Address_to_CommonName_Dic[string[20:25]]
    rs1 = Binary_Address_to_CommonName_Dic[string[12:17]]
    rs2 = Binary_Address_to_CommonName_Dic[string[7:12]]
    rd_value = int(Register_Value_Dictionary[rs1])//(2**(min(int(Register_Value_Dictionary[rs2]), 31)))
    Register_Value_Dictionary[rd] = str(rd_value)
    Register_Value_Dictionary["x0"] = "0"
    return
def twos_complement(string):
    num_bits = len(string)
    integer = int(string, 2)

    if string[0] == '1':
        integer -= 2**num_bits
    return integer

def orfunction(string):
    rd = Binary_Address_to_CommonName_Dic[string[20:25]]
    rs1 = Binary_Address_to_CommonName_Dic[string[12:17]]
    rs2 = Binary_Address_to_CommonName_Dic[string[7:12]]
    rs1_binary = decimaltobinary(int(Register_Value_Dictionary[rs1]))
    rs2_binary = decimaltobinary(int(Register_Value_Dictionary[rs2]))
    rd_value = ""
    for i in range(len(rs2_binary)):
        if rs2_binary[i] == "1" and rs1_binary[i] == "1":
            rd_value = rd_value + "1"
        elif rs2_binary[i] == "1" and rs1_binary[i] == "0":
            rd_value = rd_value + "1"
        elif rs2_binary[i] == "0" and rs1_binary[i] == "1":
            rd_value = rd_value + "1"
        else:
            rd_value = rd_value + "0"
    Register_Value_Dictionary[rd] = str(twos_complement(rd_value))
    Register_Value_Dictionary["x0"] = "0"
    return

def andfunction(string):
    rd = Binary_Address_to_CommonName_Dic[string[20:25]]
    rs1 = Binary_Address_to_CommonName_Dic[string[12:17]]
    rs2 = Binary_Address_to_CommonName_Dic[string[7:12]]
    rs1_binary = decimaltobinary(int(Register_Value_Dictionary[rs1]))
    rs2_binary = decimaltobinary(int(Register_Value_Dictionary[rs2]))
    rd_value = ""
    for i in range(len(rs2_binary)):
        if rs2_binary[i] == "1" and rs1_binary[i] == "1":
            rd_value = rd_value + "1"
        elif rs2_binary[i] == "1" and rs1_binary[i] == "0":
            rd_value = rd_value + "0"
        elif rs2_binary[i] == "0" and rs1_binary[i] == "1":
            rd_value = rd_value + "0"
        else:
            rd_value = rd_value + "0"
    Register_Value_Dictionary[rd] = str(twos_complement(rd_value))
    Register_Value_Dictionary["x0"] = "0"
    return

def addi(string):
    rd = Binary_Address_to_CommonName_Dic[string[20:25]]
    rs1 = Binary_Address_to_CommonName_Dic[string[12:17]]
    immediate = twos_complement(string[0:12])


    rd_value = int(Register_Value_Dictionary[rs1]) + immediate
    Register_Value_Dictionary[rd] = str(rd_value)
    Register_Value_Dictionary["x0"] = "0"
    return

def decimaltohex(string):
    string = format(string & 0xFFFFFFFF, '08x')
    string = "0x" + string
    return string

def lw(string):
    rd = Binary_Address_to_CommonName_Dic[string[20:25]]
    rs1 = Binary_Address_to_CommonName_Dic[string[12:17]]
    immediate = twos_complement(string[0:12])


    memory_adress_integer = int(Register_Value_Dictionary[rs1]) + immediate
    memory_adress = decimaltohex(memory_adress_integer)
    data_from_memory = Data_Memory_Dictionary[memory_adress]
    Register_Value_Dictionary[rd] = data_from_memory
    Register_Value_Dictionary["x0"] = "0"
    return

def jalr(string):
    pass

def sw(string):
    pass

def beq(string):

    pass

def bne(string):

    pass

def blt(string):

    pass

def jal(string):

    pass

def errorinstructionnotfound():

    print("error: instruction not found")



Instruction_Executor(instruction_list, Written_Instruction_List)
Final_Memory_list = []
def display_register_values(list):

    for key, value in Data_Memory_Dictionary.items():
        string = key + ":" + "0b" + decimaltobinary(value)
        list.append(string)

    return

display_register_values(Final_Memory_list)

def outputfile(file_path,list1,list2):
    with open(file_path, "w") as file:
        for line in list1:
                file.write(line)
                print("")
        for line in list2:
                file.write(line)
                file.write("\n")
        
    return


outputfile("simple_1_output.txt", Trace_list,Final_Memory_list)