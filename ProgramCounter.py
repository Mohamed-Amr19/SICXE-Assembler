from LineParser import Line
class ProgramCounter(object):
    __instance = None
    starting_address = None
    loc_counter = 0
    line_array = []
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
        # print(self.loc_counter)
