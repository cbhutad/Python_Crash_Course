# Notes

### Boolean Expression and Conditional test

An Expression which can result into an True or False value is called as _Boolean Expression_ or _Conditional Test_.

### Features

##### **in Keyword**

- To check whether an element exists in a list we can use the in keyword
- We can also use this to check if a list is empty or not

``` Python

numbers = list(range(1,11))
if 11 in numbers:
	print("Miracle") # Conditional test in if block fails

if numbers:
	print("Empty list") # Checks whether the list numbers is empty or not.

```

##### **not Keyword**

Used before in Keyword to check whether the mentioned element is not present in the list.

``` Python

numbers = list(range(1,11))
if 11 not in numbers:
	print("Its The truth") # Conditional test passes

```


