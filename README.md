# simple-equ

An open source library containing multiple known STEM equations in a functional form. 

## Installation
```pip install simple-equ```

(For versions 3.8 or newer)

Optional: Use a venv (virtual environment).

## Usage

simple-equ is simple, yet practical. That is the problem is solves. Sure, someone with some knowledge in their field can implement this library's
functionality. But, let us look on how that would realistically look like: 

```
a = 3
b = 4
c = 4

"""
Here is an example of implementing a basic quadratic equation
"""
import math

delta = b**2 - 4 * a * c
solution1 = (-b + math.sqrt(delta)) / 2*a
solution2 = (-b - math.sqrt(delta)) / 2*a

"""
Here, just an import and a function call is needed!
"""

import simple_equ.math_general.algebra as sa

result = sa.basic_quadratic(a,b,c)
```
```
Looking to calculate the sin of an angle? Well... here is the algorithm to do this, is pseudo-code

function sin_taylor(x, n_terms):
    result = 0
    sign = 1             # alternates between + and -

    for i from 0 to n_terms-1:
        term_exponent = 2*i + 1
        term_factorial = factorial(term_exponent)
        term = sign * (x ^ term_exponent) / term_factorial
        result = result + term
        sign = -sign     # flip the sign for next term

    return result

function factorial(k):
    if k == 0 or k == 1:
        return 1
    else:
        f = 1
        for j from 2 to k:
            f = f * j
        return f

"""

import simple_equ.math_general.geometry as sg
sin30 = sg.sin(30) # In case you didn't notice, this is the same thing in simple_equ
```

```
"""
Normally, we would put a linear regression here. But it is pretty monsterous. Worry not though. This is how to do it with simple-equ:
"""

import simple_equ.economics.statistics as se

se.linear_regression([3,4,6],[4,6,7])
```

<img width="1233" height="185" alt="linearreg" src="https://github.com/user-attachments/assets/a09cc933-0e2b-493d-bbef-894115112f31" />

You just import the field of your liking, and then boom!

## Structure

The library is structured into fields. These fields have their own folder aka modules. However, a field can have multiple subsets. These subsets are usually 
present in the form of `python` files. For example: `algebra.py` and `geometry.py`, are examples of subfields of the general math field called **math_general**.

To import something in a practical sense in simple_equ, the structure looks like this: 

`import simple_equ.field.subfield as ...`

Practical examples include: 
`import simple_equ.math_general.geometry as sg`
`import simple_equ.economics.statistics as se`  

## Contributing

**Contributions are always welcome!**

The project encourages a community-driven approach. Everyone can contribute.
Be sure to be kind and respectful. Do not assume that something is known to the contributor
you are talking to just because you know it and do not be rude or even made comments about their
skill. This behaviour is not welcome here. 

See `contributing.md` for ways to get started.

## Features

- Community driven and open 
- Functions from different fields
- Reusable
- Highly accurate
- Simple yet practical

Do not forget to star the repo if you like it! It means a lot!
Thank you for reading this document and getting involved with our community :) 
