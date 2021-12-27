from FirstPassUtility import *


def firstPass(file_location):
    
    line_num = 0
    symbol_table = {}
    literal_table = {}
    opened_file = open(file_location)
    program_name, START, starting_address = getFirstLine(opened_file.readline()) 
    loc_counter = int(starting_address)             #Relocation stuff
    for line in opened_file.read().splitlines():    #read the label instruction target
        line_num += 1
        label, instruction, target = splitLine(line)    #label instructoin target are defined
        if(label != placeholder):
            symbol_table[label] = loc_counter

        print(hex(loc_counter),label,instruction,target)

        if(target[0] == '='): #check for literals
            target = target[1:]
            literal_table[label] = target
            print(target)
            continue
            # print(target)
        

        #handle WORD, BYTE, RESW, RESB and LTORG
        if(instruction == "WORD"):
            loc_counter += 3
        elif(instruction == "RESW"):
            loc_counter += int(target)*3                #we can add error handle here
        elif(instruction == "RESB"):
            loc_counter += int(target)
        elif(instruction == "BYTE"):
            loc_counter += convertOutliers(target)
        elif(instruction == 'LTORG'):
            if(target == '*'):
                loc_counter += getLiteralSize(literal_table)
                literal_table = {}
        elif(instruction == 'END'):
            if(literal_table=={}):
                loc_counter+=1
            loc_counter += getLiteralSize(literal_table)
            literal_table = {}
        else:
            loc_counter += getInstructionSize(instruction)
    print("final memory location: " + hex(loc_counter))
    #print(symbol_table)
    #print(literal_table)
    opened_file.close()    
        
firstPass("Example_Book_P94.txt")
# print(getInstructionSize("RSUB"))
#
# print(getFirstLine("test start 0"))
# print(splitLine("start"))