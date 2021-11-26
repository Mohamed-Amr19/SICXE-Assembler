class SingletonTables(object):#fuck microsoft, shit company. i hope they all die.
    __instance = None
    symbol_table = {}
    literal_table = {}
    instruction_table = {}
    @staticmethod
    def getInstance():
        if SingletonTables.__instance == None:
            SingletonTables()
        return SingletonTables.__instance
    def __init__(self):
        if SingletonTables.__instance != None:
            raise Exception("This class has already been initialized")
        else:
            SingletonTables.__instance = self
    def assignToSymbolTable(self,symbol_name, location):
        self.symbol_table[symbol_name] = location
        #print("assignToSymbolTable")
    def assignToLiteralTable(self,literal_name, location):
        self.literal_table[literal_name] = location
        #print("assignToLiteralTable")
    def getSymbolLocation(self,symbol_name):
        return self.symbol_table[symbol_name]
        #print("getSymbolLocation")
    def getLiteralLocation(self,literal_name):
        return self.literal_table[literal_name]
        #print("getLiteral")
    def getInstructionOpcode(self):
        print("getInstructionOpcode")