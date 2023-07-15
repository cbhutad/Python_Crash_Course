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

