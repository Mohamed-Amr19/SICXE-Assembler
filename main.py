
class SingletonTables(object):
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
    def assignToSymbolTable(self):
        print("assignToSymbolTable")
    def assignToLiteralTable(self):
        print("assignToLiteralTable")
    def getSymbol(self):
        print("getSymbol")
    def getLiteral(self):
        print("getLiteral")
    def getInstructionOpcode(self):
        print("getInstructionOpcode")

class FileWrapper(object):
    file_locations = str()
    opened_file = None
    def __init__(self, file_locations):
        self.file_locations = file_locations
        print("__init__")
    def ReadFile(self):
        print("ReadFile")
    def ParseLines():
        print("ParseLines")
    def WriteFile(self):
        print("WriteFile")
    def WriteLine(self):
        print("WriteLine")




def main():
    tmp = FileWrapper(["test_asm.txt","test_asm2.txt"])
    tmp.ReadFile()
    singleton_tables = SingletonTables()
if __name__ == "__main__":
    main()