class SIC(object):
    byte_size = int()
    instruction_format = int()
    def __init__(self,):
        byte_size = 
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

def FormatFactory(instruction): #calls the singletonTables to find the current instruction format then returns the corresponding object
    format_type = SingletonTables.InstructionDictionary[instruction][0]
    if(format_type = 0) return SIC()