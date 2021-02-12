          
from abc import ABC, abstractmethod 
class Person(ABC):
    @abstractmethod    
    def get_gender(self): 
        pass
  
class Male(Person):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
    def get_gender(self): 
        print(self.name,"is",self.gender)
  
class Female(Person): 
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
    def get_gender(self): 
        print(self.name,"is",self.gender)
#P = Person() 
#P.get_gender()
#TypeError: Can't instantiate abstract class Person with abstract method get_gender
R = Male("Arun","Male") 
R.get_gender() 
  
K = Female("Padma","Female") 
K.get_gender()
