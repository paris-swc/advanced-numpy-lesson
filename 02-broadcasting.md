---
layout: page
title: Advanced NumPy 
subtitle: Operations on NumPy arrays
minutes: 5
---
> ## Learning Objectives {.objectives}
>
> After the lesson learner:
>
> * Knows how to add a scalar to all elements of an array.
> * Can predict the result of additions of matrices and row or column vectors.
> * Can explain why broadcasting is better than using for loops.
> * Understands the rules of broadcasting and can predict the shape of broadcasted arrays.
> * Knows how to control broadcasting using `np.newaxis` object.


> ## Normalising data {.challenge}
> 
> Calculate Z-score for each row of a 10x100 matrix.

> ## Three-dimensional broadcasting {.challenge}
>
> Below, produce the array containing the sum of every element in `x` with every element in `y`
>
> ```python
> x = np.random.rand(3, 5)
> y = np.random.randint(10, size=8)
> z = x # FIX THIS
> ```

> ## Broadcasting rules {.challenge}
> 
> Given the arrays:
> ```
> X = np.random.rand(10,3)
> Y = np.random.rand(3)
> ```
> 
> which of the following will *not* produce an error:
> 
> a) `X + Y`
> 
> b) `X[None, :] + Y`
> 
> c) `X[np.newaxis, :] + Y`
> 
> d) `X[None, :] + Y[:, None]`
> 
> e) `X[:, np.newaxis] + Y`
> 
> f) `X + Y[np.newaxis, :]`
> 
> What will be the shapes of the final broadcasted arrays? Try to guess and then check using `np.broadcast_arrays`.

> ## Creating a two-dimensional grid {.challenge}
> 
> What are the dimensionalities of `x`, `y` and `z` in the two cases:
>
> ```
> x, y = np.mgrid[:10, :5]
> z = x + y
> ```
> 
> and 
> 
> ```
> x, y = np.ogrid[:10, :5]
> z = x + y
> ```
> 
> What might be the advantage of using `np.ogrid` over `np.mgrid`?
