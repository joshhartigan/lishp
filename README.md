# Lishp

An English-like language that transpiles to Python.

## Example

### my_program.lishp

```
set myName to Josh Hartigan
set myAge to 101
add 3 - 4 * 2 to myAge
take 9 from myAge
say {myName} is {myAge} years old.
```

### my_program.py
```
from __future__ import print_function

myName = "Josh" "Hartigan"
myAge = 101
myAge += 3 - 4 * 2
myAge -= 9
print(myName,  "is",  myAge,  "years",  "old.")
```
