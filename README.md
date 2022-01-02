# pyoccur

## Python Occurrence Operations on Lists

### About Package
A simple python package with 3 functions

* has_dup(<listparam>)
* get_dup(<listparam>)
* remove_dup(<listparam>)

Currently the duplicate operation functions can operate on list of elements with below data types

* str
* int
* float
* dict
* list
* pandas.DataFrame

### Example
```
from pyoccur import pyoccur
l1 = ['abc',123,'def','abc',22,10]
l2 = [{'abc':100},'wee',123,{'abc':100},'abc',123,{'a':1,'b':2}]
pyoccur.has_dup(l1)
# Output: True
pyoccur.get_dup(l2)
# Output: [{'abc':100},123]
```

### Contributing
- Feel free to raise PR to add your contributions
- Do raise issues if found any, in the Github Issues
