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


### Multiplication by scalar and array

### Reshaping

`np.reshape`

### Axis-based reductions

### Special modules

> ## Finding closest element {.challenge}
>
> Generate a 10 x 3 array of random numbers. From each row, pick the number closest to 0.75. Make use of `np.abs` and `np.argmax` to find the column j which contains the closest element in each row.

> ## Solving linear equations {.challenge}
>
> Solve the following system of linear equations using numpy. Test the solution.
> $$2x_1 + 3x_2 = 3$$
> $$5x_1 - x_2 = 6$$
