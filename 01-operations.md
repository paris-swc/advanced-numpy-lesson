---
layout: page
title: Advanced NumPy 
subtitle: Operations on NumPy arrays
minutes: 5
---
> ## Learning Objectives {.objectives}
>
> * Learner will explain the difference between element-wise and matrix product of two arrays.
> * Learner will apply reduction functions (mean, min, max) along a given axis.
> * Learner find a specialised numerical algorithm from the ones available in numpy.
> * Learner will be able to use from several sorting routines.

Multiplication of two arrays is elementwise. For example, to calculate a square of each element we may use:

```
>>> a = np.arange(3)
>>> a
array([0, 1, 2])
>>> b = a * a
>>> b
array([0, 1, 4])
```

Matrix products are calculated using the `np.dot` function:

```
>>> np.dot(a, a)
5
```

For 1-D arrays the same result can be obtained by:

```
>>> np.sum(a * a)
5
```

### Axis-based reductions

The `np.sum` function sums all elements regardless of the number of array dimensions:


```
>>> b = np.arange(9).reshape(3,3)
>>> b
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> np.sum(b)
36
```

If we want to sum only columns or rows, we need to pass the index of the axis over which we want to sum:

```
>>> np.sum(b, 0)
array([ 9, 12, 15])
>>> np.sum(b, 1)
array([ 3, 12, 21])
```

Other similar reduction functions are `np.min`, `np.max` or `np.mean`:

```
>>> np.min(b)
0
>>> np.min(b, 0)
array([0, 1, 2])
>>> np.min(b, 1)
array([0, 3, 6])
```

We can also find the index of the minimum element in each axis:

```
>>> np.argmin(b, 0)
array([0, 0, 0])
```

### Sorting

NumPy also implement various sorting algorithms. To sort elements of an array we can simply use `np.sort` functions:

```
>>> a = np.random.rand(4)
>>> a
array([ 0.9490829 ,  0.07528673,  0.17463988,  0.95964801])
>>> np.sort(a)
array([ 0.07528673,  0.17463988,  0.9490829 ,  0.95964801])
```

By default, `np.sort` flattens the array (make it 1-D) before sorting, but similarly to the reduction functions we can also pass the axis index to sort along: 

```
>>> b = a.reshape(2, 2)
>>> b
array([[ 0.9490829 ,  0.07528673],
       [ 0.17463988,  0.95964801]])
>>> np.sort(b, 0)
array([[ 0.17463988,  0.07528673],
       [ 0.9490829 ,  0.95964801]])
>>> np.sort(b, 1)
array([[ 0.07528673,  0.9490829 ],
       [ 0.17463988,  0.95964801]])
```

We can also find the order in which elements need to be placed to have them sorted:

```
>>> np.argsort(a)
array([1, 2, 0, 3])
```

### Special modules

NumPy also provides extra modules implementing basic numerical methods:

* `np.linalg` -- linear algebra,
* `np.fft` -- fast Fourier transform,
* `np.random` -- random number generators.

> ## Finding closest element {.challenge}
>
> Generate a 10 x 3 array of random numbers. From each row, pick the number closest to 0.75. Make use of `np.abs` and `np.argmax` to find the column j which contains the closest element in each row.

> ## Solving linear equations {.challenge}
>
> Solve the following system of linear equations using numpy. Test the solution.
> $$2x_1 + 3x_2 = 3$$
> $$5x_1 - x_2 = 6$$
