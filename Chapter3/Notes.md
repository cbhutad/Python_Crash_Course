# Notes

### List intricacies

For a list in python the elements from last can be accessed using the negative indexes such as -1,-2 and so on where -1 indicates the index for last element.

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
