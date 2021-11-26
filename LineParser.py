#from main import SingletonTables

class Symbol(object):
    symbol_name = str()
    symbol_loc = int()
    def __init__(self, name, loc): #initializes its variables then calls assignSymbol
        self.symbol_name = name
        self.symbol_loc = loc
        assignSymbol()
        print("__init__")
    def assignSymbol(self): # calls SingletonTables.assignSymbolTable() to add itself
        SingletonTables.assignToSymbolTable(self.symbol_name,symbol_loc)
        print("assignSymbol")

class Instruction(object): #
    instruction_name = str()
    opcode = int() #will need to be hex
    instruction_format = None # should be initialized from Formatting.py
    byte_size = None
    def __init__(self, instruction_name):
        self.instruction_name = instruction_name
        instruction_format, opcode = SingletonTables.InstructionDictionary[self.instruction_name]
        print("__init__")
    def checkInstruction(self, instruction_name): #probably obsolete
        print("CheckInstruction")
    def getInstructionSize(self): #calls instruction_format.byte_size
        printf("getInstructionSize")

class Addressed(object):
    address_prefix = str()
    content = None
    def __init__(self, content):
        address_prefix = content[0]
        self.content = content.split(',')
        tempor,asd
        print("__init__")
    def DetermineContent(self): #checks if it's a single string or an array of string
        print("DetermineContent")

class LineDirection(object):
    symbol_obj = None
    instruction_obj = None
    address_obj = None
    flags = int()
    is_faulty = bool()
    errors = str()
    def __init__(self, str): #initializes these objects, then calls singletonTables.assignSymbolTable()
        print("__init__")
    def checkLen(self):#checks how many strings
        print("checkLen")
    def initSymbol(self,symbol_name):#may have unique logic before creating symbol object
        print("initSymbol")
    def initInstruction(self,instruction_name):#calls singletonTable to get the instruction Opcode to save it in instruction_obj
        #may have unique logic before creating instruction object
        print("initInstruction")
    def initAddressed(self,adressed_name):#may have unique logic before creating address object
        print("initAdressed")
    def setFlags(self):#not now
        print("setFlags")
    def incrementLocationCounter(self): #adds instruction_obj.format.byte_size to the current location counter
        print("incrementLocationCounter")