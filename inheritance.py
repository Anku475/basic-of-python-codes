class parent():
    _adhar=1234567
    __pan=1234678
    def add(self,a,b):
     self.a=a
     self.b=b
     print(self.a+self.b)
class child(parent):
   def sub(self,a,b):
      self.a=a
      self.b=b
      print(self.a-self.b)
obj=child()
obj.sub(6,4)
obj.add(6,4)
print(obj._adhar) #protected
print(obj._parent__pan) #private

# child(parent):  it inherit the property of parent

#multilevel

class grandparent():

    def mul(self,a,b):
     self.a=a
     self.b=b
     print(self.a*self.b)
class parent(grandparent):
   def sub(self,a,b):
      self.a=a
      self.b=b
      print(self.a-self.b)
class child(parent):
   def add(self,a,b):
      self.a=a
      self.b=b
      print(self.a+self.b)     
obj=child()
obj.sub(6,4)
obj.add(6,4)
obj.mul(6,4)

#multiple
class grandparent():

    def mul(self,a,b):
     self.a=a
     self.b=b
     print(self.a*self.b)
class parent():
   def sub(self,a,b):
      self.a=a
      self.b=b
      print(self.a-self.b)
class child( grandparent,parent):
   def add(self,a,b):
      self.a=a
      self.b=b
      print(self.a+self.b)     
obj=child()
obj.sub(6,4)
obj.add(6,4)
obj.mul(6,4)
