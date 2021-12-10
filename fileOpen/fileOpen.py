#todo: load file, data verification, pre-proces data, return data

class fileOpen():
    def __init__(self, filePath:str="skirsesort.kitzbuehel/4x4.txt"):
        self.filePath = filePath
        self.readFile()
        self.checkData()
        self.preProcess()
        return self.exportData()
        
    def readFile(self):
        pass
    def checkData(self):
        pass
    def preProcess(self):
        pass
    def exportData(self):
        pass
    
        