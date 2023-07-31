# Notes

### Reading a file

In order to read a file in python this are the steps to follow
1) Open the file
2) Read the content at a go or line by line
3) Close the file

The opening and closing of file can be done using 2 seperate functions `open()` and `close()`. But if in case any error occurs and the file is not closed properly this can lead to the data being corrupted in the file which leads to an issue. So instead we can use the `with` statement in order to open a file and close it automatically once the content is read.

Syntax :

``` Python

with open("filename.txt") as objectname:
    #do stuff

```

Here as per the syntax the file will be represented by an object which can be referred with the objectname. The content of the string is stored in the memory. So as long as the memory is sufficient we can work with any size of data. The `open()` must be passed the location of the file or filename if it exists in the same folder as program in order to access the file. The path of the file can be relative or absolute. While providing absolute path in windows we have to provide `\`. This will be confused with escaping characters as the path is provided in string format. So we have to use the esacping character for backslash which is `\\` when providing absolute path in case of windows ecosystem. 

There are 2 main functions on the file object which can be used to read the content

* read() -> This will read the entire content from the file and return it in the form of a string. Also this returns a blank string when it reaches the end of the file and this might be added in the result when contents are printed (is applicable for previous versions. in `3.11` its not showing). So we might have to remove it. Now this can also be used to read the lines provided there are actual lines in the text file meaning there will be newline characters present `\n`. In such case we can use the for loop to read them one by one. Now since the contents are read as string during the display of the contents the newline characters will be printed as well.
> Check the file_reader.py example

* readlines() -> This will return the contents of the file as list of lines. Now the file object is available only in the scope of `with` keyword. So in order to access it outside the scope we can use this method in order to store the content as list and operate on it later on.
> Check pi_string.py example

#### Arguments for open()

* encoding - This argument must be used if the systems default encoding is different from the text file encoding.

``` Python

with open(filename,encoding="encoding") as file_obj:
    #code

```

### Writing to a file

In order to write to a file we must open it in either write, append or read & write modes. This can be specified as second parameter in the open() function.

`w -> write`
`a -> append`
`r+ -> read and write`

By default `r -> read` is default mode in which the file is opened. In case of `a` or append mode if the file does not exist a new file is created in the current folder.

### Exceptions and Handling

When a program executes and it does not handle _exceptions_ (special objects generated to indicate the errors that occurred) the program will halt and generate a _traceback_ which includes the report of exception generated.

The process of handling the exceptions in order to have a graceful exit of program and show a user friendly error messages instead of tracebacks we do _exception handling_.

So the mechanism to perform exception handling in python involves the use of `try-except-else` blocks.
1) try : This block will contain the code that might cause the exception.
2) except: This block represents a unique exception and is contains code that must be executed if the given exception does occur due to running of code in try block
3) else: This block contains the code to be executed if try block was executed successfully without any exception.

`pass` - This keyword is used if we don't want to execute any code when an exception occurs. So here in the except block instead of any error we just write pass and if exception occurs then it will be ignored.

### Working with JSON

In order to work with JSON data format, we can use the `json` module. 
API's encountered are :

1) dump() -> This will dump the data from a python list, dictionary or variable into a file with json extension. So the arguments to be passed are variable and file object (needs to be opened in write mode)

``` Python

import json

nums = [1,2,3,4]
file = "dummy.json"

with open(file,"w") as file_obj:
    json.dump(nums,file_obj)

```

2) load() -> reads the json extension file and returns the data that can be stored in a varibale in python. The file needs to be opened in read mode

``` Python

import json

file = "dummy.json"

with open(file,"r") as file_obj:
    contents = json.load(file_obj)

print(contents)

```