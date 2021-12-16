class Library(object):#fuck microsoft, shit company. i hope they all die.
    __instance = None
    starting_address = 0
    base_address = None
    symbol_table = {}
    literal_queue = []
    literal_pool_size = int()
    instruction_table = {} #unsure of this data struct
    directive_table = {"RESW":3,"RESB":0,"WORD":3,"BYTE":0,"BUFFER":0,"LTORG":0}
    unique_instruction_table = {'+':1, '&':0,'$':1}
    unique_addressed_table = {'=':1,'@':1,'#':1}
    @staticmethod
    def getInstance():
        if Library.__instance == None:
            Library()
        return Library.__instance
    def __init__(self):
        if Library.__instance != None:
            raise Exception("This class has already been initialized")
        else:
            Library.__instance = self
    def assignToSymbolTable(self,symbol_name, location):
        #print(self.symbol_table)
        if(self.symbol_table.get(symbol_name,-1) != -1):
            raise Exception("'{}'Symbol already exists in table".format(symbol_name))    
        self.symbol_table[symbol_name] = location    
        
        
        #print("assignToSymbolTable")
    def enqueueLiteral(self,literal_name, location,size):
        self.literal_queue.append([literal_name,location])
        self.literal_pool_size+= size
    def getLiteralSize(self):
        tmp = self.literal_pool_size
        self.literal_pool_size = 0
        return tmp
        #print("assignToLiteralTable")
    def getSymbolLocation(self,symbol_name):
        return self.symbol_table[symbol_name]
        #print("getSymbolLocation")
    def dequeueLiteral(self):
        return self.literal_queue.pop()
        #print("getLiteral")
    def getInstructionOpcode(self):
        print("getInstructionOpcode")
    def printSymbolTable(self):
        for key in self.symbol_table:
            print(key, ':' ,hex(self.symbol_table[key]))

