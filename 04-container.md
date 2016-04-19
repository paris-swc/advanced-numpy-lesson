---
layout: page
title: Advanced NumPy 
subtitle: Array container
minutes: 45
---
> ## Learning Objectives {.objectives}
>
> After the lesson learner:
>
> Learning objectives:
>
> * Can list some of the object types which can be contained in an array.
> * Understands the concept of `dtype` and can select `dtype` best for the data at hand.
> * Knows what is an object array and when it is created.
> * Can explain what are `ndim`, `shape` and `stride` properties of an array.
> * Understand the layout of an array in memory and knows how to use it for best array performance.
> * Can explain the difference between Fortran- and C-based order. Knows the default.

### `dtype`

> ## Integer or real number? {.challenge}
>
> Construct the array `x = np.array([0, 1, 2, 3], dtype=np.uint8)` (here, `uint8`
> represents a single byte in memory, an unsigned integer between 0 and 255). Can
> you explain the results obtained by x + 1 and x / 2? Also try `x.astype(float) + 1` and `x.astype(float) / 2`.

> ## Data types {.challenge}
>
> What is the dtype of the following arrays?
>
> ```
> a = np.array([[1], 
>               [2,3],
>               [4,5,6]])
> b = np.array(['a', 'b', 'c'])
> c = np.array([1, 2., 3.])
> d = np.array([np.dot, np.array])
> ```

> ## Complex data types {.challenge}
>
> Imagine you have a list of names and scores, which you want to store in numpy array. Construct a dtype such that the following works. Look at documentation of `np.dtype`.
>
> ```
> dtype = ?
> np.array([('Bartosz', 5), ('Nelle', 4)], dtype=dtype)
> ```

### Memory layout

> ## Transpose {.challenge}
>
> Create 3x4 random array. Have a look at its different properties: ``x.shape``, ``x.ndim``,
``x.dtype``, ``x.strides``. What does each property tell you about the array?
> 
> Compare the strides property of x.T to the above. What is x.T and can you
explain the new strides?

> ## Fastest changing index {.challenge}
>
>  Compare the time of summing over rows and columns of an array `A = np.random.rand(10, 100000)`. How would you explain the differences?

> ## Sliding window {.challenge}
>
> Use `as_strided` to produce a sliding-window view of a 1D array.
>
> ```
> def sliding_window(arr, size=2):
>     """Produce an array of sliding window views of `arr`
>     
>     Parameters
>     ----------
>     arr : 1D array, shape (N,)
>         The input array.
>     size : int, optional
>         The size of the sliding window.
>         
>     Returns
>     -------
>     arr_slide : 2D array, shape (N - size - 1, size)
>         The sliding windows of size `size` of `arr`.
>         
>     Examples
>     --------
>     >>> a = np.array([0, 1, 2, 3])
>     >>> sliding_window(a, 2)
>     array([[0, 1],
>            [1, 2],
>            [2, 3]])
>     """
>     return arr  # fix this
> ```

> ## Fortran or C-ordering? {.challenge}
>
> The `order` keyword of some `numpy` functions determines how two- or more dimensional arrays are laid out in the memory. If order is 'C', then the array will be in C-contiguous order (last-index varies the fastest). If order is 'F', then the returned array will be in Fortran-contiguous order (first-index varies the fastest). In what order will be the 2D array stored in memory? (*Hint*: You can use `np.ravel(x, order='A')` to test it).

> ## Broadcasting revisited {.challenge}
>
>  Explain how broadcasting works internally using the example below. What will be shapes and strides of `x` and `y` after broadcasting. Test it using `np.broadcast_arrays` in the following example and look at `strides` and `shape` properties of both arrays.
