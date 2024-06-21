class Dog:
    #class level variables
      Animal="dog"
      def __init__(self,breed,color):
          #local variables
          self.breed=breed
          self.color=color
          #object
rod=Dog("pulfy","red")
print(rod.Animal)
print(rod.breed)
print(rod.color) 
print(Dog.Animal)         