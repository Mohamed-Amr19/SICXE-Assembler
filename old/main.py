from SingletonTables import Library
from FirstPass import FirstPass
from ProgramCounter import ProgramCounter
# from LineParser import * 
import Formatting #has not been implemented 
import sys
programCounter = ProgramCounter.getInstance()
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
    singletonTables = Library.getInstance()
    print(singletonTables.symbol_table)
    tmp.secondPass()
    programCounter.printArray()
    tmp.WriteFiles()
    
    # programCounter.getBase()
    # programCounter.resetStartingAddress()
    # for i in range(len(programCounter.line_array)-1):
    #     line = programCounter.current_line
    #     programCounter.calculateAddresses()
    #     # print(hex(line.target_obj.address))
    #     line.generateObjectCode()
        # print("{}|{}".format(hex(line.loc_counter),line.object_code))
        #print(line.target_obj.address)
        # print("{}\t{}\t{}".format(hex(line.loc_counter),line.flags,hex(line.target_obj.address)))
    # tmp.secondPass()
    # for i in ProgramCounter.line_array:
    #     print("{} {} {}".format(hex(i.loc_counter),i.flags,i.calculateAddress()))
    
    
    #print(FileWrapper.opened_file.read())    #example file reading debug
    
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
