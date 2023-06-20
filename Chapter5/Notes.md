# Notes

### Boolean Expression and Conditional test

An Expression which can result into an True or False value is called as _Boolean Expression_ or _Conditional Test_.

### Features

##### **in Keyword**

- To check whether an element exists in a list we can use the in keyword
- We can also use this to check if a list is empty or not. Here do check with len() function is the lenght is 0 or not. Cause even if the list contains elements or does not just `if list_name:` return True

``` Python

numbers = list(range(1,11))
if 11 in numbers:
	print("Miracle") # Conditional test in if block fails

if numbers:
	print("Empty list") # Checks whether the list numbers is empty or not. The condition should be len(numbers) == 0. Even if the numbers is non empty the above mentioned condition will result in True.

```

##### **not Keyword**

Used before in Keyword to check whether the mentioned element is not present in the list.

``` Python

numbers = list(range(1,11))
if 11 not in numbers:
	print("Its The truth") # Conditional test passes

```


