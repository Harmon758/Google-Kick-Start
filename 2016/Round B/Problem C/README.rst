.. _Problem C. Watson and Intervals:
    https://code.google.com/codejam/contest/5254487/dashboard#s=p2

==================================
`Problem C. Watson and Intervals`_
==================================

Problem
-------
Sherlock and Watson have mastered the intricacies of the language C++ in their
programming course, so they have moved on to algorithmic problems. In today's
class, the tutor introduced the problem of merging one-dimensional intervals.
**N** intervals are given, and the ``i``\ th interval is defined by the
inclusive endpoints [**L**\ |i|\ **, R**\ |i|], where **L**\ |i| **≤ R**\ |i|.

.. |i| raw:: html

    <b><sub>i</sub></b>

The tutor defined the *covered area* of a set of intervals as the number of
integers appearing in at least one of the intervals. (Formally, an integer p
contributes to the covered area if there is some j such that
**L**\ |j| ≤ ``p`` ≤ **R**\ |j|.)

.. |j| raw:: html

    <b><sub>j</sub></b>

Now, Watson always likes to challenge Sherlock. He has asked Sherlock to
remove exactly one interval such that the covered area of the remaining
intervals is minimized. Help Sherlock find this minimum possible covered area,
after removing exactly one of the **N** intervals.

Input
-----
Each test case consists of one line with eight integers **N**,
**L**\ |1|\ **, R**\ |1|, **A**, **B**, **C**\ |1|, **C**\ |2|, and **M**.
**N** is the number of intervals, and the other seven values are parameters
that you should use to generate the other intervals, as follows:

.. |1| raw:: html

    <b><sub>1</sub></b>

.. |2| raw:: html

    <b><sub>2</sub></b>

First define |x_1| = **L**\ |1| and |y_1| = **R**\ |1|.
Then, use the recurrences below to generate |x_i, y_i| for
``i`` = 2 to **N**:

.. |x_1| raw:: html

    <code>x<sub>1</sub></code>

.. |y_1| raw:: html

    <code>y<sub>1</sub></code>

.. |x_i, y_i| raw:: html

    <code>x<sub>i</sub>, y<sub>i</sub></code>

- |x_i| = ( **A**\*\ |x_i-1| + **B**\*\ |y_i-1| + **C**\ |1| ) modulo **M**.
- |y_i| = ( **A**\*\ |y_i-1| + **B**\*\ |x_i-1| + **C**\ |2| ) modulo **M**.

.. |x_i| raw:: html

    <code>x<sub>i</sub></code>

.. |y_i| raw:: html

    <code>y<sub>i</sub></code>

.. |x_i-1| raw:: html

    <code>x<sub>i-1</sub></code>

.. |y_i-1| raw:: html

    <code>y<sub>i-1</sub></code>

We define **L**\ |i| = |min(x_i, y_i)| and **R**\ |i| = |max(x_i, y_i)|,
for all ``i`` = 2 to **N**.

.. |min(x_i, y_i)| raw:: html

    <code>min(x<sub>i</sub>, y<sub>i</sub>)</code>

.. |max(x_i, y_i)| raw:: html

    <code>max(x<sub>i</sub>, y<sub>i</sub>)</code>

Output
------
For each test case, output one line containing ``Case #x: y``, where ``x`` is
the test case number (starting from 1) and ``y`` is the minimum possible
covered area of all of the intervals remaining after removing exactly one
interval.

Limits
------
| 1 ≤ **T** ≤ 50.
| 0 ≤ **L**\ |1| ≤ **R**\ |1| ≤ |10^9|.
| 0 ≤ **A** ≤ |10^9|.
| 0 ≤ **B** ≤ |10^9|.
| 0 ≤ **C**\ |1| ≤ |10^9|.
| 0 ≤ **C**\ |2| ≤ |10^9|.
| 1 ≤ **M** ≤ |10^9|.

.. |10^9| replace:: 10\ :sup:`9`

Small dataset
-------------
1 ≤ **N** ≤ 1000.

Large dataset
-------------
1 ≤ **N** ≤ 5 * 10\ :sup:`5`\ (500000).

Sample
------

::

    Input               Output
    
    3                   Case #1: 0
    1 1 1 1 1 1 1 1     Case #2: 4
    3 2 5 1 2 3 4 10    Case #3: 9
    4 3 4 3 3 8 10 10

In case 1, using the generation method, the set of intervals generated are:
{[1, 1]}. Removing the only interval, the covered area is 0.

In case 2, using the generation method, the set of intervals generated are:
{[2, 5], [3, 5], [4, 7]}. Removing the first, second or third interval would
cause the covered area of remaining intervals to be 5, 6 and 4, respectively.

In case 3, using the generation method, the set of intervals generated are:
{[3, 4], [1, 9], [0, 8], [2, 4]}. Removing the first, second, third or fourth
interval would cause the covered area of remaining intervals to be
10, 9, 9 and 10, respectively.
