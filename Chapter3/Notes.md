# Notes

### List intricacies

- All the list variable names must be plural form.
- For a list in python the elements from last can be accessed using the negative indexes such as -1,-2 and so on where -1 indicates the index for last element.
- List can contain elements of multiple data types in it. We cannot perform sort operation on such list.

### Definitions

**List** Collection of elements stored in a order. They are 0-indexed.

### API's

1) append() -> Adds an element to the end of the list.
2) insert() -> Allows us to add the element at the mentioned index.

``` Python

months = ["Jan", "Feb", "Mar", "Apr", "Jun"]
months.insert(4,"May")

``` 

3) del -> Used to remove an element from a list. Once deleted we cannot access it after the operation.

``` Python

numbers = [1,2,3,4,5,6,7]

del numbers[2] #numbers = [1,2,4,5,6,7]

```

4) pop() -> Used to remove an element from a list. We can store the value of removed element into a variable for future use after this operation. If no index is specified then it removes the last element from the list.

``` Python

numbers = [1,2,3,4,5,6,7]

value = numbers.pop(2) # value = 3

```

5) remove() -> Used to remove element whose value is passed as argument. This will remove only the first occurence for the element if multiple such elements exist in the list.

``` Python

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
months.remove("Jul") #["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Aug", "Sep", "Oct", "Nov", "Dec"]

```

6) sort() -> sorts the elements in alphabetical order. To sort in reverse order alphabetically we can pass the argument reverse = True to the function call.

``` Python

months.sort()
months.sort(reverse=True)

```

7) sorted() -> Only prints the element of the list is sorted order but does not change the arrangement of list elements. To display the reverse order of sorting we can reverse = True as an argument to function call.

``` Python

sorted(months)
sorted(months,reverse=True)

```

8) reverse() -> Reverse the elements order in the list. To revert back to original order we can pass reverse=True argument to it.

``` Python

months.reverse()

```

9) len() -> Gives the length of the array. 

``` Python

len(months)

```

### Error's

- IndexError -> Occurs when an index which does not exist for the list is asked for.

