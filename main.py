from SingletonTables import SingletonTables
from LineParser import * 
import Formatting


class FileWrapper(object):
    file_locations = str()
    opened_file = None
    def __init__(self, file_locations):
        self.file_locations = file_locations
        self.opened_file = open(file_locations)
        #tmp = self.opened_file.read() 
        #print(tmp)
        print("__init__")
    
    def LoadInstructions(self,DictionaryLocation):
        for line in (open(DictionaryLocation).read().splitlines()):
            instruction, instruction_format , opcode = line.split()
            instruction_format = int(instruction_format)
            #print(instruction,instruction_format,opcode)
            #SingletonTables=singletonTables
            singletonTables.instruction_table[instruction]= [instruction_format, opcode]

    def ParseLines(self): #increment ?
       # global loc_counter
        progName, directive, loc_counter = self.opened_file.readline().split()
        loc_counter = int(loc_counter)
        for line in self.opened_file.read().splitlines():
            #print(line.split())
            lineDirection = LineDirection(line.split(), loc_counter)
            print("{} {}".format(loc_counter,line.split()))
            loc_counter = lineDirection.getLocationCounter()
        print(singletonTables.symbol_table)
        print(hex(loc_counter))
        #return opened_file.readline()
    def WriteFile(self):
        print("WriteFile")
    def WriteLine(self):
        print("WriteLine")
    



def main():
    #loc_counter = 1000
    tmp = FileWrapper("example_2.txt")
    
    #print(FileWrapper.opened_file.read())    #example file reading debug
    #singletonTables = SingletonTables.getInstance()
    #singletonTables.assignToSymbolTable("add",200)
    #print(singletonTables.getSymbolLocation("add"))   #symbol table search
    tmp.LoadInstructions("InstructionDictionary.txt")
    #print(singletonTables.instruction_table)
    tmp.ParseLines()
    #print(SingletonTables.instruction_table)       #instruction pring table debug
    #print(singletonTables.instruction_table["ADD"])
    #temp = Instruction("ADD")
    #print(temp.instruction_format)
    #print(temp.opcode)
    #lineDirection = LineDirection("LENGTH RESB C'F122'".split(),loc_counter)
    #print(lineDirection.instruction_obj.instruction_name)
    #print(singletonTables.instruction_table)
    #loc_counter = lineDirection.getLocationCounter()
    #print(singletonTables.symbol_table)
    #print(loc_counter)


if __name__ == "__main__":
    main()
