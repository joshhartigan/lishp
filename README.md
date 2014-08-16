lishp
=====

An English-like language that transpiles to Python.

Some example Lishp code, that shows all its features (Lishp is a minimal language):

```
say hello, world!

set my_name to "Arnold"
set my_age  to 55

say I am {my_name} and I am {my_age}

add 1 to my_age

say in 1 year I will be {my_age}

take 1 from my_age

say as for now, I am stuck at {my_age} years.
```

The Python generated from the above code:

```python
print("hello, world!")
print("I am Arnold and I am 55")
print("in 1 year I will be 56")
print("as for now, I am stuck at 55 years.")
```
