# Notes

### Definitions

**Dictionary** -> Its a collection of key-value pairs. The number of key-value pairs can be unlimited.

### Points to note

- The key in this pairs can be a string or number.
- The value can be number, string, list or dictionary itself.

### Features

##### **Dictionary**

- The order of insertion of key-value pairs in dictionary is maintained.

_Syntax_ :

``` Python

person = {
	key1 : value,
	key2 : value,
}

```

The last ending key-value pair also has comman at the end.

_Operations on dictionary_ : 

1) Add : To add a new key-value pair to a dictionary we use the following syntax

``` Python

person[key3] = value3

``` 

2) Update : To update an existing value for a key we can use the following syntax

``` Python

person[key2] = updatedValue2

```

3) Delete : To remove a value from dictionary we can use the below syntax

``` Python

del person[key1]

```

Once a key-value pair is deleted its not recoverable.

4) Read : To read the value for a key in dictionary we can use 2 ways either the specifying key as index or using the get API.

Using the key as index way:

``` Python

print(person[key2])

```
This approach has a drawback that if the mentioned key is not present in the dictionary then we get `KeyError`.

Using the get API:

``` Python

print(person.get(key2, default-value))

```
Using this approach allows us to retrieve a set default value in case the mentioned key is not present in the dictionary. Also this way we do not receive the error

_Looping through dictionary_ :

We can loop through a dictionary in 3 ways:

1) Looping through the keys

This can be done using the keys() API. This will return a list containing the keys in the dictionary.

``` Python

for key in person.keys():
	#do something

```

2) Looping through the values

This can be done using the values() API. This will return a list containing the values in the dictionary.

``` Python

for value in person.values():
	#do something

```

3) Looping the key-value pairs

This can be done using the items() API.

``` Python

for key,value in person.items():
	#do something

```

##### **Set**

This is another inbuild data type in which we can store only unique elements. Here there is no order maintained so we cannot access the elements in indexed way.

_Syntax_ :

``` Python

setElements = {element1, element2, element3}

```
Even if we add duplicates during the initalization of list only the unique values among them are stored.

##### **Nesting**

The dictionaries can be nested in the following manner:

1) List of dictionaries
2) Dictionaries with list as values
3) Dictionaries with dictionaries as values