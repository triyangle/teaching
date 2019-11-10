* Any questions first?

# Asymptotic Analysis
* Why is this important?
* Important to analyze runtime of algorithms to distinguish/compare which ones are more
    performant and more scalable to larger input sizes (e.g. how to decide which of the
    many sorting algorithms are better?)
    * Input size in general is the size of the data our algorithm works on
        (e.g. length of list, number of vertices/edges in a graph)
* Since we are more interested in the performance of algorithms for large
    inputs, we usually only analyze the algorithm's performance as the input
    size $\to$ $\infty$, hence the name *asymptotic* analysis
    * *Enlightening Example:* Consider the functions $f(x) = x^{2}$ and $g(x) = x^{2} +
        100$. As $x \to \infty$ the importance of the constant term becomes
        less important. In fact, $\lim_{x \to \infty} \frac{f(x)}{g(x)} =
        \lim_{x \to \infty} \frac{x^{2}}{x^{2} + 100} = \lim_{x \to \infty}
        \frac{1}{1 + \frac{100}{x^{2}}} = 1$. So as $x \to \infty$, these
        functions approach the same values. They have the same *asymptotic*
        behavior.
* In general, to describe the performance of the algorithm with respect to the input size
    ($n$), we measure the number of times an operation is performed (instead of
    measuring exact time b/c this can vary a lot depending on your computer,
    whereas #
    of ops. is intrinsic to the algorithm itself, independent of the computer it is
    running on)
    * We can typically describe the number of times an operation is performed
        as a function of the input size
    * The runtime (in terms of number of operations performed) of the algorithm
        is then encapsulated by this function $f(n)$
    * *Ex:* For loop over a list of length $n$

## Order Notation
* To simplify the comparison of different algorithms, we can classify them into
    different complexity classes corresponding to their runtime as a function
    of the input size ($n$)

### Big Oh
* Suppose your algorithm has runtime $f(n)$. We say $f(n) \in O(g(n))$ if
    $\exists c, N \in \mathbb{R} : f(n) \leq c \cdot g(n)$ $\forall n > N$
    * In words: $f(n)$ is eventually bounded above by a constant multiple of $g(n)$
    * In pictures: draw picture
    * List iteration example
    * Drawbacks of Big Oh notation → upper bound can be arbitrarily large,
        may not give tightest possible bound
        * Need to also consider lower bounds

### Big Omega
* Suppose your algorithm has runtime $f(n)$. We say $f(n) \in \Omega(g(n))$ if
    $\exists c, N \in \mathbb{R} : f(n) \geq c \cdot g(n)$ $\forall n > N$
    * In words: $f(n)$ is eventually bounded below by a constant multiple of $g(n)$
    * In pictures: draw picture
    * List iteration example
    * Big Omega also may not give tightest possible lower bound
        * Need to also consider upper bounds
* Solution = Big Theta notation!

### Big Theta
* If $f(n) \in O(g(n))$ and $f(n) \in \Omega(g(n))$, then $f(n) \in
    \Theta(g(n))$
    * Draw picture
    * List example

## Examples
* Constant
* Logarithmic
    * Binary search
* Square root
    * Number of divisors
* Linear
    * List iteration
* Linearithmic
    * Merge sort
* Quadratic, cubic, etc.
    * Nested loops
* Exponential
    * Recursion
* Factorial
    * Generate all permutations of a list
    * Naive Traveling Salesman
* Once you have some basic examples, you can compose them with one another to
    determine the runtime of other algorithms that use them as building blocks

## Drawbacks
* Usually used only to consider **worst case** behavior (e.g. quicksort, simplex
    method), which may not always be the *average case* situation (quicksort $n
    \log{n}$ average)
* This type of analysis is only concerned with the asymptotic behavior of
    algorithms
* However, sometimes it can be appropriate to consider the performance of the
    algorithm for smaller input sizes
    * In this case, algorithmic analysis of the asymptotic behavior of the
        algorithm does not give us the complete picture of what's going on
    * Timsort (Python's default sorting alg.) uses insertion sort for smaller inputs
