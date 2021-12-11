
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
    
    def findBestWay(self):
        # Upper left corner
        if self.i == 0 and self.j == 0:
            vertex = self.matrix[self.i][self.j]                  
            south = self.matrix[self.i+1][self.j]
            east = self.matrix[self.i][self.j+1]
            
            bestWay0 = []
            bestWay1 = []

            if vertex.getValue() > south.getValue():
                if south.visited == False:
                    bestWay0 = [vertex.getValue()] + south.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + south.findBestWay()         
            elif east.getValue() < vertex.getValue():
                if east.visited == False:
                    bestWay1 = [vertex.getValue()] + east.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + east.bestWay
            else:
                bestWay0 += [vertex.getValue()]
                
            vertex.setBestWay(max(bestWay0, bestWay1))
            vertex.setVisited = True
            print (max(bestWay0, bestWay1))
            return max(bestWay0, bestWay1)
                
                
        #Upper middle vertex
        if self.i == 0 and self.j > 0 and self.j < self.size[1]-1:
            vertex = self.matrix[self.i][self.j]
            south = self.matrix[self.i+1][self.j]
            east = self.matrix[self.i][self.j+1]
            west = self.matrix[self.i][self.j-1]
            
            bestWay0 = []
            bestWay1 = []
            bestWay2 = []
            
            #Revisa si hay mas posibles caminos hacia el sur
            if south.getValue() < vertex.getValue():
                if south.visited == False:
                    bestWay0 = [vertex.getValue()] + south.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + south.bestWay
            #Revisa si hay mas posibles caminos hacia el este   
            elif east.getValue() < vertex.getValue():
                if east.visited == False:
                    bestWay1 = [vertex.getValue()] + east.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + east.bestWay
            #Revisa si hay mas posibles caminos hacia el oeste 
            elif west.getValue() < vertex.getValue():
                if east.visited == False:
                    bestWay2 = [vertex.getValue()] + east.findBestWay()
                else:
                    bestWay2 = [vertex.getValue()] + east.bestWay
            else:
                bestWay0 += [vertex.getValue()]
            
            #Evalua los caminos resultantes y se queda con el mejor    
            vertex.setBestWay(max(bestWay0, max(bestWay1, bestWay2)))
            vertex.visited = True
            return max(bestWay0, max(bestWay1, bestWay2))
            
        #Upper right corner
        if self.j == self.size[1]-1 and self.i == 0:
            vertex = self.matrix[self.i][self.j]
            south = self.matrix[self.i+1][self.j]
            west = self.matrix[self.i][self.j-1]
            
            bestWay0 = []
            bestWay1 = []
            
            if south.getValue() < vertex.getValue():
                if south.visited == False:
                    bestWay0 = [vertex.getValue()] + south.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + south.bestWay                
            elif west.getValue() < vertex.getValue():
                if west.visited == False:
                    bestWay1 = [vertex.getValue()] + west.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + west.bestWay
            else:
                bestWay0 += [vertex.getValue()]
                
            vertex.setBestWay(max(bestWay0, bestWay1))
            vertex.visited = True
            return max(bestWay0, bestWay1)
            
        #Left middle vertex
        if self.j == 0 and self.i > 0 and self.i < self.size[0]-1:
            vertex = self.matrix[self.i][self.j]
            north = self.matrix[self.i-1][self.j]
            south = self.matrix[self.i+1][self.j]
            east = self.matrix[self.i][self.j+1]
            
            bestWay0 = []
            bestWay1 = []
            bestWay2 = []
            
            #Revisa si hay mas posibles caminos hacia el norte
            if north.getValue() < vertex.getValue():
                if north.visited == False:
                    bestWay0 = [vertex.getValue()] + north.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + east.bestWay        
            #Revisa si hay mas posibles caminos hacia el sur
            elif south.getValue() < vertex.getValue():
                if south.visited == False:
                    bestWay1 = [vertex.getValue()] + south.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + south.bestWay
            #Revisa si hay mas posibles caminos hacia el este   
            elif east.getValue() < vertex.getValue():
                if east.visited == False:
                    bestWay2 = [vertex.getValue()] + east.findBestWay()
                else:
                    bestWay2 = [vertex.getValue()] + east.bestWay
            else:
                bestWay0 += [vertex.getValue()]
            #Revisa si hay mas posibles caminos hacia el oeste 
           
            #Evalua los caminos resultantes y se queda con el mejor    
            vertex.bestWay = max(bestWay0, max(bestWay1, bestWay2))
            vertex.visited = True
            return max(bestWay0, max(bestWay1, bestWay2))
        
        #Middle vertex
        if self.i > 0 and self.i < self.size[0]-1 and self.j > 0 and self.j < self.size[1]-1:
            vertex = self.matrix[self.i][self.j]
            north = self.matrix[self.i-1][self.j]
            south = self.matrix[self.i+1][self.j]
            east = self.matrix[self.i][self.j+1]
            west = self.matrix[self.i][self.j-1]
            
            bestWay0 = []
            bestWay1 = []
            bestWay2 = []
            bestWay3 = []
            
            #Revisa si hay mas posibles caminos hacia el norte
            if north.getValue() < vertex.getValue():
                if north.visited == False:
                    bestWay0 = [vertex.getValue()] + north.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + north.bestWay
            #Revisa si hay mas posibles caminos hacia el sur
            elif south.getValue() < vertex.getValue():
                if south.visited == False:
                    bestWay1 = [vertex.getValue()] + south.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + south.bestWay
            #Revisa si hay mas posibles caminos hacia el este   
            elif east.getValue() < vertex.getValue():
                if east.visited == False:
                    bestWay2 = [vertex.getValue()] + east.findBestWay()
                else:
                    bestWay2 = [vertex.getValue()] + east.bestWay
            #Revisa si hay mas posibles caminos hacia el oeste   
            elif west.getValue() < vertex.getValue():
                if west.visited == False:
                    bestWay3 = [vertex.getValue()] + west.findBestWay()
                else:
                    bestWay3 = [vertex.getValue()] + west.bestWay
            else:
                bestWay0 += [vertex.getValue()]
                
            #Evalua los caminos resultantes y se queda con el mejor    
            vertex.setBestWay(max(bestWay0, max(bestWay1, max(bestWay2,bestWay3))))
            vertex.visited = True
            return max(bestWay0, max(bestWay1, max(bestWay2,bestWay3)))
            
        #Right vertex
        if self.j == self.size[1]-1 and self.i > 0 and self.i < self.size[0]-1:
            vertex = self.matrix[self.i][self.j]
            north = self.matrix[self.i-1][self.j]
            south = self.matrix[self.i+1][self.j]
            west = self.matrix[self.i][self.j-1]
            
            bestWay0 = []
            bestWay1 = []
            bestWay2 = []
            
            #Revisa si hay mas posibles caminos hacia el norte
            if north.getValue() < vertex.getValue():
                if north.visited == False:
                    bestWay0 = [vertex.getValue()] + north.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + north.bestWay
            #Revisa si hay mas posibles caminos hacia el sur
            elif south.getValue() < vertex.getValue():
                if south.visited == False:
                    bestWay1 = [vertex.getValue()] + south.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + south.bestWay 
            #Revisa si hay mas posibles caminos hacia el oeste   
            elif west.getValue() < vertex.getValue():
                if west.visited == False:
                    bestWay2 = [vertex.getValue()] + west.findBestWay()
                else:
                    bestWay2 = [vertex.getValue()] + west.bestWay
            else:
                bestWay0 += [vertex.getValue()]
            #Evalua los caminos resultantes y se queda con el mejor    
            vertex.setBestWay(max(bestWay0, max(bestWay1, bestWay2)))
            vertex.visited = True
            return max(bestWay0, max(bestWay1, bestWay2))
        
        #Lower left corner
        if self.i == self.size[1]-1 and self.j == 0:
            vertex = self.matrix[self.i][self.j]
            north = self.matrix[self.i-1][self.j]
            east = self.matrix[self.i][self.j+1]
            
            bestWay0 = []
            bestWay1 = []
            
            if north.getValue() < vertex.getValue():
                if north.visited == False:
                    bestWay0 = [vertex.getValue()] + north.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + north.bestWay
            if east.getValue() < vertex.getValue():
                if east.visited == False:
                    bestWay1 = [vertex.getValue()] + east.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + east.bestWay
            else:
                bestWay0 += [vertex.getValue()]
                
            vertex.setBestWay(max(bestWay0, bestWay1))
            vertex.visited = True
            return max(bestWay0, bestWay1)
        #Lower middle vertex
        if self.j > 0 and self.j < self.size[1]-1 and self.i == self.size[0]-1:
            vertex = self.matrix[self.i][self.j]
            north = self.matrix[self.i-1][self.j]
            east = self.matrix[self.i][self.j+1]
            west = self.matrix[self.i][self.j-1]  
            
            bestWay0 = []
            bestWay1 = []
            bestWay2 = []
            
            #Revisa si hay mas posibles caminos hacia el sur
            if north.getValue() < vertex.getValue():
                if north.visited == False:
                    bestWay0 = [vertex.getValue()] + north.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + north.bestWay
            #Revisa si hay mas posibles caminos hacia el este   
            elif east.getValue() < vertex.getValue():
                if east.visited == False:
                    bestWay1 = [vertex.getValue()] + east.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + east.bestWay
            #Revisa si hay mas posibles caminos hacia el oeste 
            elif west.getValue() < vertex.getValue():
                if east.visited == False:
                    bestWay2 = [vertex.getValue()] + east.findBestWay()
                else:
                    bestWay2 = [vertex.getValue()] + east.bestWay
            else:
                bestWay0 += [vertex.getValue()]
            
            #Evalua los caminos resultantes y se queda con el mejor    
            vertex.setBestWay(max(bestWay0, max(bestWay1, bestWay2)))
            vertex.visited = True
            return max(bestWay0, max(bestWay1, bestWay2))
        #Lower right corner
        if self.j == self.size[1]-1 and self.i == self.size[0]-1:
            vertex = self.matrix[self.i][self.j]
            north = self.matrix[self.i-1][self.j]
            west = self.matrix[self.i][self.j-1]
            
            bestWay0 = []
            bestWay1 = []
            
            if north.getValue() < vertex.getValue():
                if north.visited == False:
                    bestWay0 = [vertex.getValue()] + north.findBestWay()
                else:
                    bestWay0 = [vertex.getValue()] + north.bestWay
            elif west.getValue() < vertex.getValue():
                if west.visited == False:
                    bestWay1 = [vertex.getValue()] + west.findBestWay()
                else:
                    bestWay1 = [vertex.getValue()] + west.bestWay
            else:
                bestWay0 += [vertex.getValue()]
                
            vertex.setBestWay(max(bestWay0, bestWay1))
            vertex.visited = True
            return max(bestWay0, bestWay1)
        #TODO: revisar vecinos, si es menor y ya es visitado, toma el mejor camino
        #sino, encuentra el mejor camino
        #todo: 2. Evalua el mejor camino
        #todo: 3. Retorna el mejor camino  
        pass 