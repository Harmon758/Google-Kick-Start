.. _Problem A. Diwali lightings:
    https://code.google.com/codejam/contest/5264487/dashboard#s=p0

==============================
`Problem A. Diwali lightings`_
==============================

Problem
-------
Diwali is the festival of lights. To celebrate it, people decorate their houses
with multi-color lights and burst crackers. Everyone loves Diwali, and so does
Pari. Pari is very fond of lights, and has transfinite powers, so she buys an
infinite number of red and blue light bulbs. As a programmer, she also loves
patterns, so she arranges her lights by infinitely repeating a given finite
pattern **S**.

For example, if **S** is ``BBRB``, the infinite sequence Pari builds would be
``BBRBBBRBBBRB...``

Blue is Pari's favorite color, so she wants to know the number of blue bulbs
between the **I**\ th bulb and **J**\ th bulb, inclusive, in the infinite
sequence she built (lights are numbered with consecutive integers starting from
1). In the sequence above, the indices would be numbered as follows::

    B  B  R  B  B  B  R  B  B  B  R  B...
    1  2  3  4  5  6  7  8  9  10 11 12

So, for example, there are 4 blue lights between the 4th and 8th positions, but
only 2 between the 10th and 12th.

Since the sequence can be very long, she wrote a program to do the count for
her. Can you do the same?

Input
-----
| The first line of the input gives the number of test cases, **T**. **T** test
  cases follow.
| First line of each test case consists of a string S, denoting the initial
  finite pattern.
| Second line of each test case consists of two space separated integers **I**
  and **J**, defined above.

Output
------
For each test case, output one line containing ``Case #x: y``, where ``x`` is
the test case number (starting from 1) and ``y`` is number of blue bulbs
between the **I**\ th bulb and **J**\ th bulb of Pari's infinite sequence,
inclusive.

Limits
------
| 1 ≤ **T** ≤ 100.
| 1 ≤ length of **S** ≤ 100.
| Each character of **S** is either uppercase ``B`` or uppercase ``R``.

Small dataset
-------------
1 ≤ **I** ≤ **J** ≤ 10\ :sup:`6`.

Large dataset
-------------
1 ≤ **I** ≤ **J** ≤ 10\ :sup:`18`.

Sample
------

::

    Input       Output
    
    3           Case #1: 4
    BBRB        Case #2: 2
    4 8         Case #3: 500000
    BBRB
    10 12
    BR
    1 1000000

Cases #1 and #2 are explained above.

In Case #3, bulbs at odd indices are always blue, and bulbs at even indices are
always red, so there are half a million blue bulbs between positions 1 and
10\ :sup:`6`.
