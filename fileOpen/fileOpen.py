
#todo: load file, data verification, pre-proces data, return data
# readFile help to read file and return list with the information
class fileOpen():
    def __init__(self, filePath:str="skirsesort.kitzbuehel/map.txt"):
        self.readFile(filePath)      
        self.preProcess(self.data)
        self.checkData()
        
    def readFile(self, filePath): 
        
        a_file = open(filePath) #open file 
        file_contents = a_file.read() #return list of strings
        contents_split = file_contents.splitlines() #Split list of lines
        contents_split = [contents_split[i].split(" ") for i in range(len(contents_split))] # go line by line and split the data for the " " in line
        self.data = [list(map(int,contents_split[i])) for i in range(len(contents_split))] # transform the list whit str in a list with int
    
    def checkData(self):
        pass
    
    def preProcess(self, data):
        self.size = data[0] #Take the first position whit the matrix dimensions
        self.data = data[1:] # Take the matrix whit the data 
        #print(self.matrixData[0][3])
        pass
    
    def exportMatrix(self):
        return self.data
    def exportSize(self):
        return self.size

def main():
    fileOpen()   

if __name__ == '__main__':
    main()    