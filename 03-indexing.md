---
layout: page
title: Advanced NumPy 
subtitle: Indexing 
minutes: 45
---
> ## Learning Objectives {.objectives}
>
> After the lesson learner:
>
> * Can get the value of any element of a N-dimensional array knowing its row, column etc. 
> * Can use slices to get and modify ranges of elements.
> * Can explain the difference between a copy and a view. Knows which methods of indexing return a copy or view.
> * Knows how to select elements from an array based on some criteria applied to their values.
> * Can obtain a sub-array of non-contiguous of elements using fancy indexing.
> * Can combine axis-based reductions, broadcasting and indexing to implement simple clustering algorithms.
> * Understands what are the advantages of vectorisation and when to use or not use it.

### Integer indexing and slicing

Individual items of an array can be accessed by the integer index of the element (starting with 0):

```
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a[0], a[2], a[-1]
(0, 2, 9)
```

For two- or more dimensional arrays multiple indices should be specified:

```
>>> b = np.arange(6).reshape(2,3)
>>> b
array([[0, 1, 2],
       [3, 4, 5]])
>>> b[1, 2]
5
```

Slicing allows to extract sub-arrays of multiple elements from the array. It's defined by three integers separated by a colon, i.e. `start:end:increment`. Any of the values can be skipped in which case they are replaced by defaults (0 for start, -1 for end and 1 for increment):

```
>>> c = np.arange(9)
>>> c[1:3]
array([1, 2])
>>> c[:3]
array([0, 1, 2])
>>> c[1:]
array([1, 2, 3, 4, 5, 6, 7, 8])
```

You can also assign elements with slices and indexes:

```
>>> c
array([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> c[1:8:2]=1000
>>> c
array([   0, 1000,    2, 1000,    4, 1000,    6, 1000,    8])
```

> ## View or copy {.challenge}
>
> Create a 3x4 array of
> random values (using `np.random.rand`), and call it ``x``.
> Create another array as follows: ``y = x[2]``.
> What happens when you modify ``y`` &mdash; does ``x`` also change? Now try `y = x[:2]` and modify it's first element. What happens now?

> ## Checkerboard {.challenge}
>
> Create an array of zeros and fill it with a checkerboard pattern with of size 8x8.
>
> ![](fig/checkerboard.svg)

### Boolean mask

Sometimes we may want to select array elements based on some criterion. For this case boolean mask is very useful. The mask is an array of the same length as the indexed array containg only `False` or `True` values:

```
>>> a = np.arange(4)
>>> a
array([0, 1, 2, 3])
>>> mask = np.array([False, True, True, False])
>>> a[mask]
array([1, 2])
```

In most cases the mask is constructed from the values of the array itself. For example, to select only odd numbers we could use the following mask:

```
>>> odd = (a % 2) == 1
>>> odd
array([False,  True, False,  True], dtype=bool)
>>> a[odd]
array([1, 3])
```

This could be also done in a single step:

```
>>> a[(a % 2) == 1]
array([1, 3])
```

Indexing with a mask can be also useful to assign a new value to a sub-array:

```
>>> a[(a % 2) == 1] = -1
>>> a
array([ 0, -1,  2, -1])
```

> ## View or copy? {.challenge}
>
> What are the final values of `a` and `b` at the end of the following program? Explain why.
>
> ```
> a = np.arange(5)
> b = a[a < 3]
> b[::2] = 0
> ```
> 
> a) `a = [0, 1, 2, 3, 4], b = [0, 1, 2]`
> b) `a = [0, 1, 0, 3, 4], b = [0, 1, 0]`
> c) `a = [0, 0, 2, 3, 4], b = [0, 0, 2]`
> d) `a = [0, 1, 2, 3, 4], b = [0, 1, 0]`
> e) `a = [0, 1, 2, 3, 4], b = [0, 1, 0, 3, 0]`

> ## Rectification {.challenge}
>
> Rectify an array with random numbers from normal distribution (generated with `np.random.randn`) using boolean indexing.

### Fancy indexing

Indexing can be done with an array of integers. In this case the same index can be also repeated several times:

```
>>> a = np.arange(0, 100, 10)
>>> a
array([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
>>> a[[2, 3, 2, 4, 2]] 
array([20, 30, 20, 40, 20])
```

New values can be also assigned with this kind of indexing:

```
>>> a[[9, 7]] = -100
>>> a
array([   0,   10,   20,   30,   40,   50,   60, -100,   80, -100])
```

When a new array is created by indexing with an array of integers, the new array has the same shape than the array of integers. Note that the array returns a copy and not a view.

```
>>> a = np.arange(10)
>>> idx = np.array([[3, 4], [9, 7]])
>>> idx.shape
(2, 2)
>>> a[idx]
array([[3, 4],
       [9, 7]])
```

> ## Random elements {.challenge}
>
> Using fancy indexing Select randomly with repetition 10 elements from an array of 100 elements.

> ## Drawing random integers without repetition {.challenge}
>
> Generate a random sequence of 10 integers from 1 to 100 without repetition (you may want to use `np.random.rand` and `np.argsort`).

> ## Broadcasting indices {.challenge}
>
>Predict and verify the shape of the following operation.
> 
> ```python
> x = np.empty((10, 8, 6))
> 
> idx0 = np.zeros((3, 8)).astype(int)
> idx1 = np.zeros((3, 1)).astype(int)
> idx2 = np.zeros((1, 1)).astype(int)
> 
> x[idx0, idx1, idx2]
> ```

> ## Sub-arrays {.challenge}
> 
> Let `x = np.array([1, 5, 10])`.
> 
> Which of the following will show [1, 10]:
> 
> a) `print(x[::2])`
> 
> b) `print(x[[0, 2]])`
> 
> c) `x[1, 3]`
> 
> d) `x[[1, -1]]`
>
> e) `x[[False, True, False]]`
>
> For each statement predict whether it returns a copy or a view.

