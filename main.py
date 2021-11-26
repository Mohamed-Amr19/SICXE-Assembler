from SingletonTables import SingletonTables
from LineParser import LineParser
from Formatting import Formatting


class FileWrapper(object):
    file_locations = str()
    opened_file = None
    def __init__(self, file_locations):
        self.file_locations = file_locations
        opened_file = open(file_locations)
        tmp = opened_file.read() 
        print(tmp)
        print("__init__")
    
    def LoadInstructions(DictionaryLocation):
        for line in (open(DictionaryLocation).read().splitlines()):
            instruction, instruction_format , opcode = line.split()
            #print(instruction,instruction_format,opcode)
            #SingletonTables=SigneltonTables.SingeltonTables
            SingletonTables.instruction_table[instruction]= [instruction_format, opcode]

    def ParseLines():#increment ?
        global loc_counter
        print("ParseLines")
        return opened_file.readline()
    def WriteFile(self):
        print("WriteFile")
    def WriteLine(self):
        print("WriteLine")



loc_counter = 0
def main():
    tmp = FileWrapper("example_2.txt")
    #print(FileWrapper.opened_file.read())    #example file reading debug
    singletonTables = SingletonTables()
    #singletonTables.assignToSymbolTable("add",200)
    #print(singletonTables.getSymbolLocation("add"))   #symbol table search
    FileWrapper.LoadInstructions("InstructionDictionary.txt")
    #print(SingletonTables.instruction_table)       #instruction pring table debug


if __name__ == "__main__":
    main()