import abc
from abc import ABC, abstractmethod



#abstraction programs in python
'''class Subbu(ABC):
    def MyProperty(self):
        print("Abstract Base Class")

class Revansh(Subbu):
    def MySelf(self):
        super().MyProperty()
        print("subclass ")

# Driver code
r = Revansh()
r.MySelf()


class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"
'''

'''class child(parent):

    @property
    def geeks(self):
        return "child class"


try:
    p = parent()
    print(p.geeks)
except Exception as err:
    print(err)

p = child()
print(p.geeks)
'''

#protected acees specifeir data members progrsm in python 
'''class Base:
    def __init__(self):
        #protected
        self._a=2
class Derived:
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of class:",self._a)
        
        #modify the protected variable:
        self._a=10
        print("calling modify the variable value:",self._a)
obj1=Derived()
obj2=Base()
print("Aceesing protected member of obj1:",obj1._a)
print("Acessing protected member of obj2:",obj2._a)
        '''
        
#private data members in python

'''class Base:
    def __init__(self):
        self.a="Revansh"
        self.__b="Pythontpoint"        
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("calling private numbers of base class:")
        print(self.__b)
        
obj=Base()
print(obj.a)
D=Derived()
print(D._b)
'''

#polymorphism in python 
'''def add(a,b,c=0):
  return a+b+c
print(add(3,4))
print(add(2,4,6))

class India():
    def capital(self):
        print("India capital is Delhi")
    def language(Self):
        print("Hindi mostly used language in India")
    def type(self):
        print("India is developing country")
class USA():
    def capital(self):
        print("Washington D.C is the capital of india:")
    def language(self):
        print("English language used mostly in USA :")
    def type(self):
        print("USA WAS DEVELOPED COUNTRY IN THE WORLD") 

obj1=India()
obj2=USA()

for country in (obj1,obj2):
    country.capital()
    country.language()
    country.type()
        '''
 #polymorphism with inheritance

''' class Bird:
     def intro(self):
       print("There are many types of birds.")
     
     def flight(self):
       print("Most of the birds can fly but some cannot.")
class sparrow(Bird):
     def flight(self):
         print("sparrow can fly.")
class ostrich(Bird):
    def flight(self):
         print("ostrich cannot fly.") 
b=Bird()
s=sparrow()
o=ostrich()                    
         
b.intro()
b.flight()
s.intro()
s.flight()
         
o.intro()
o.flight()
'''
#Strings
'''String1="GeeksForGeeks"
print("Initial String: ")
print(String1)
print("\nFirst character of string is:")
print(String1[0])
print("\nLast character of string is:")
print(String1[-1])
     #lists           
list=[]
print("Initially blank list:")
print(list)

list=["Revansh Raj"]
print("\nprint list of ")
print(list)

list=[['Rao'],["Venkat"],["sai"]]
print(list[0])
print(list[2])

print(list)


#Tuples

tuple1=()
print(tuple1)
tuple1=("rama","rao")
print(tuple1)
list1=tuple[1,2,3,4,5,6]
print(tuple(list1))
tuple1=tuple('Geeks')
print(tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)
print(tuple1[0])
print(tuple1[2])
'''
#set
'''set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)
        
        
        
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

'''
'''
l=["nandyala","revansh","rajini"]
for i in l:
    print(i)
#tuple iteration
print("\nTuple iteration")
t=("Nandyala","Subbaramaiah","Hello")
for i in t:
    print(i)
    string="Hey"
#dictionary
print("\nDictionary Iteration")   
d=dict()
d['xyz']=123
d['abc']=585
for i in d:
    print(i,d[i])

class Subject:

	def __init__(self, attr1, attr2):
		self.attr1 = attr1
		self.attr2 = attr2


obj = Subject('Maths', 'Science')
print(obj.attr1) 
print(obj.attr2)

class car():
    
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def show(self):
        print("Model is", self.model)
        print("color is", self.color)
        
audi=car("audi","blue")
ferrari=car("ferrari","green")
audi.show()
ferrari.show()
print(audi.model)
print(ferrari.model)
'''

#Array

'''import array as arry
a=arry.array('i',[1,2,3])

for i in range(0,3):
    print(a[i],end=" ")   
 
myname='subbu'
len(myname)

gfg="subbu"
gfg="".join(reversed(gfg)) 
print(gfg)
gfg="revansh"
print(gfg)
del gfg[1]
print(gfg)

String1 = "Hello, I'm a Geek"
print(String1)

print("Deleting character at 2nd Index: ")
del String1
print(String1)     

#positional formating
string="{f} {g} {l}" .format(l='leeks', f='for', g='Geeks')
print(string)
#positional formating
str="{0:b}".format(16)
print(str)
#formating of floats
str="{0:e}".format(165.7373)
print(str)
String1 = "{0:.2f}".format(1/6)
print(String1)
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks',
                                          'for', 
                                          'Geeks')
print(String1)


mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)


def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)
'''
