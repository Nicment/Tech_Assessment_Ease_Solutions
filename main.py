from fileOpen.fileOpen import fileOpen
from challengeSolution.challengeSolution import challengeSolution

class mainChallenge():
    def __init__(self):
        readFile = fileOpen()
        size = readFile.exportSize()
        data = readFile.exportMatrix()
        challengeSolution(data,size)
        print(data)

def main():
    mainChallenge()

if __name__ == '__main__':
    main()  