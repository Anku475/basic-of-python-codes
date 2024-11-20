from abc import *
class polygon():
    @abstractmethod
    def calaculatearea(self,a,b):
        pass
class traingle(polygon):
    def calculatearea(self,b,h):
        return 0.5*b*h

obj=traingle()
area=obj.calculatearea(5,4)
print(area)