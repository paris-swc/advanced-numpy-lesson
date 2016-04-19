---
layout: page
title: Advanced NumPy 
subtitle: Broadcasting 
minutes: 30
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

> ## Distances {.challenge}
> 
> Given an array of latitudes and longitudes of major European capitals calculate pairwise distances between them. Use the approximate formula: 
>
> $$D=6371.009\sqrt{(\Delta\phi)^2 + (\Delta\lambda)^2}\qquad \text{(in kilometers)},$$
>
> where $\Delta\phi=\phi_1-\phi_2$ and $\Delta\lambda=\lambda_1-\lambda_2$ are the differences between the latitudes and longitude of two cities in radians. (*Hint*: To convert degrees to radians multiply them by $\pi/180$).
> ```
> coords = np.array([
>                   [ 23.71666667,  37.96666667],
>                   [ 13.38333333,  52.51666667],
>                   [ -0.1275    ,  51.50722222],
>                   [ -3.71666667,  40.38333333],
>                   [  2.3508    ,  48.8567    ],
>                   [ 12.5       ,  41.9       ]])
> names = np.array(['Athens', 'Berlin', 'London', 'Madrid', 'Paris', 'Rome'])
> ```
> When you are done you can compare the results with a more [precise formula](https://en.wikipedia.org/wiki/Geographical_distance#Spherical_Earth_projected_to_a_plane):
>
> $$D=6371.009\sqrt{(\Delta\phi)^2 + (\cos(\phi_m)\Delta\lambda)^2}$$
>
> where $\phi_m = (\phi_1+\phi_2) / 2$ is the mean longitude.
