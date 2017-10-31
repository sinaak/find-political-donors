
def getLine(lineNumber): 
    with open("../input/itcont.txt", "r") as fp:
        for i, line in enumerate(fp):
            if i == lineNumber-1:
                return line
            if line == '\n':
                return None



def readline(lineCounter):
    rawline =getLine(lineCounter)
    return rawline


def split(rawLine):
    splittedRawLine = rawLine.split("|")
    return splittedRawLine
