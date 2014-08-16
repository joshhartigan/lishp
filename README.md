lishp
=====

An English-like language that transpiles to Python.

Some example Lishp code:

```
say hello there

set old to 100
set young to 2

say if you are {young} then you are young!
say if you are {old} then you are old!
```

The Python generated from the above code:

```python
print("hello there")
print("if you are 2 then you are young!")
print("if you are 100 then you are old!")
```
