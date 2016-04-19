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

It’s possible to do operations on arrays of different sizes if Numpy can
transform these arrays so that they all have the same size: this conversion is
called broadcasting.

![numpy broadcasting in 2D](fig/numpy_broadcasting.png "numpy broadcasting in 2D")

Let's try to reproduce the above diagram. First, we create two one-dimensional arrays:

```
>>> a = np.arange(3) * 10
>>> b = np.arange(3)
>>> a
array([ 0, 10, 20])
>>> b
array([0, 1, 2])
```

We can tile them in 2D using `np.tile` function:

```
>>> b2 = np.tile(b, (3, 1))
>>> b2
array([[0, 1, 2],
       [0, 1, 2],
       [0, 1, 2]])
>>> a2 = np.tile(a, (3, 1))
>>> a2 = a2.T
>>> a2
array([[ 0,  0,  0],
       [10, 10, 10],
       [20, 20, 20]])
```

Then you can add them element-wise:

```
>>> a2 + b2
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22]])
```

Alternatively, you could directly add a 1D array to 2D array. NumPy will automatically "tile" the 1D array along the missing direction, however no copy is involved:

```
>>> a2 + b
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22]])
```

To obtain a column vector from a 1D array we need to convert it to 2D array by a special `np.newaxis` object:

```
>>> a.shape
(3,)
>>> a_column = a[:, np.newaxis]
>>> a_column.shape
(3, 1)
>>> a_column
array([[ 0],
       [10],
       [20]])
```

We can add a column vector and a 1D array:

```
>>> a_column + b
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22]])
```

This is the same as:

``` {.python}
>>> b_row = b[np.newaxis, :]
>>> b_row
array([[0, 1, 2]])
>>> b_row.shape
(1, 3)
>>> a_column + b_row
array([[ 0,  1,  2],
       [10, 11, 12],
       [20, 21, 22]])
```

> ## Normalising data {.challenge}
> 
> Calculate Z-score for each row of a 10x100 matrix.


Broadcasting seems a bit magical, but it is actually quite natural to use it when we want to solve a problem whose output data is an array with more dimensions than input data. There a simple rule that allow to determine the validity of broadcasting and the shape of broadcasted arrays:

>  In order to broadcast, the size of the trailing axes for both arrays in an operation must either be the same or one of them must be one. 

Lets look at two examples:

```
Image  (3d array): 256 x 256 x 3
Scale  (1d array):             3
Result (3d array): 256 x 256 x 3

A      (4d array):  8 x 1 x 6 x 1
B      (3d array):      7 x 1 x 5
Result (4d array):  8 x 7 x 6 x 5
```

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

> ## Three-dimensional broadcasting {.challenge}
>
> Below, produce the array containing the sum of every element in `x` with every element in `y`
>
> ```python
> x = np.random.rand(3, 5)
> y = np.random.randint(10, size=8)
> z = x # FIX THIS
> ```


A lot of grid-based or network-based problems can also use broadcasting. For instance, if we want to compute the distance from the origin of points on a 10x10 grid, we can do
```
>>> x = np.arange(5)
>>> y = np.arange(5)[:, np.newaxis]
>>> distance = np.sqrt(x ** 2 + y ** 2)
>>> distance
array([[ 0.        ,  1.        ,  2.        ,  3.        ,  4.        ],
       [ 1.        ,  1.41421356,  2.23606798,  3.16227766,  4.12310563],
       [ 2.        ,  2.23606798,  2.82842712,  3.60555128,  4.47213595],
       [ 3.        ,  3.16227766,  3.60555128,  4.24264069,  5.        ],
       [ 4.        ,  4.12310563,  4.47213595,  5.        ,  5.65685425]])
```

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

> ## Worked example: Route 66 {.callout}
>
> Let’s construct an array of distances (in miles) between cities of Route 66: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque, Flagstaff and Los Angeles.
> ```
> >>> mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544,
> ...        1913, 2448])
> >>> distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
> >>> distance_array
> array([[   0,  198,  303,  736,  871, 1175, 1475, 1544, 1913, 2448],
>        [ 198,    0,  105,  538,  673,  977, 1277, 1346, 1715, 2250],
>        [ 303,  105,    0,  433,  568,  872, 1172, 1241, 1610, 2145],
>        [ 736,  538,  433,    0,  135,  439,  739,  808, 1177, 1712],
>        [ 871,  673,  568,  135,    0,  304,  604,  673, 1042, 1577],
>        [1175,  977,  872,  439,  304,    0,  300,  369,  738, 1273],
>        [1475, 1277, 1172,  739,  604,  300,    0,   69,  438,  973],
>        [1544, 1346, 1241,  808,  673,  369,   69,    0,  369,  904],
>        [1913, 1715, 1610, 1177, 1042,  738,  438,  369,    0,  535],
>        [2448, 2250, 2145, 1712, 1577, 1273,  973,  904,  535,    0]])
>```
> ![Distances on Route 66](fig/route66.png)

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
> where $\phi_m = (\phi_1+\phi_2) / 2$ is the mean latitude.





