# from SingletonTables import SingletonTables
from FirstPass import FirstPass
# from LineParser import * 
import Formatting #has not been implemented 
import sys

def main():
    #making the first SIC/XE Pass    
    if(len(sys.argv) == 1):
        tmp = FirstPass(input("Available Example files: Example_1.txt, Example_2.txt, Example_Book_P94.txt\nEntire File name: "))
    else:
        args = sys.argv[1:]
        tmp = FirstPass(args[0])
    # tmp.LoadInstructions("InstructionDictionary.txt")
    #print(singletonTables.instruction_table)
    # tmp.ParseLines()
    
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
