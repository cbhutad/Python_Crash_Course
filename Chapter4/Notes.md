# Notes

### Syntax for loop

``` Python


for variablename in collectionname:
	operations

```

Here the variablname can be anything but usually the preferred convention is to use a name which aligns well with individual element in the collection.

### Common syntax errors observed with for loop

1) Missing indentation after for loop

``` Python

for cat in cats:
print(cat)

```

Here we get _IndentationError_ from python.

2) Forget to add indentation to few lines

``` Python

for cat in cats:
	print(cat)
print("cats are senile")

```

Here say we want to print second print() for each cat but since its not a part of indentation of for loop the line won't be printed for each element in the list but will be printed at the end of for loop. This is a logical error.

3) Indenting unessecary lines

``` Python

names = "cheenmaya"
	print(name)

```

Here we get _IndentationError_ as we are not indenting the statement with respect to a code block. This will cause python to raise error.

4) Indenting lines which are not part of for loop

``` Python

for cat in cats:
	print(cat)
	print(cat + "1")




	print("Hello there")

```

Here the 3rd print is also considered to be part of indented code as there exists a indentation before it and no other statements exist between the print and for loop. So the 3rd print statement will be executed for each iteration of for loop.


### API's

1) range(start,stop,stepsize) -> Generates the mentioned numbers from start and ends at stop-1. If the third argument stepsize is also provided then it skips to the next number as start,start + stepsize, start + 2xstepsize and so on (can be applied to generate even and odd numbers). If only one argument is passed then this is considered as stop argument and here the numbers are generated starting from 0 to stop-1. We can also pass this as argument to list function `list()` in order to generate a numerical list.

``` Python

evenNumbers = list(range(2,11,2)) #generates a list containing even numbers less than equal to 10.

```

2) min() -> This can be used to find minimum value in a numerical list by passing the list as argument to the function.

3) max() -> This can be used to find maximum value in a numerical list by passing the list as argument to the function.

4) sum() -> This can be used to find sum of all the elements in a numerical list by passing the list as argument to the function.

### Features

##### **List Comprehensions**

This feature allows us to perform following 3 operations related to list in one line of code

- Initialize a empty list to a variable name
- Loop across a range of quantities. 
- Perform a given operation for each of this quantity and assign the result as an element to the list.

Syntax for list comprehension is as follows:

list_name = [operation_to_perform loop_over_quantities_code]


Consider the example to find a cube of first 10 natural numbers

Normal approach without list comprehensions:

``` Python

cubes = []
numbers = list(range(1,11))

for number in numbers:
	cubes.append(number ** 3)

```

List Comprehension approach:

list_name => cubes\
operation_to_perform => number ** 3\
loop_over_quantities_code => for number in range(1,11)

``` Python

cubes = [number ** 3 for number in range(1,11)]

print(cubes) # 1,8,27 and so on

```

##### Slicing

This feature allows us to work with sublist of list. 

- The syntax is `list_name[start_index:stop_index]`. Here both start_index and stop_index are optional. 
- `list_name[start_index:stop_index]` returns list with elements whose index is from start_index to stop_index-1.
- `list_name[:stop_index]` returns list of elements from start of list to the stop_index-1 elements.
- `list_name[start_index:]` return list of elements from start_index from list to the end of list.
- We can also pass negative index as the start_index and stop_index in the syntax.
- `list_name[:]` allows us to make a copy of the list. This provides with what we call a deep copy(in java). 

``` Python

numbers = list(range(1:11))

numbers_copy = numbers[:]

print(numbers)
print(numbers_copy)

```

##### Tuples

This are called as immutable list. An tuple is list of elements which is ordered but the individual elements in the list cannot be modified. Only we can change the reference of the tuple variable.

- Tuple are declared with paranthesis instead of square brackets.
- If we try to modify an element from the tuple we get a TypeError.

``` Python

dimesions = (3,4)
dimensions[0] = 5 # not allowed. Gives TypeError
dimesions = (4,5) # allowed.

```

- To create a tuple with a single element we must add comma at the end of the element.

``` Python

dimesions = (3,) # for a single element tuple 

```

### Observations

In python the ** operator is usually used to find square of a number but we can also find a respective power of a number by mentioning the number after this operator. 

To find cube => 2 ** 3
To find fourth power => 2 ** 4 and so on.
