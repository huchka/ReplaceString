
import glob


"""
try:
    input = open('data.txt', 'r')
    lines = input.readlines()
    input.close()
except IOError:
    print "The file doesnt exist"

testing branch. on this change changed from master branch

"""

oldString = 'Huchka'
newString = 'Tulgaa'

def getFileNames():
    fileNames = glob.glob('*.txt')
    return fileNames

def replace(line, old, new):
    return line

fileNames = getFileNames()

for fileName in fileNames:
    inputFile = open(fileName, 'r')
    lines = inputFile.readlines()
    inputFile.close()

    outputFile = open(fileName, 'w')
    for line in lines:
        line = replace(line, oldString, newString)
        outputFile.write(line)
    outputFile.close()
    


