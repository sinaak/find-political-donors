
def getLine(lineNumber): 
    with open("../input/itcont.txt", "r") as fp:
        for i, line in enumerate(fp):
            if i == lineNumber-1:
                return line
            if line == '\n':
                return None



def readline(lineCounter):
    rawLine =getLine(lineCounter)
    return rawLine


def split(rawLine):
    splittedRawLine = rawLine.split("|")
    return splittedRawLine
