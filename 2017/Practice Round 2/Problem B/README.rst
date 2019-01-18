.. _Problem B. Safe Squares: https://code.google.com/codejam/contest/12254486/dashboard#s=p1

==========================
`Problem B. Safe Squares`_
==========================

Problem
-------
Codejamon trainers are actively looking for monsters, but if you are not a
trainer, these monsters could be really dangerous for you.
You might want to find safe places that do not have any monsters!

Consider our world as a grid, and some of the cells have been occupied by
monsters. We define a *safe square* as a grid-aligned **D** × **D** square of
grid cells (with **D** ≥ 1) that does not contain any monsters. Your task is
to find out how many safe squares (of any size) we have in the entire world.

Input
-----
The first line of the input gives the number of test cases, **T**.
**T** test cases follow. Each test case starts with a line with three
integers, **R**, **C**, and **K**. The grid has **R** rows and **C** columns,
and contains **K** monsters. **K** more lines follow; each contains two
integers **R**\ |i| and **C**\ |i|, indicating the row and column that the
i-th monster is in. (Rows are numbered from top to bottom, starting from 0;
columns are numbered from left to right, starting from 0.)

.. |i| raw:: html

    <b><sub>i</sub></b>

Output
------
For each test case, output one line containing ``Case #x: y``,
where ``x`` is the test case number (starting from 1)
and ``y`` is the the total number of safe zones for this test case.

Limits
------
1 ≤ **T** ≤ 20.

(**R**\ |i|, **C**\ |i|) ≠ (**R**\ |j|, **C**\ |j|) for i ≠ j.
(No two monsters are in the same grid cell.)

0 ≤ **R**\ |i| < **R**, i from 1 to **K**

0 ≤ **C**\ |i| < **C**, i from 1 to **K**

.. |j| raw:: html

    <b><sub>j</sub></b>

Small dataset
-------------
1 ≤ **R** ≤ 10.

1 ≤ **C** ≤ 10.

0 ≤ **K** ≤ 10.

Large dataset
-------------
1 ≤ **R** ≤ 3000.

1 ≤ **C** ≤ 3000.

0 ≤ **K** ≤ 3000.

Sample
------

::

    Input       Output
    
    2           Case #1: 10
    3 3 1       Case #2: 51
    2 1
    4 11 12
    0 1
    0 3
    0 4
    0 10
    1 0
    1 9
    2 0
    2 4
    2 9
    2 10
    3 4
    3 10

The grid of sample case #1 is:

| ``0 0 0``
| ``0 0 0``
``0 1 0``

Here, 0 represents a cell with no monster, and 1 represents a cell with a
monster. It has 10 safe squares: 8 1x1 and 2 2x2.

The grid of sample case #2 is:

| ``0 1 0 1 1 0 0 0 0 0 1``
| ``1 0 0 0 0 0 0 0 0 1 0``
| ``1 0 0 0 1 0 0 0 0 1 1``
``0 0 0 0 1 0 0 0 0 0 1``

Note that sample case #2 will only appear in the Large dataset.
It has 51 safe squares: 32 1x1, 13 2x2, 5 3x3, and 1 4x4.
