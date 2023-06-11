# Notes

### Better to Know

Number data type can be classified as integers or floats.
	- Float is type displayed for operation of division between any combination of number types `integer/integer, float/integer and integer/float`
	- The result of operation is always the float type is any of the operand is of float type.

### Defintions

**Traceback** is a record which shows where the interpreter ran into trouble while executing the python code.
**Method** refers to an action which can be performed on a variable.
**Whitespaces** refer to any nonprinting character such as _spaces, tabs or newlines._


### API's

String API encountered

- title() -> Capitalizes the first character for each word in the variable or sentence.
- upper() -> Converts to uppercase letters.
- lower() -> Converts to lowercase letters.
- rstrip() -> Removes the whitespaces on the right extremes of the string (at the end of string). This api does not have any effect unless the result of operation is reassinged to the original variable.
- lstrip() -> Removes the whitespaces on the left extremes of the string(at the start of the string). This api does not have any effect unless the result of operation is reassinged to the original variable.
- strip() -> Removes the whitespaces on both sides of the string. This api does not have any effect unless the result of operation is reassinged to the original variable.

``` Python

	let message = "Hello "
	message.strip() # if performed on terminal will display the whitespace removed
	print(message) #prints 'Hello '. the original string in variable is unaffected.

	message = message.strip()
	print(message) #print 'Hello' the desired result is obtained.

	# Same applies for rstrip,lstrip and strip API's.

```

### Features

##### **f_strings**

- This feature is similar to that of template literals in Javascript.
- Here we can format the string to produce a dynamic output by adding variables in it.

``` Python

	#Syntax f is required to be followed by double quotes or single quotes.

	f"{} {}" #here the {} will include the variable names to be displayed when the result is executed.
	f'{} {}'
	
```

- We can also assign this f_strings to a variable to store the result and perform API operations on it directly as well.

``` Python
	
	message = f"{} {}"
	f"{variable.title()} {}" #shows how API can be used on variables mentioned in f_strings

```

_Use Case_:
	The following feature can used when we want to format strings based on a variable value.

##### Underscores in integers, floats

- This features allows us to make large numbers more readable. Can be used with either integers or floats.

``` Python

number = 14_000_000_000
print(number) #output is 14000000000
 
```

##### Multiple Variable Assignments

- This allows to initalize multiple variables via a single line of code. As long as the number of variables match the number of arguments proper mapping is done by python

``` Python

a,b,c = 1,2,3

print(a) # 1
print(b) # 2
print(c) # 3

```

### Error's

1) NameError -> This occurs if interpreter notices the varibale which is not defined and used, or other keyowords in the python program.
2) SyntaxError -> This occurs if there are misspelled variable or keywords in the python program.

