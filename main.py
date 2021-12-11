from fileOpen.fileOpen import fileOpen
from challengeSolution.challengeSolution import challengeSolution
import sys

class mainChallenge():
    def __init__(self):
        path = "skirsesort.kitzbuehel/map.txt"
        if(len(sys.argv) > 1):
            path = sys.argv[1]
        readFile = fileOpen(path)
        size = readFile.exportSize()
        data = readFile.exportMatrix()
        challengeSolution(data,size)

def main():
    mainChallenge()

if __name__ == '__main__':
    main()  