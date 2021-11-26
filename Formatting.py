
class SIC(object):
    byte_size = int()
    instruction_format = int()
    def __init__(self):
        print("__init__")

class SICXE(SIC):
    prefix_char = str()
    flags = int() #unsure if it's supposed to be here
    def __init__(self, prefix_char):
        print("__init__")

class SpecialSICXE(SICXE):
    #we have no clue what we're going to do here
    def __init__(self):
        print("__init__")

class FormatFactory(object): #calls the singletonTables to find the current instruction format then returns the corresponding object
    def getFormat(self,instruction):
        print("getFormat")
    