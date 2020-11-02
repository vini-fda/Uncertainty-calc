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

If you want to install the **latest version** from this repo, you need to:
 - `git clone` this repository(using http or ssh)
 - Make sure you're in the `master` branch
 - Run `pip install -e .` in the repository root(likely to be a directory called `u_calc/`) to [create a symlink](https://stackoverflow.com/questions/42609943/what-is-the-use-case-for-pip-install-e)
 - You're finished!:smile:
 
 **Note**: sometimes, you might have to use `python3 -m pip` instead of just `pip`. [You can read about this here](https://snarky.ca/why-you-should-use-python-m-pip/)
