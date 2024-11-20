class hello:
 name='pankaj'

obj=hello()
print(obj.name)

#if we use __ then it make the private 

class hello:
  __name='pankaj'
  def show(self):
    print(self.__name)

obj=hello()
print(obj.show())