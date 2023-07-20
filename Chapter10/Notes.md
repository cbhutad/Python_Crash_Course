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


