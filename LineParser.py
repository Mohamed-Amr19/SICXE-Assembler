from SingletonTables import SingletonTables
from math import floor
singletonTables = SingletonTables.getInstance()
class Symbol(object):
    symbol_name = str()
    symbol_loc = int()
    def __init__(self, name, loc): #initializes its variables then calls assignSymbol
        self.symbol_name = name
        self.symbol_loc = loc
        self.assignSymbol()
        #print("__init__")
    def assignSymbol(self): # calls SingletonTables.assignSymbolTable() to add itself
        singletonTables.assignToSymbolTable(self.symbol_name,self.symbol_loc)
        #print("assignSymbol")
class Literal(object):#needs refactoring
    literal_name = str()
    literal_loc = int()
    literal_size = int()
    def __init__(self, literal_name, literal_loc,literal_size):
        self.literal_name = literal_name
        self.literal_loc = literal_loc
        self.literal_size = literal_size
        self.assignLiteral()
        #print("Literally")
    def assignLiteral(self): 
        singletonTables.enqueueLiteral(self.literal_name, hex(self.literal_loc),self.literal_size)

class Instruction(object): #
    instruction_name = str()
    format_char = str()
    opcode = int() #will need to be hex
    instruction_format = int() # should be initialized from Formatting.py
    byte_size = None
    def __init__(self, instruction_name,format_char = None):
        self.format_char = format_char
        self.instruction_name = instruction_name
        self.instruction_format, self.opcode = singletonTables.instruction_table.get(self.instruction_name)
        #print("inst format {}".format(self.instruction_format))
        #print("__init__")
    def checkInstruction(self, instruction_name): #probably obsolete
        print("CheckInstruction")
    def getInstructionSize(self): #calls instruction_format.byte_size
        printf("getInstructionSize")
    def getInstructionFormat():
        print("it's not 0 yet")
        print(self.instruction_format)
        return self.instruction_format

class Addressed(object):
    address_prefix = str()
    content = None
    def __init__(self, content, address_prefix):
        self.address_prefix = address_prefix
        self.content = content.split(',')
    def DetermineContent(self): #checks if it's a single string or an array of string
        print("DetermineContent")

class LineDirection(object):
    loc_counter = None
    symbol_obj = None
    instruction_obj = None
    addressed_obj = None
    flags = int()
    is_faulty = bool()
    errors = str()
    def __init__(self, str_arr, loc_counter): #initializes these objects, then calls singletonTables.assignSymbolTable()
        self.loc_counter = loc_counter
        if(len(str_arr) == 1):
            self.symbol_obj = None
            self.instruction_obj = self.initInstruction(str_arr[0])
            self.addressed_obj = None
        elif(len(str_arr) == 2): #error handling needed
            self.symbol_obj = None
            self.instruction_obj = self.initInstruction(str_arr[0])
            self.addressed_obj = self.initAddressed(str_arr[1])
        else:
            self.symbol_obj = self.initSymbol(str_arr[0],loc_counter)
            self.instruction_obj = self.initInstruction(str_arr[1])
            self.addressed_obj = self.initAddressed(str_arr[2])
        #if(self.addressed_obj.address_prefix == '='):
        #    self.initLiteral(literal_name, loc_counter)
        #print("__init__")
    def checkLen(self):#checks how many strings
        print("checkLen")
    def initSymbol(self,symbol_name, loc_counter):#may have unique logic before creating symbol object
        if symbol_name == ' ':
            return None
        return Symbol(symbol_name,loc_counter)
        #print("initSymbol")
    def initLiteral(self, literal_name, loc_counter,size): #needs refactoring
        if literal_name == ' ':
            return None
        return Literal(literal_name, loc_counter,size)
    def initInstruction(self,instruction_name):#calls singletonTable to get the instruction Opcode to save it in instruction_obj
        if(singletonTables.unique_instruction_table.get(instruction_name[0],-1) != -1): #error
            #print(instruction_name[1:], instruction_name[0])
            return Instruction(instruction_name[1:], instruction_name[0])
        return Instruction(instruction_name)
        #may have unique logic before creating instruction object
        #print("initInstruction")
    def initAddressed(self,adressed_name):#may have unique logic before creating address object
        if(adressed_name == ' '):
            return None
        elif(singletonTables.unique_addressed_table.get(adressed_name[0],0) != 0 ):    
            #print(adressed_name[0])
            if(adressed_name[0] == '='):
                self.initLiteral(adressed_name[1:],self.loc_counter,self.convertOutliers(adressed_name[1:]))
            return Addressed(adressed_name[1:],adressed_name[0])
        return Addressed(adressed_name,0)
        #print("initAdressed")
    def byte_length(self,i):
        return (i.bit_length() + 7) // 8

    def convertOutliers(self,addressed):
        if(addressed[0].upper() == 'C'):
            #print("herere")
            return len(addressed.split('\'')[1])
        elif(addressed[0].upper() == 'X'):
            return self.byte_length(int(addressed.split('\'')[1],16))
        else:
            return self.byte_length(int(addressed[0]))
    def setFlags(self):#not now
        print("setFlags")
    def getLocationCounter(self): #adds instruction_obj.format.byte_size to the current location counter
        #if(singletonTables.directive_table.get(self.instruction_obj.instruction_name,-1) != -1):
            #return self.loc_counter + singletonTables.directive_table.get(self.instruction_obj.instruction_name) + self.convertOutliers(self.addressed_obj.content)
        if(self.instruction_obj.instruction_name.upper() == 'WORD'):
            return (self.loc_counter + 3)
        elif (self.instruction_obj.instruction_name.upper() == 'BYTE'):
                #if(self.convertOutliers(self.addressed_obj.content) > 3) 
            return (self.loc_counter + self.convertOutliers(self.addressed_obj.content[0]))
        elif(self.instruction_obj.instruction_name.upper() == 'RESW'):
            return (self.loc_counter + 3*int(self.addressed_obj.content[0]))
        elif(self.instruction_obj.instruction_name.upper() == 'RESB'):
            return (self.loc_counter +int(self.addressed_obj.content[0]))
        elif(self.instruction_obj.instruction_name.upper() == 'LTORG' or self.instruction_obj.instruction_name.upper() == 'END'):
            return(self.loc_counter + singletonTables.getLiteralSize())
        #print("2nd: {} 3rd: {}".format(type(self.instruction_obj.instruction_format),type(singletonTables.unique_instruction_table.get(self.instruction_obj.format_char,0))))
        return (self.loc_counter + self.instruction_obj.instruction_format + singletonTables.unique_instruction_table.get(self.instruction_obj.format_char,0))
        #print("incrementLocationCounter")