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
    # print(tmp,size)
    if(size == 1):
        tmp.insert(0,' ')
        tmp.append(' ')
    elif(size == 2):
        tmp.insert(0, ' ')
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


#global variables
instruction_table = loadInstructions("InstructionDictionary.txt")