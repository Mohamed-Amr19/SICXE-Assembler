from LineParser import Line
from SingletonTables import Library
singletonTables = Library.getInstance()
class ProgramCounter(object):
    __instance = None
    starting_address = None
    loc_counter = 0
    line_counter = 0
    line_array = []
    current_line = None
    next_line = None
    @staticmethod
    def getInstance():
        if ProgramCounter.__instance == None:
            ProgramCounter()
        return ProgramCounter.__instance
    def __init__(self):
        if ProgramCounter.__instance != None:
            raise Exception("This class has already been initialized")
        else:
            ProgramCounter.__instance = self
    def addLine(self, line):
        self.line_array.append(line)
        self.loc_counter = line.getLocationCounter()
        self.line_counter += 0
        # print(self.loc_counter)
    def getCurrentLocation(self):
        return self.loc_counter
    def calculateAddresses(self):
        if(self.current_line.target_obj == None):
            self.nextLine()
            return
        elif(self.current_line.target_obj.target_prefix in singletonTables.unique_addressed_table):
            prefix = self.current_line.target_obj.target_prefix
            if(prefix == '*'):
                self.current_line.address = 0
            elif(prefix == '#'):
                try:
                    self.current_line.target_obj.address = int(self.current_line.target_obj.content)
                except:
                    self.current_line.target_obj.address = singletonTables.symbol_table.get(self.current_line.target_obj.content)
                    #     try:
        #         return int(self.target_obj.content)
        #     except:
        #         return self.calculateDisplacement(singletonTables.symbol_table.get(self.target_obj.content))
            self.nextLine()
            return
        elif(self.current_line.instruction_obj.format_char == '+'):
                if(singletonTables.symbol_table.get(self.current_line.target_obj.content) == None):
                    print("{} is not in the symbol table".format(self.current_line.target_obj.content))
                    exit()
                self.current_line.target_obj.address = singletonTables.symbol_table.get(self.current_line.target_obj.content)
                self.nextLine()
                return
        self.current_line.target_obj.address = self.current_line.calculateDisplacement(self.loc_counter,singletonTables.symbol_table.get(self.current_line.target_obj.content))
        #print("{} {} {}".format(self.loc_counter,self.current_line.instruction_obj.instruction_name,self.current_line.target_obj.address))
        self.nextLine()
    def getBase(self):
        if(type(singletonTables.base_address) != int):
            singletonTables.base_address = singletonTables.getSymbolLocation(singletonTables.base_address)
        print("Base address = {}".format(singletonTables.base_address))

    def printArray(self):
        for element in self.line_array:
            print("{} | {} | {}".format(
                hex(element.loc_counter),
                element.symbol_obj.symbol_name,
                element.instruction_obj.opcode,
                hex(element.target_obj.address)
                ))
            # self.array[i].append(line.instruction_obj.opcode)
            # self.array[i].append(line.flags)
            # self.array[i].append(line.target_obj.address)
            # self.array[i].append(line.object_code)
            # print(self.array[i])
    def resetStartingAddress(self):
        self.line_counter = 0
        self.next_line = self.line_array[self.line_counter+1]
        self.current_line = self.line_array[self.line_counter]
        self.loc_counter = self.starting_address
    def nextLine(self):
        #print("{} {} {}".format(self.loc_counter,self.current_line.instruction_obj.instruction_name,self.current_line.target_obj.address))
        self.line_counter +=1
        self.current_line = self.next_line
        self.next_line = self.line_array[self.line_counter]
        self.loc_counter = self.next_line.loc_counter
