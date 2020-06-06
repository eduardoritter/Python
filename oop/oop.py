class Base:

    def __init__(self):
        print("Base constructor")

    # Declaring public method
    def do(self):
        print("Public method") 
  
    # Declaring private method 
    def __do(self): 
        print("Private method")

    @classmethod
    def class_do(cls):
        print("Executing class_do(%s)" % cls)

    @staticmethod
    def static_do():
        print("Executing static_do()")


# Creating a derived class  
class Derived(Base):  
    def __init__(self):
        print("Derived constructor")
          
        # Calling constructor of  
        # Base class  
        Base.__init__(self)  
          
    def call_public(self): 
          
        # Calling public method of base class 
        print("\nInside derived class") 
        self.do() 
          
    def call_private(self): 
          
        # Calling private method of base class 
        self.__do() 

Base.static_do()
Base.class_do()

# Uncommenting Base.do() will
# raise a TypeError:

b = Base()
b.static_do()
b.class_do()
b.do()

# Uncommenting b.__do() will  
# raise an AttributeError

d = Derived()
d.call_public()

# Uncommenting d.call_private()  
# will also raise an AttributeError

