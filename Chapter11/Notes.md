# Notes

- A unit test checks whether a specific aspect of the function's behavior is correct.
- A test case is collection of unit test cases which checks whether the function behaves within the range of situations.

### Testing using unittest

- unittest is inbuilt module provided with Python installation. 
- We can import this module in the module where testing code is written.

#### Setup

1) We first import the module in the file where the testing code will be written.
2) Then we create a class which inherits from `unittest.TestCase` class.

``` Python

class TestClass(unittest.TestCase):
    #code

```

3) Each function inside this class must begin with `test_` prefix. This will functions then will be called directly when the python file is executed. No need to create a object of the class or anything.

``` Python

class TestClass(unittest.TestCase):
    """Description"""

    def test_1(self):
        #code for testing

    def test_2(self):
        #code for testing

```

4) In order to verify the expected result and actual result we use the assert functionality of unittest module. We pass the actual result and expected result as arguments to this method.

> check testing_name_formatter.py

- In some test frameworks the test files will be imported. In python as a file is imported the interpreter is executing it. In case we want to avoid it from executing we add the code as below

``` Python

if __name__ = "__main__":
    unittest.main()

```

Here the file where the test case is being imported is main.py then only name is set to main satifying the if condition and then only the testcase are executed else it would not be executed.

Writing test cases from start are more beneficial in the long run as they ensure the any new code changes does not break the previous logic or else the code must be modified to support the backward compatibility.
