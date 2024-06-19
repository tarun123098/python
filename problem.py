class shape:
    def __init__(self,shapeType):
        self.shapeType=shapeType
    def printmytype(self):
        print(f"i am a {self.shapeType}")
class square(shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    def calculatearea(self):
        return self.length**2
    def printmytype(self):
         print(f"I am a {self.shapeType}")
class rectangle(shape):
    def __init__(self,length,breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth= breadth
    def calculatearea(self):
        return self.length*self.breadth
    def printmytype(self):
        print(f"iam a {self.shapeType}")
def main():
    square = square(5)
    square.printmytype()
    print(f"Area: {square.calculatearea()}")

    rectangle = Rectangle(5, 4)
    rectangle.printmytype()
    print(f"Area: {rectangle.calculatearea()}")

if __name__ == "__main__":
    main() 


