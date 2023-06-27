# Notes

### Taking user input

In order to read input from user we can use the `input()` function.

Syntax :

``` Python

input(prompt)

```

Here the prompt is argument of type string which we can pass to the user indicating him what he should be enter as the data. The entered data here is taken as string type.

``` Python

message = print("Enter the message you want to pass : ")
print(message)

```

Here the data being entered by user will be on the same line as prompt is being printed. Also we can print multiple lines prompt. 

``` Python

message = print("Enter the message on the line below.\n message : ")
print(message)

```

In order to take the numerical input from the user one can use the `int()` function. Here the string argument is passed to function which is a numeric string. This function will perform numeric conversion of the same.

``` Python

age = int(input("Enter your age : "))
print("Age is : ")

```

### While loop

The main use for while loop is to automate the execution of certain tasks until the given condition is satisfied. If the condition fails the execution is stopped.

Syntax :

``` Python

while condition:
	operation

```

In order for the while loop to end the condition must fail after certain iterations. If say we are checking the condition after while keyword we must check for the condition to fail in the operation of while loop.

``` Python

current_number = 1
flag = True
while flag:
	if current_number == 6:
		flag = False
	else:
		current_number += 1

```

We can also use the `break`, `continue` along with the for and while loops as we do in other programming languages.

