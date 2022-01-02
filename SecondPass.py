from FirstPassUtility import *
from FirstPass import *
import re
import sys 
if(len(sys.argv) == 1):
    star = """Available Example files: 
    1)Example_1.txt 
    2)Example_2.txt
    3)Example_3.txt
    4)Example_4.txt
    5)Example_Book_P94.txt
    6)Example_extref.txt
    7)Example_SpecialFormats.txt
    \nEntire File number: """
    examples = {
        '1':"Example_1.txt",
        '2':"Example_2.txt",
        '3':"Example_3.txt",
        '4':"Example_4.txt",
        '5':"Example_Book_P94.txt",
        '6':"Example_extref.txt",
        '7':"Example_SpecialFormats.txt"
        }
    inp = examples.get(input(star),0)
    if(inp):
        base_loc,base_target,final_address = FirstPass(inp)
    else:
        print("Wrong input, exiting")
        exit()
else:
    args = sys.argv[1:]
    base_loc,base_target,final_address = FirstPass(args[0])
# base_loc,base_target,final_address = FirstPass(arg)
SecondPass_printable_table = []
external_definitions = []
objectcode = []
modification_table = []
def pad(star,size,char):
    if(size > 0):
        return((size - len(star))*char + star)
    else:
        size = abs(size)
        return(star + (size - len(star))*char)


def directive():
    return(['0','0','0','0','0'],0)

def splitTarget(star):
    return re.split('(\+|-)',star)

def SecondPass():
    mod_flag = False
    def format1():
        print("format 1")
    def format2(target):
        if(',' in target):
            r1,r2 = target.split(',')
            r1 = registers.get(r1)
            r2 = registers.get(r2)
            if(r1 == None or r2 == None):
                print("Missing Register input")
                exit()
            return([r1,r2])
        if(target not in registers):
            print("Register not found, exitting")
            exit()
        return([registers.get(target),'0'])
    def format3(loc_counter,target):
        flags,target_address = getFlags(loc_counter,3,target)
        flags = "".join(flags)
        return([flags, target_address])
    def format4(loc_counter,target):
        flags,target_address = getFlags(loc_counter,4,target)
        flags = "".join(flags)
        return([flags, target_address])
    def format5(loc_counter,target):
        flags,target_address = getFlags(loc_counter,3,target)
        flags[0] = '0' if target_address %3 == 0 else '1'
        flags[1] = '0' if target_address > 0 else '1'
        flags[2] = '1' if target_address == 0 else '0'
        flags = "".join(flags)
        return([flags, target_address])
    def format6(loc_counter,target):
        flags,target_address = getFlags(loc_counter,4,target)
        flag[3] = '0' if target_address % 3 == 0 else '1'
        flag[4] = '0' if target_address == 0 else '1'
        flag[5] = '0' if target_address == base_loc else '1'
        flags = "".join(flags)
        return([flags, target_address])
    def getSymbol(symbol_name):
        symbol = symbol_table.get(symbol_name,0)
        if(symbol_name in external_references):
            size = 5 if instruction[0] in ['+','$'] else 3
            modification_table.append([loc_counter,symbol_name,size])
            return 0
        return symbol
    def getFlags(loc_counter,format,target):     #Immediate “#” i=1, n=0 Value = TA
                                #Indirect “@” i=0, n=1 Value = ((TA))
        n,i,x,b,p,e = '1','1','0','0','0','0'   #simple in sicxe i=1 , n=1 Value = (TA)
        flag=0
        if(target == placeholder):
            return([n,i,x,b,p,e],0)
        if('#' in target):
            n,i = '0','1'
            target = target[1:]
            flag=1
            try:
                target_address = int(target)
                return([n,i,x,b,p,e],(target_address))
            except:
                target_address = getSymbol(target)
                return([n,i,x,b,p,e],(target_address))

        elif('@' in target):
            n,i = '1','0'
            
            #removing the # from target
            target = target[1:]
            flag=1
            
            try:
                target_address = int(target)
                return([n,i,x,b,p,e],(target_address))
            except:
                target_address = getSymbol(target)
                return([n,i,x,b,p,e],(target_address))
        elif('=' in target):
            target_address = int(literal_table.get(target[3:-1])[0],16)

        else:
            target_address = getSymbol(target)
        if(',X' in target):
            x = '1'
            target = target[0:-2]
            target_address = getSymbol(target)
            return([n,i,x,b,p,e],(target_address))
        if(format in [4,6] ):
            if(flag==1):
                target_address=int(target)
            b,p,e = '0','0','1'
            return([n,i,x,b,p,e],(target_address))
        disp = target_address - (int(loc_counter,16) + format)
        if(disp >= -2048 and disp < 0):
            #b = 0 , p = 1
            b,p = '0','1'
            disp &= int('FFF',16)
        elif(disp <= 2047 and disp > 0):
            #b = 0 , p = 1
            b,p = '0','1'
            # return disp
        elif(target_address <= 4096 + base_loc and target_address >= base_loc ):
            #b = 1 , p = 0
            b,p = '1','0'
            disp = target_address - base_loc
        else:
            print("Base Address hasn't been specified and the jump is too large for PC-relative addressing, Please use format 4 at {}".format(loc_counter))
            exit()
        
        return([n,i,x,b,p,e],(disp))

    for line in FirstPass_output:
        
        loc_counter, label, instruction, target = line
        mod_flag = False

        if(instruction in reserved):
            if(instruction == "WORD"):
                objectcode.append([loc_counter,pad(identifyData(target),6,'0')])
            elif(instruction == "BYTE"):
                objectcode.append([loc_counter,pad(identifyData(target),2,'0')])
            elif(instruction == "RESW" or instruction == "RESB"):
                objectcode.append([loc_counter,skipper])
            elif(instruction == "EXTREF"):
                continue
            elif(instruction == "EQU"):
                continue
            elif(instruction == "EXTDEF"):
                for i in target.split(','):
                    external_definitions.append([getSymbol(i),i])
                continue

            else:
                objectcode.append([loc_counter,placeholder])
            ocode = objectcode[-1][1]
            printered = loc_counter+' | '+label +' '+instruction+' '+target+' | '+ocode
            SecondPass_printable_table.append(printered)
            continue

        elif(instruction[0] =='+'):
            form,opcode = instruction_table.get(instruction[1:])
            form+=1
            opcode = opcode >> 2
            objectcode.append([opcode,*format4(loc_counter,target)])
            mod_flag = True

        elif(instruction[0] =='&'):
            form,opcode = instruction_table.get(instruction[1:])
            form+=1
            opcode = opcode >> 2
            objectcode.append([opcode,*format5(loc_counter,target)])

        elif(instruction[0] =='$'):
            form,opcode = instruction_table.get(instruction[1:])
            form+=1
            opcode = opcode >> 2
            objectcode.append([opcode,*format6(loc_counter,target)])
        elif(instruction == placeholder):
            printered = loc_counter+' | '+label +' '+instruction+' '+target+' | '+target
            SecondPass_printable_table.append(printered)
            objectcode.append([loc_counter,target])
            continue
        else:
            form,opcode = instruction_table.get(instruction)
            if(form == 1):
                printered = loc_counter+' | '+label +' '+instruction+' '+target+' | '+ opcode
                SecondPass_printable_table.append(printered)
                objectcode.append([loc_counter,opcode])
                continue
            elif(form == 2):
                ocode = hex(opcode)[2:]+"".join(format2(target))
                printered = loc_counter+' | '+label +' '+instruction+' '+target+' | '+ocode
                SecondPass_printable_table.append(printered)
                objectcode.append([loc_counter,ocode])
                continue
            elif(form == 3):
                opcode = opcode >> 2
                objectcode.append([opcode,*format3(loc_counter,target)])
        
        objectcode[-1][2] = hex(objectcode[-1][2])[2:]
        size = 3 if form == 3 else 5
        if(len(objectcode[-1][2]) < size):
            objectcode[-1][2] = pad(objectcode[-1][2],size,'0')#(size - len(objectcode[-1][2]))*'0' + objectcode[-1][2]
        ocode = bin(objectcode[-1][0])[2:] + objectcode[-1][1] #+ objectcode[-1][2]
        if(mod_flag):
            modification_table.append([loc_counter,instruction,size])
        #ensure that the opcode and flags are 3 bytes
        ocode = pad(hex(int(ocode,2))[2:],3,'0')
        ocode += objectcode[-1][2]
        
        ocode = pad(ocode,6,'0')
        objectcode[-1][0] = hex(objectcode[-1][0])
        objectcode[-1] = [loc_counter,ocode]
        printered = loc_counter+' | '+label +' '+instruction+' '+target+' | '+ocode
        SecondPass_printable_table.append(printered)
    

SecondPass()
opened_file = open("output/SecondPass_Output.txt",'w')
for i in SecondPass_printable_table:
    opened_file.write(i+'\n')
opened_file.close()

def GenerateHRecord():
    program_name, starting_address = first_line
    program_name = pad(program_name,-6,padding)#(program_name + (6 - len(program_name))*padding)

    starting_address = int(starting_address,16)
    program_size = hex(final_address - starting_address)[2:]
    program_size = pad(program_size,6,'0')#((6 - len(program_size))*'0' + program_size)

    starting_address = hex(starting_address)[2:]
    starting_address = pad(starting_address,6,'0')#((6 - len(starting_address))*'0'+ starting_address)
    star = "H." + program_name + seperator + starting_address + seperator + program_size + '\n'
    return(star)
def GenerateTRecords():
    records = []
    max_size = 10
    size=0
    opcode_record = ''
    starting_address = objectcode[0][0][2:]
    def addRecord(address,size,opcode):
        address = pad(address,6,'0')
        size = pad(hex(int(size/2))[2:],2,'0')
        record = 'T.'+address + '.' +size + opcode
        records.append(record)
    for loc_counter,opcode in objectcode:
        if(size == 0):
            starting_address= loc_counter[2:]
        if(opcode == placeholder):
            continue
        if(opcode == skipper):
            if(size == 0):
                continue
            addRecord(starting_address, size, opcode_record)

            size = 0
            opcode_record = ''
            continue

        if(size + len(opcode) > 60):
            addRecord(starting_address, size, opcode_record)
            starting_address = loc_counter[2:]
            size = len(opcode)
            opcode_record = '.' + opcode
            continue
        size += len(opcode)
        opcode_record += '.'+opcode
    addRecord(starting_address, size, opcode_record)
    return records
def GenerateERecord():
    return( 'E.' + pad(objectcode[0][0][2:],6,'0'))
def GenerateRRecord():
    records = 'R'
    for rec in external_references:
        records += '.' +pad(rec,-6,padding)
    return(records)
def GenerateMRecord():
    records = []
    if(objectcode[0][0][2:] != '0'):
        print("No address relocation will occur")
        return
    
    for loc,inst,offset in modification_table:
        # print(modification_table)
        loc = pad(loc[2:],6,'0') + '.'
        offset = pad(hex(offset)[2:],2,'0')#+'.' #disabled till sectioning is done
        record = "M."+loc+offset
        if(inst in external_references):
            record += '.+'+inst
        records.append(record)
    return records
def GenerateDRecord():
    records = 'D'
    for loc,symbol in external_definitions:
        loc = pad(hex(loc)[2:],6,'0')
        symbol = '.' + pad(symbol,-6,padding)
        records += '.' + loc + symbol
    return(records)
def GenerateHDRTME():
    opened_file = open("output/hdrtme_record.txt",'w')
    Hrecord = GenerateHRecord()
    Drecord = GenerateDRecord()
    Rrecord = GenerateRRecord()
    opened_file.write(Hrecord)
    if(Drecord != 'D'):
        # print(Drecord)
        opened_file.write(Drecord+'\n')
    if(Rrecord != 'R'):
        # print(Rrecord)
        opened_file.write(Rrecord+'\n')
    Trecs = GenerateTRecords()
    Mrecs = GenerateMRecord()
    
    # print(Mrecs)
    for rec in Trecs:
        opened_file.write(rec+'\n')
    if(Mrecs):    
        for rec in Mrecs:
            opened_file.write(rec+'\n')
    opened_file.write(GenerateERecord())
    opened_file.close()
GenerateHDRTME()
