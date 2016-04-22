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

### Data type 

In contrast to built-in Python containers (like lists) the contents of NumPy arrays are statically **typed**, i.e. they can store elements only in specific format. To see the type of array contents you can use the `dtype` attribute. Let's look at two examples:

```
>>> a = np.array([1, 2, 3])
>>> a.dtype
dtype('int64')

>>> b = np.array([1., 2., 3.])
>>> b.dtype
dtype('float64')
```

In the first case the numbers are 64-bit (8-byte) integers and in the second 64-bit floating point (real)  numbers. Note that NumPy auto-detects the data-type from the input. Different data-types allow us to store data more compactly in memory, but most of the time we simply work with floating point numbers.

Note that all of the elements of an array must be of the same type. If we construct an array with different elements it will be **cast** to the "most general" type that can represent all elements. For example, array constructed from real numbers and integers will have a floating point data type:

```
>>> a = np.array([1., 2])
dtype('float64')
```

In cases it is impossible, NumPy will use an `object` type (also represented by capital `'O'`) which can represent any Python object -- even a function:

```
>>> def f(): pass
>>> a = np.array([f, f])
>>> a.dtype
dtype('O')
```

Some of NumPy features (like element-wise functions, `np.abs`, `np.sqrt`, etc., or reductions, `np.sum`, `np.max` etc.) won't work with object arrays, but all types of indexing still work.

`object` type is most commonly encountered when constructing an array from multiple lists of different lengths:

```
>>> np.array([[1], [2, 3]])
array([[1], [2, 3]], dtype=object)
```


> ## Integer or real number? {.challenge}
>
> Construct the array `x = np.array([0, 1, 2, 3], dtype=np.uint8)` (here, `uint8`
> represents a single byte in memory, an unsigned integer between 0 and 255). Can
> you explain the results obtained by x + 1 and x / 2? Also try `x.astype(float) + 1` and `x.astype(float) / 2`.

> ## Data types {.challenge}
>
> Try to guess the data type of the following arrays. Then test your prediction by  constructing the arrays and check their dtype attribute.
>
> ```
> a = np.array([[1, 2], 
>               [2, 3]])
> b = np.array(['a', 'b', 'c'])
> c = np.array([1, 2, 'a'])
> d = np.array([np.dot, np.array])
> e = np.random.randn(5) > 0
> f = np.arange(5)
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

NumPy array is just a memory block with extra information how to interpret its contents. Since memory has only linear address space, NumPy arrays need extra information how to lay out this block into multiple dimensions. This is done by means of `shape`  and `strides` attributes:

![Shape and strides](fig/strides.svg)

Lets try to reproduce this example. We first generate a 1D NumPy array of 8 elements:

```
>>> a = np.arange(8, dtype=np.uint8)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7], dtype=uint8)
>>> a.strides
(1,)
>>> a.shape
(8,)
```

`shape` and `strides` attributes are read-only, so we can not modify them directly. However, we my use 
`as_strided` function from NumPy library module:

```
>>> a1 = np.lib.stride_tricks.as_strided(a, strides=(4, 1), shape=(2,4))
>>> a1
array([[0, 1, 2, 3],
       [4, 5, 6, 7]], dtype=uint8)
```

Similarly, we can obtain the second example:
```
>>> a2 = np.lib.stride_tricks.as_strided(a, strides=(2, 1), shape=(3,4))
>>> a2
array([[0, 1, 2, 3],
       [2, 3, 4, 5],
       [4, 5, 6, 7]], dtype=uint8)
```

Note that in the second case the same data appears twice. However, it does not consume extra memory -- all three arrays share the same memory block:

```
>>> a[2] = 100
>>> a1
array([[  0,   1, 100,   3],
       [  4,   5,   6,   7]], dtype=uint8)
>>> a2
array([[  0,   1, 100,   3],
       [100,   3,   4,   5],
       [  4,   5,   6,   7]], dtype=uint8)
```

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
