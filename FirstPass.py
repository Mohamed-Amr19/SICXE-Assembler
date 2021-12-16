from SingletonTables import Library
from LineParser import * 
singletonTables = Library.getInstance()
from ProgramCounter import ProgramCounter
programCounter = ProgramCounter()
class FirstPass(object):
    file_locations = str()
    opened_file = None
    array = []
    def __init__(self, file_locations, DictionaryLocation = "InstructionDictionary.txt"):
        self.file_locations = file_locations
        try:
            self.opened_file = open(file_locations)
        except:
            print("File doesn't exist")
            exit()
        #do the first pass 
        #first load instructions
        try:
            self.LoadInstructions(DictionaryLocation)
        except: #if dictionary doesn't exist program terminates.
            print("InstructionDictionary.txt file not found, exiting.")
            exit()
        #second going through each line and assigning program counter
        self.ParseLines()
        #tmp = self.opened_file.read() 
        #print(tmp)
        #print("__init__")
    
    def LoadInstructions(self,DictionaryLocation):
        for line in (open(DictionaryLocation).read().splitlines()):
            instruction, instruction_format , opcode = line.split()
            instruction_format = int(instruction_format)
            #print(instruction,instruction_format,opcode)
            #SingletonTables=singletonTables
            singletonTables.instruction_table[instruction]= [instruction_format, opcode]

    def ParseLines(self): #increment ?
       # global loc_counter
        progName, directive, programCounter.starting_address = self.opened_file.readline().split()
        programCounter.starting_address = int(programCounter.starting_address,16)
        programCounter.loc_counter = programCounter.starting_address
        for line in self.opened_file.read().splitlines():
            #print(line.split())
            directLine = Line(line.split(), programCounter.loc_counter)
            self.array.append([hex(programCounter.loc_counter),line.split()])
            # programCounter.loc_counter = line.getLocationCounter()
            programCounter.addLine(directLine)
        self.opened_file.close()    
        for line in programCounter.line_array:
            print("{} {}".format(hex(line.loc_counter), line.flags))
        # print(singletonTables.symbol_table)
        # print(singletonTables.literal_queue)
        print("Final Location: {}".format(hex(programCounter.loc_counter)))
        #return opened_file.readline()
    def WriteFiles(self):
        tmp = open("out.txt", 'w')
        for element in self.array:
            st = element[0],'|', *element[1]
            tmp.write("\t".join(st))
            tmp.write("\n")
        tmp.close()
        tmp = open("SymbolTable.txt",'w')
        for element in singletonTables.symbol_table:
            st = element, '|', hex(singletonTables.symbol_table[element])
            #print("\t".join(st))
            tmp.write("\t".join(st))
            tmp.write("\n")
        tmp.close()
            #print(element)
        #print("WriteFile")
    def WriteLine(self):
        print("WriteLine")