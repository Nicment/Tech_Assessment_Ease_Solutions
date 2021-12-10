
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
                print(i, j)
                value = self.data[i][j]
                print (value)  
        pass

class vertex():# an object is created that will contain the data of each vertex
    def __init__(self, position:list):
        pass

def main():
    challengeSolution()

if __name__ == '__main__':
    main()   