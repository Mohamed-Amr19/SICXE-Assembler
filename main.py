from SingletonTables import SingletonTables
from LineParser import * 
import Formatting
import sys

class FileWrapper(object):
    file_locations = str()
    opened_file = None
    new_file = []
    def __init__(self, file_locations):
        self.file_locations = file_locations
        try:
            self.opened_file = open(file_locations)
        except:
            print("File doesn't exist")
            exit()
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
        progName, directive, loc_counter = self.opened_file.readline().split()
        loc_counter = int(loc_counter,16)
        for line in self.opened_file.read().splitlines():
            #print(line.split())
            lineDirection = LineDirection(line.split(), loc_counter)
            self.new_file.append([hex(loc_counter),line.split()])
            loc_counter = lineDirection.getLocationCounter()
        self.opened_file.close()    
        # print(singletonTables.symbol_table)
        # print(singletonTables.literal_queue)
        print("Final Location: {}".format(hex(loc_counter)))
        #return opened_file.readline()
    def WriteFiles(self):
        tmp = open("out.txt", 'w')
        for element in self.new_file:
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
    



def main():
    if(len(sys.argv) == 1):
        tmp = FileWrapper(input("Available Example files: Example_1.txt, Example_2.txt, Example_Book_P94.txt\nEntire File name: "))
    else:
        args = sys.argv[1:]
        tmp = FileWrapper(args[0])
    tmp.LoadInstructions("InstructionDictionary.txt")
    #print(singletonTables.instruction_table)
    tmp.ParseLines()
    tmp.WriteFiles()
    #print(FileWrapper.opened_file.read())    #example file reading debug
    #singletonTables = SingletonTables.getInstance()
    #singletonTables.assignToSymbolTable("add",200)
    #print(singletonTables.getSymbolLocation("add"))   #symbol table search
    
    #singletonTables.printSymbolTable()
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
