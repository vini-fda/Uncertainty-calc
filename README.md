# u-calc: A calculator with uncertainties

Tired of doing physics calculations by hand or with spreadsheets? Look no further, because this python module is here to make these calculations as easy as ever!

## HOW TO

A simple use case: adding two numbers with uncertainties. 

Let's say `x = (23.00 +- 0.01)` and `y = (12.02 +- 0.03)`.

Open up the python interpreter and:

```python3
>>> from u_calc.measurement import Measurement as Msm
>>> x = Msm(23.00, 0.01)
>>> y = Msm(12.02, 0.03)
>>> print(x+y)
35.020 \pm 0.032
```

In your python files, you can just `import` this module just like any other.

## Installation

To install it, you only need `pip`. Example for v0.0.1:
```bash
$ pip install u-calc==0.0.1
```