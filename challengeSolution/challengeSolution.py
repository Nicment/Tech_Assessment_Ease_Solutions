
#Todo: find the correct way to solve this problem, write the solution, and then print the solution

class challengeSolution():
    def __init__(self,data:list, size:list):
        self.size = size
        self.data = data
        self.algorithm()
        pass
    def algorithm(self):
        # for to loop through the array
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if i == 0 and j == 0:
                    vertex = self.data[i][j]
                    north = 0                    
                    south = self.data[i+1][j]
                    east = self.data[i][j+1]
                    west = 0
                    matrixVertex = [[0,north,0],[west,vertex,east],[0,south,0]]
                    print (matrixVertex)
                if i > 0 and i < self.size[0]-1 and j > 0 and j < self.size[1]-1:
                    vertex = self.data[i][j]
                    north = self.data[i-1][j]
                    south = self.data[i+1][j]
                    east = self.data[i][j+1]
                    west = self.data[i][j-1]
                    matrixVertex = [[0,north,0],[west,vertex,east],[0,south,0]]
                    print (matrixVertex)
                if i == 0 and j > 0 and j < self.size[1]-1:
                    vertex = self.data[i][j]
                    north = 0
                    south = self.data[i+1][j]
                    east = self.data[i][j+1]
                    west = self.data[i][j-1]
                    matrixVertex = [[0,north,0],[west,vertex,east],[0,south,0]]
                    print (matrixVertex)
                    pass
                print(i, j)
                value = self.data[i][j]
                #print (value)  
        pass

class vertex():# an object is created that will contain the data of each vertex
    def __init__(self, position:list):
        pass 