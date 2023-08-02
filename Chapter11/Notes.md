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

if __name__ == "__main__":
    unittest.main()

```

Here the file where the test case is being imported is main.py then only name is set to main satifying the if condition and then only the testcase are executed else it would not be executed.

Writing test cases from start are more beneficial in the long run as they ensure the any new code changes does not break the previous logic or else the code must be modified to support the backward compatibility.

The various type of asserts one can perform are as follows
1) assertEqual(a, b) -> asserts whether a and b are equal
2) assertNotEqual(a, b) -> asserts whether a and b are not equal
3) assertTrue(x) -> asserts whether x is True
4) assertFalse(x) -> asserts whether y is True
5) assertIn(item, list) -> asserts whether item is in list
6) assertNotIn(item, list) -> asserts whether item is not in list 

While executing the test cases module in the output various characters are printed. Here are their indications
1) `.` -> Indicates successful execution of the test case.
2) `E` -> Indicates an error is generated.
3) `F` -> Indicates the test case assertions has failed.

In order to test class behaviour by testing their methods the approach is similar to testing of functions behaviors. Here we create a test class with methods to which will test the methods of the class we want to test. Here in order to actually test the methods of class in case we must first create object and add test data to the attributes in each of the test method. This can be done once before the calling of any `test_` methods by performing the setup of a object of the class and other data in attributes in special method `setUp()`. The object created and other changes done to the will be available to all the `test_` methods as they are attached to `self`.

> check the no_setUp_testClass.py and setUp_testClass.py for more clarity.