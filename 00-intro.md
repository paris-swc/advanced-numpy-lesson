---
layout: page
title: Advanced NumPy 
subtitle: Introduction 
minutes: 15
---
> ## Learning Objectives {.objectives}
>
> * Learner will know how to import `numpy`
> * Learner will be able to create one- and more dimensional arrays with zeros/ones, given elements or random elements. 
> * Learner will be able to apply a function to all elements of an array.

NumPy array is a data container. It is similar to Python lists, but it's specialised for working on numerical data. NumPy is at the center of scientific Python ecosystem and it is a work-horse of many scientific libraries including scikit-learn, scikit-image, matplotlib, SciPy.

To use NumPy we need to start python interpreter and import `numpy` package -- it's customary the use the following import statement, which will make all NumPy functions available under the `np` prefix:

```
import numpy as np
```

If `numpy` was installed correctly, this should not produce any messages. Let's create a simple three-element NumPy array:

```
>>> x = np.array([2, 1, 5])
>>> x
array([2, 1, 5])
```

One of the advantages of NumPy is that it allows to apply functions (called `ufunc`s) to all elements of an array without the need of for loops:

```
>>> np.sin(x)
array([ 0.90929743,  0.84147098, -0.95892427])
```

This is not only convenient but also more efficient than iterating through the elements using for loops. Similarly, we can add scalars to all elements or multiply them by a constant:


```
>>> x + 1
array([3, 2, 6])
```

To construct an array with pre-defined elements we can also use one of the built-in helper functions. `np.arange` works like Python built-in `range`, but it returns an array; `np.ones` and `np.zeros` returns arrays of 0s or 1s; `np.random.rand` creates an array of random number from an interval [0, 1]:

```
>>> np.arange(5)
array([0, 1, 2, 3, 4])
>>> np.ones(5)
array([ 1.,  1.,  1.,  1.,  1.])
>>> np.zeros(5)
array([ 0.,  0.,  0.,  0.,  0.])
>>> np.random.rand(5)
array([ 0.27386612,  0.42769767,  0.38762774,  0.63308478,  0.46215844])
```

We can also construct a two- or more dimensional arrays:

```
>>> x = np.array([[1, 2], [5, 6]])
>>> x
array([[1, 2],
       [5, 6]])
>>> np.ones((2, 2))
array([[ 1.,  1.],
       [ 1.,  1.]])
```

Alternatively, a n-dimensional array can be obtained by reshaping a 1-D array:

```
>>> a = np.arange(9)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> a.reshape(3,3)
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
```

Note that in this case we used a method of the array itself called `reshape` rather than a function from NumPy module (`np.reshape`). Both ways are possible and it's usually only a matter of convenience which one we choose in a particular case.


> ## Creating a square array {.challenge}
>
> Create a 5x5 square array with number 5 on diagonal and zeros otherwise. Consider using `np.eye` function (you can check the docstring).
