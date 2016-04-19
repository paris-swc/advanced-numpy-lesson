---
layout: page
title: Advanced NumPy 
subtitle: Summing up
minutes: 30
---


> ## Quantile normalisation {.challenge}
>
> [Quantile Normalization](https://en.wikipedia.org/wiki/Quantile_normalization) is a method to align distributions. Implement it using NumPy axis-wise operations and fancy indexing.
> 
> Hint: look for documentation for `np.sort`, and `np.argsort`.*
>
> ```
> def qnorm(x):
>     """Quantile normalize an input matrix.
>     
>     Parameters
>     ----------
>     x : 2D array of float, shape (M, N)
>         The input data, with each column being a
>         distribution to normalize.
>         
>     Returns
>     -------
>     xn : 2D array of float, shape (M, N)
>         The normalized data.
>     """
>     return x 
> 
> import numpy as np
> data = np.array([[5, 4, 3],
>                  [2, 1, 4],
>                  [3, 5, 6],
>                  [4, 2, 7]])
> from numpy.testing import assert_array_almost_equal
> assert_array_almost_equal(qnorm(data), results, decimal=2)
> ```
