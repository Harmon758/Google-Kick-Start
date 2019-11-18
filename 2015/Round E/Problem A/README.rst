.. _Problem A. Lazy Spelling Bee:
    https://code.google.com/codejam/contest/8264486/dashboard#s=p0

===============================
`Problem A. Lazy Spelling Bee`_
===============================

Problem
-------
In the Lazy Spelling Bee, a contestant is given a target word W to spell. The
contestant's answer word A is acceptable if it is the same length as the target
word, and the i-th letter of A is either the i-th, (i-1)th, or (i+1)th letter
of W, for all i in the range of the length of A. (The first letter of A must
match either the first or second letter of W, since the 0th letter of W doesn't
exist. Similarly, the last letter of A must match either the last or
next-to-last letter of W.) Note that the target word itself is always an
acceptable answer word.

You are preparing a Lazy Spelling Bee, and you have been asked to determine,
for each target word, how many distinct acceptable answer words there are.
Since this number may be very large, please output it modulo 1000000007
(|10^9| + 7).

.. |10^9| replace:: 10\ :sup:`9`

Input
-----
The first line of the input gives the number of test cases, **T**. **T** test
cases follow; each consists of one line with a string consisting only of
lowercase English letters (``a`` through ``z``).

Output
------
For each test case, output one line containing "Case #x: y", where x is the
test case number (starting from 1) and y is the number of distinct acceptable
answer words, modulo |10^9| + 7.

Limits
------
1 ≤ **T** ≤ 100.

Small dataset
-------------
1 ≤ length of each string ≤ 5.

Large dataset
-------------
1 ≤ length of each string ≤ 1000.

Sample
------

::

    Input   Output
    
    4       Case #1: 4
    ag      Case #2: 1
    aa      Case #3: 108
    abcde   Case #4: 1
    x

In sample case #1, the acceptable answer words are ``aa``, ``ag``, ``ga``, and
``gg``.

In sample case #2, the only acceptable answer word is ``aa``.
