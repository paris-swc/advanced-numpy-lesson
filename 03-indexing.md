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


> ## View or copy {.challenge}
>
> Create a 3x4 array of
> random values (using `np.random.rand`), and call it ``x``.
> Create another array as follows: ``y = x[2]``.
> What happens when you modify ``y`` &mdash; does ``x`` also change? Now try `y = x[:2]` and modify it's first element. What happens now?

> ## Checkerboard {.challenge}
>
> Create a 8x8 matrix and fill it with a checkerboard pattern

### Boolean indexing

> ## Rectification {.challenge}
>
> Rectify an array with random numbers from normal distribution (generated with `np.random.randn`) using boolean indexing.

> ## Criterion-based selection {.challenge}
> 
> Select odd elements from an integer array.

### Fancy indexing

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

### K-mean clustering
