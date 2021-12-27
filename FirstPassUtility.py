def loadInstructions(DictionaryLocation):
    instruction_table = {}
    for line in (open(DictionaryLocation).read().splitlines()):
        instruction, instruction_format , opcode = line.split()
        instruction_format = int(instruction_format)
        opcode = int(opcode,16)
        instruction_table[instruction]= [instruction_format, opcode]
    return instruction_table

def splitLine(line):
    tmp = line.upper().split()
    size = len(tmp)
    
    if(size == 1):
        tmp.insert(0,placeholder)
        tmp.append(placeholder)
    elif(size == 2):
        tmp.insert(0, placeholder)
    elif( size > 3):
        print("line contains more than 3 words")
        exit()
    return tmp

def getFirstLine(line):
    program_name, START, starting_address = line.upper().split()
    if START != "START":
        print("first line error: no start")
        exit()
    return program_name, START, starting_address

def WriteFiles(self):
        output = open("out.txt", 'w')

def getInstructionSize(instruction):
    # global(instructio)
    format_flag = ' '
    if(instruction[0] in special_instructions):
        format_flag = instruction[0]
        instruction = instruction[1:]
    format = instruction_table.get(instruction.upper(),-1)
    if(format != -1):
        if(format_flag == '+'):
            return format[0] + 1 #return the type of format 4
        elif(format_flag == '$'):
            return format[0] + 1
        return format[0]            #return the type of format 1 or 2 or 3
    else:
        print(instruction + " Instruction not found,exiting")
        exit()

def convertOutliers(target):
    print("rem"+target)
    def byte_length(i):
        return (i.bit_length() + 7) // 8
    if(target[0].upper() == 'C'):
        #print("herere")
        return len(target.split('\'')[1])
    elif(target[0].upper() == 'X'):
        return byte_length(int(target.split('\'')[1],16))
    else:
        return byte_length(int(target[0]))

def getLiteralSize(literal_table):
    size = 0
    for element in literal_table:
        size += convertOutliers(literal_table.get(element))
    print(size)
    return size
#global variables
instruction_table = loadInstructions("InstructionDictionary.txt")
special_instructions = ['+','$','#']
placeholder = '-'
# print(instruction_table)