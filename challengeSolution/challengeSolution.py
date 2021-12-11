
#Todo: find the correct way to solve this problem, write the solution, and then print the solution

class challengeSolution():
    def __init__(self,data:list, size:list):
        self.size = size
        self.data = data
        self.algorithm()
        pass
    def algorithm(self):
        # for to loop through the array
        matrix = [[0 for i in range(self.size[0])] for j in range(self.size[1])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                matrix[i][j] = vertex(self.data[i][j],i,j,matrix,self.size)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                matrix[i][j].findBestWay()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                print(matrix[i][j].bestWay)
                

class vertex():# an object is created that will contain the data of each vertex
    def __init__(self, value:int, i:int, j:int, matrix:list, size:list):
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
        
        northWaySteps = len(northWay)
        southWaySteps = len(southWay)
        eastWaySteps = len(eastWay)
        westWaySteps = len(westWay)
        
        if northWaySteps < 0:
            northWayHeight = northWay[0] - northWay[northWaySteps-1] + 1
        else:
            northWayHeight = 0
        if southWaySteps < 0:
            southWayHeight = southWay[0] - southWay[southWaySteps-1] + 1
        else:
            southWayHeight = 0
        if westWaySteps < 0:
            westWayHeight = southWay[0] - southWay[eastWaySteps-1] + 1
        else:
            westWayHeight = 0
        if eastWaySteps < 0:
            eastWayHeight = westWay[0] - westWay[westWaySteps-1] + 1
        else:
            eastWayHeight = 0
        
        maxSteps = max(northWaySteps,max(southWaySteps,max(eastWaySteps,westWaySteps)))
        maxHeight = max(northWayHeight,max(southWayHeight,max(eastWayHeight,westWayHeight)))
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
            
        print(north.getValue(), south.getValue(), east.getValue(),west.getValue())
        
        northWay = []
        southWay = []
        eastWay = []
        westWay = []
        
        #Revisa si hay mas posibles caminos hacia el norte
        if north.getValue() < self.getValue():
            if north.visited == False:
                northWay = [self.getValue()] + north.findBestWay()
            else:
                northWay = [self.getValue()] + north.bestWay
        #Revisa si hay mas posibles caminos hacia el sur
        elif south.getValue() < self.getValue():
            if south.visited == False:
                southWay = [self.getValue()] + south.findBestWay()
            else:
                southWay = [self.getValue()] + south.bestWay
        #Revisa si hay mas posibles caminos hacia el este   
        elif east.getValue() < self.getValue():
            if east.visited == False:
                eastWay = [self.getValue()] + east.findBestWay()
            else:
                eastWay = [self.getValue()] + east.bestWay
        #Revisa si hay mas posibles caminos hacia el oeste   
        elif west.getValue() < self.getValue():
            if west.visited == False:
                westWay = [self.getValue()] + west.findBestWay()
            else:
                westWay = [self.getValue()] + west.bestWay
        else:
            self.bestWay = [self.getValue()]
            northWay = [self.getValue()] 
            
        #Evalua los caminos resultantes y se queda con el mejor    
        self.setBestWay(self.bestWaySelected(northWay, southWay, eastWay, westWay))
        self.visited = True
        return self.bestWaySelected(northWay, southWay, eastWay, westWay)
    
    #TODO: revisar vecinos, si es menor y ya es visitado, toma el mejor camino
    #sino, encuentra el mejor camino
    #todo: 2. Evalua el mejor camino
    #todo: 3. Retorna el mejor camino  
    pass 