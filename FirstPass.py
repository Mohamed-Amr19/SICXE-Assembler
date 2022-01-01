from FirstPassUtility import *

#variables needed in pass 2
symbol_table = {}
literal_table = {}
tmp_literals = {}
FirstPass_output = []
    
def FirstPass(file_location):
    #variables needed for pass 2
    line_num = 0
    printable_table = []
    base_loc = 0
    base_target = None
    #this code can be reused in 2nd pass
    opened_file = open(file_location)
    program_name, START, starting_address = getFirstLine(opened_file.readline()) 
    loc_counter = int(starting_address,16)             #Relocation stuff
    printable_table.append([hex(loc_counter),program_name,START,hex(loc_counter)])
    for line in opened_file.read().splitlines():    #read the label instruction target
        line_num += 1
        label, instruction, target = splitLine(line)    #label instructoin target are defined
        FirstPass_output.append([hex(loc_counter),label, instruction, target])
        printable_table.append(FirstPass_output[-1])#add
        if(label != placeholder):
            symbol_table[label] = loc_counter

        

        if(target[0] == '='): #check for literals
            target = target[1:]
            print("This is the problem")
            size = convertOutliers(target)
            loc_counter += getInstructionSize(instruction)
            literal_table[target[2:-1]] = [hex(loc_counter),size,identifyData(target)]
            tmp_literals[target[2:-1]] = [hex(loc_counter),size,identifyData(target)]
            continue
        

        #handle WORD, BYTE, RESW, RESB and LTORG
        # if(instruction in reserved)
        if(instruction == "WORD"):
            loc_counter += 3
        elif(instruction == "RESW"):
            loc_counter += int(target)*3                #we can add error handle here
        elif(instruction == "RESB"):
            loc_counter += int(target)
        elif(instruction == "BYTE"):
            size = convertOutliers(target)
            #loc_counter += convertOutliers(target)
        elif(instruction == 'LTORG'):
            # print(FirstPass_output)
            if(target == '*' or target == placeholder):
                loc_counter = generateLiterals(literal_table, tmp_literals,FirstPass_output,loc_counter)
                # loc_counter += getLiteralSize(literal_table)
                tmp_literals.clear()
                # literal_table = {}
            print(literal_table)
        elif(instruction == 'END'):
            if(tmp_literals!={}):
                # generateLiterals(literal_table,loc_counter)
                loc_counter = generateLiterals(literal_table,tmp_literals ,FirstPass_output,loc_counter)
                print(literal_table)
                tmp_literals.clear()
            print(literal_table)
            # literal_table = {}
        elif(instruction == "BASE"):
            if(target == placeholder or target == '*'):
                base_loc = loc_counter
            else:
                base_target = target
        else:
            loc_counter += getInstructionSize(instruction)
    print("final memory location: " + hex(loc_counter))
    if(base_target):
        base_loc = symbol_table.get(base_target)
        print("base and location works inside",base_target,hex(base_loc))

    opened_file.close()    
    #write to loc + file to output.txt
    print("Writing to file")
    opened_file = open("output/FirstPass_output.txt",'w')
    for i in printable_table:
        opened_file.write("{}| {} {} {}\n".format(*i))
    opened_file.close()
    #write symbols to symbolTable
    opened_file = open("output/SymbolTable.txt",'w')
    print(symbol_table)
    for i in symbol_table:
        opened_file.write("{} {}\n".format(hex(symbol_table[i]),i))
    opened_file.close()
    #write literals to literal Table
    opened_file = open("output/LiteralTable.txt",'w')
    for i in literal_table:
        opened_file.write("{} {} {}\n".format(literal_table[i][0],literal_table[i][1],literal_table[i][2]))
    # print(literal_table)
    opened_file.close()
    return base_loc,base_target,loc_counter

# print(FirstPass("Example_4.txt"))

# import SecondPass