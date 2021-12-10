import numpy as np
#todo: load file, data verification, pre-proces data, return data

# readFile help to read file and return list with the information
class fileOpen():
    def __init__(self, filePath:str="skirsesort.kitzbuehel/4x4.txt"):
        data = self.readFile(filePath)      
        print (data) 
        self.checkData()
        self.preProcess()
        return self.exportData()
        
    def readFile(self, filePath): 
        a_file = open(filePath)
        file_contents = a_file.read()
        contents_split = file_contents.splitlines()
        contents_split = [contents_split[i].split(" ") for i in range(len(contents_split))]
        return [list(map(int,contents_split[i])) for i in range(len(contents_split))]
    
    def checkData(self):
        pass
    
    def preProcess(self):
        pass
    
    def exportData(self):
        pass

def main():
    fileOpen()   

if __name__ == '__main__':
    main()    