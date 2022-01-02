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
    if(len(line.split()) != 3):
        print("First line error, missing parameters")
        exit()
    if START != "START":
        print("first line error: no start")
        exit()
    first_line.append(program_name)
    first_line.append(starting_address)
    return program_name, START, starting_address

def WriteFiles(self):
        output = open("out.txt", 'w')

def getInstructionSize(instruction):
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
def byte_length(i):
        return (i.bit_length() + 7) // 8
def convertOutliers(target):
    if(target[0].upper() == 'C'):
        return len(target.split('\'')[1])
    elif(target[0].upper() == 'X'):
        return byte_length(int(target.split('\'')[1],16))
    else:
        return byte_length(int(target[0]))

def getLiteralSize(literal_table):
    size = 0
    for element in literal_table:
        size += literal_table.get(element)[1] 
    return size
def generateLiterals(literal_table,tmp_literals, FirstPass_output,loc):
    for literal in tmp_literals:
        FirstPass_output.append([hex(loc),placeholder,placeholder,tmp_literals.get(literal)[2]])
        # print(literal_table[literal][0])
        literal_table[literal][0] = hex(loc)
        loc += literal_table[literal][1]
    return loc
def identifyData(star):
    if(',' in star):
        arr = star.split(',')
        output = ''
        for ch in arr:
            if(ch[0].upper() == 'C'):
                dat = hex(ord(ch[2]))[2:]
                for ch in ch[3:-1]:
                    dat += hex(ord(ch))[2:]
                output+= dat
            elif(ch[0].upper() == 'X'):
                output+= ch[2:-1]
        return output
    elif(star[0].upper() == 'C'):
        dat = hex(ord(star[2]))[2:]
        for ch in star[3:-1]:
            dat += hex(ord(ch))[2:]
        return dat
    elif(star[0].upper() == 'X'):
        return star[2:-1]
    else:
        return hex(int(star))[2:]


#global variables
instruction_table = loadInstructions("InstructionDictionary.txt")
special_instructions = ['+','$','&']
reserved = ["BASE","RESW","RESB","WORD","BYTE","END","LTORG","EXTREF","EXTDEF","EQU"]
registers = {"A":"0","X":"1","L":"2","B":"3","S":"4","T":"5","F":"6"}
placeholder = '-'
skipper = '?'
seperator = '.'
padding = '_'
first_line = []