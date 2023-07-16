# Notes

### Class

In python one can define classes in order to implement object oriented programming. The instances made of classes are called as objects.

Syntax for a class is as follows:

``` Python

class ClassName:

    def __init__(self,para1,para2):
        self.para1 = para1
        self.para2 = para2

    def method1(self,*parameters):
        #method body

classObject = ClassName(para1,para2)

```

Here the points to note are as follows:
- Each class definition starts with `class` keyword.
- The classname is generally starting with capital letters.
- we don't require a `new` keyword in order to create an object of class as shown on line 20.
- Here the `__init__()` function is called automatically when a new instance is created for the class. This is used to initialize the attributes for the class. The syntax is 2 underscores followed by init followed again by 2 underscores.
- `self` is the parameter which represents the instance of the class. The reference of the instance of class is automatically passed when a method is being called on the instance. So in order to do so the self must be the first parameter for the `__init__()` or any other methods. So even if a method does not have a parameter it will have a self parameter in its definition (This is required else we error `TypeError: Restaurant.describe_restaurant() takes 0 positional arguments but 1 was given`).
- The default value returned by a python method is `None`.

> check the dog.py in examples for a simple class in python.

### Inheritance

Inheritance in allows us to inherit the attributes and methods of superclass/parentclass in a subclass/childclass. By doing this we can generalize a base class and create class which uniquely define the attributes and methods for a specific scenario. Example would be cat class as base and Lion as subclass.

``` Python

class Baseclass:

    def __init__(self,para1,para2):
        self.para1 = para1
        self.para2 = para2

    def method1(self):
        #function body

class Childclass(Baseclass):

    def __init__(self,para1,para2,para3):
        super().__init__(para1,para2)
        self.para3 = para3

```

Rules to remember while implementing inheritance is as follows:
1) In order to indicate inheritance the syntax is `class ChildClassName(BaseClassName)`.
2) We should first call the `__init__` method of parent class in the `__init__` method of child class in order to initialize the parent class attributes if any (Making this compulsory in order to avoid errors later).
3) In order to access the methods of parent class in child class we can use the `super()` function. The attributes are available directly.
4) All the parent class methods are directly available in child class via inheritance. In order to modify the behaviour of such methods in child class we can do it by defining the same method again in the child class with the requried behaviour.
5) In case the class has instance of another class as attribute then the class must be defined before the class in which it will be added as attribute.

> check the electric_car.py example for instance as attribute example

Python allows us to organize classes using modules. This is similar to how we use functions and import them via modules. The syntax for this is same as well. Just go through the below list of examples for various ways of importings.

> Examples/Modules/my_car.py for a simple import of module car.py containing car class.
> Examples/Modules/my_electric_car.py for multiple class defined in module car.py and importing a single class from the same.
> Examples/Modules/my_cars.py for multpile classes import or importing all classes from a module car.py.

The particular `from modulename import *` syntax should be avoided as first we don't know which classes are being used which can be done by specifying multiple class import syntax and also this can issues such as same identifier already being used in current file causing ambiguity.

> Examples/Modules/electric_car.py for importing a module in another module.