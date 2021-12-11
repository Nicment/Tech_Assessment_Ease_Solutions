
#Todo: find the correct way to solve this problem, write the solution, and then print the solution

class challengeSolution():
    def __init__(self,data:list, size:list):
        self.size = size
        self.data = data
        self.globalBestWay = vertex()
        self.algorithm()
        
        
    def algorithm(self):
        # for to loop through the array
        matrix = [[0 for i in range(self.size[0])] for j in range(self.size[1])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                matrix[i][j] = vertex(self.data[i][j],i,j,matrix,self.size)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                matrix[i][j].findBestWay()
                self.findBestWay(matrix[i][j],
                                 matrix[i][j].lengthOfCalculatedPath,
                                 matrix[i][j].dropOfCalculatedPath)
        print("Length of calculated path: ",self.globalBestWay.lengthOfCalculatedPath)
        print("Drop of calculated path:   ",self.globalBestWay.dropOfCalculatedPath)
        print("Calculated path:           ",self.globalBestWay.bestWay)
                
        
    def findBestWay(self,vertex, lengthOfCalculatedPath, dropOfCalculatedPath):
        
        maxSteps = max(self.globalBestWay.lengthOfCalculatedPath, lengthOfCalculatedPath)
        maxHeight = max(self.globalBestWay.dropOfCalculatedPath, dropOfCalculatedPath)
        
        if self.globalBestWay.lengthOfCalculatedPath == maxSteps and self.globalBestWay.dropOfCalculatedPath == maxHeight:
            pass
        elif lengthOfCalculatedPath == maxSteps and dropOfCalculatedPath == maxHeight:
            self.globalBestWay = vertex

class vertex():# an object is created that will contain the data of each vertex
    def __init__(self, value:int = 0, i:int = 0 , j:int = 0, matrix:list =[], size:list=[]):
        self.value = value
        self.matrix = matrix
        self.size = size
        self.i = i
        self.j = j
        self.bestWay = []
        self.lengthOfCalculatedPath = 0
        self.dropOfCalculatedPath = 0
        self.visited = False
        
    def setValue(self):
        pass
    def getValue(self):
        return self.value
    
    def setBestWay(self, bestWay):
        self.bestWay += bestWay
    
    def bestWaySelected(self, northWay:list=[],southWay:list =[],eastWay:list =[],westWay:list=[]):
        bestWay = []
        northWaySteps = len(northWay)
        southWaySteps = len(southWay)
        eastWaySteps = len(eastWay)
        westWaySteps = len(westWay)
        
        if northWaySteps > 0:
            northWayHeight = northWay[0] - northWay[northWaySteps-1] + 1
        else:
            northWayHeight = 0
        if southWaySteps > 0:
            southWayHeight = southWay[0] - southWay[southWaySteps-1] + 1
        else:
            southWayHeight = 0
        if westWaySteps > 0:
            westWayHeight = westWay[0] - westWay[westWaySteps-1] + 1
        else:
            westWayHeight = 0
        if eastWaySteps > 0:
            eastWayHeight = eastWay[0] - eastWay[eastWaySteps-1] + 1
        else:
            eastWayHeight = 0
        
        maxSteps = max(northWaySteps,max(southWaySteps,max(eastWaySteps,westWaySteps)))
        maxHeight = max(northWayHeight,max(southWayHeight,max(eastWayHeight,westWayHeight)))
        
        self.lengthOfCalculatedPath = maxSteps
        self.dropOfCalculatedPath = maxHeight
        
        if northWaySteps == maxSteps and northWayHeight == maxHeight:
            bestWay =  northWay
        elif southWaySteps == maxSteps and southWayHeight == maxHeight:
            bestWay = southWay
        elif eastWaySteps == maxSteps and eastWayHeight == maxHeight:
            bestWay = eastWay
        elif westWaySteps == maxSteps and westWayHeight == maxHeight:
            bestWay = westWay  
        
        return bestWay
        
    
    def findBestWay(self):
        if self.visited:
            return self.bestWay
        # Upper left corner
        if self.i == 0 and self.j == 0:                
            south = self.matrix[self.i+1][self.j]
            east = self.matrix[self.i][self.j+1]
            north = self
            west = self
        elif self.i == 0 and self.j > 0 and self.j < self.size[1]-1:
            north = self
            south = self.matrix[self.i+1][self.j]
            east = self.matrix[self.i][self.j+1]
            west = self.matrix[self.i][self.j-1]
        elif self.j == self.size[1]-1 and self.i == 0:
            south = self.matrix[self.i+1][self.j]
            west = self.matrix[self.i][self.j-1]
            north = self
            east = self
        elif self.j == 0 and self.i > 0 and self.i < self.size[0]-1:
            north = self.matrix[self.i-1][self.j]
            south = self.matrix[self.i+1][self.j]
            east = self.matrix[self.i][self.j+1]
            west = self
        elif self.i > 0 and self.i < self.size[0]-1 and self.j > 0 and self.j < self.size[1]-1:
            north = self.matrix[self.i-1][self.j]
            south = self.matrix[self.i+1][self.j]
            east = self.matrix[self.i][self.j+1]
            west = self.matrix[self.i][self.j-1]
        #Right vertex
        elif self.j == self.size[1]-1 and self.i > 0 and self.i < self.size[0]-1:
            north = self.matrix[self.i-1][self.j]
            south = self.matrix[self.i+1][self.j]
            west = self.matrix[self.i][self.j-1]
            east = self
        elif self.i == self.size[1]-1 and self.j == 0:
            north = self.matrix[self.i-1][self.j]
            east = self.matrix[self.i][self.j+1]
            west = self
            south = self
        elif self.j > 0 and self.j < self.size[1]-1 and self.i == self.size[0]-1:
            north = self.matrix[self.i-1][self.j]
            east = self.matrix[self.i][self.j+1]
            west = self.matrix[self.i][self.j-1]  
            south = self
        elif self.j == self.size[1]-1 and self.i == self.size[0]-1:
            north = self.matrix[self.i-1][self.j]
            west = self.matrix[self.i][self.j-1]
            east = self
            south = self

        northWay = []
        southWay = []
        eastWay = []
        westWay = []
        
        northFlag = False
        southFlag = False
        eastFlag = False
        westFlag = False
        
        #Revisa si hay mas posibles caminos hacia el norte
        if north.getValue() < self.getValue():
            northFlag = True
            if north.visited == False:
                northWay = [self.value] + north.findBestWay()
            else:
                northWay = [self.value] + north.bestWay
        #Revisa si hay mas posibles caminos hacia el sur
        if south.getValue() < self.getValue():
            southFlag = True
            if south.visited == False:
                southWay = [self.value] + south.findBestWay()
            else:
                southWay = [self.value] + south.bestWay
        #Revisa si hay mas posibles caminos hacia el este   
        if east.getValue() < self.getValue():
            eastFlag = True
            if east.visited == False:
                eastWay = [self.value] + east.findBestWay()
            else:
                eastWay = [self.value] + east.bestWay
        #Revisa si hay mas posibles caminos hacia el oeste   
        if west.getValue() < self.getValue():
            westFlag = True
            if west.visited == False:
                westWay = [self.value] + west.findBestWay()
            else:
                westWay = [self.value] + west.bestWay
                
        if northFlag == False and southFlag == False and westFlag == False and eastFlag == False:
            self.bestWay = [self.value]
            self.visited = True
            return self.bestWay
        else:
            self.setBestWay(self.bestWaySelected(northWay, southWay, eastWay, westWay))
            self.visited = True
        #print(northWay,southWay,eastWay,westWay)
        #Evalua los caminos resultantes y se queda con el mejor    
        return self.bestWay
    
    #TODO: revisar vecinos, si es menor y ya es visitado, toma el mejor camino
    #sino, encuentra el mejor camino
    #todo: 2. Evalua el mejor camino
    #todo: 3. Retorna el mejor camino  
    pass 