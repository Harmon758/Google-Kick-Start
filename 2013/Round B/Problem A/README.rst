.. _Problem A. Sudoku Checker:
    https://code.google.com/codejam/contest/2929486/dashboard#s=p0

============================
`Problem A. Sudoku Checker`_
============================

Problem
-------
**Sudoku** is a popular single player game. The objective is to fill a 9x9
matrix with digits so that each column, each row, and all 9 non-overlapping 3x3
sub-matrices contain all of the digits from 1 through 9. Each 9x9 matrix is
partially completed at the start of game play [sic] and typically has a unique
solution.

.. image:: https://code.google.com/codejam/contest/images/?image=xxx.png&p=5645889129414656&c=2929486

.. image:: https://code.google.com/codejam/contest/images/?image=yyy.png&p=5645889129414656&c=2929486

Given a completed |N2|\ x\ |N2| Sudoku matrix, your task is to determine
whether it is a *valid* solution. A *valid* solution must satisfy the following
criteria:

- Each row contains each number from **1** to |N2|, once each.
- Each column contains each number from **1** to |N2|, once each.
- Divide the |N2|\ x\ |N2| matrix into |N2| non-overlapping **N**\ x\ **N**
  sub-matrices. Each sub-matrix contains each number from **1** to |N2|, once
  each.

You don't need to worry about the uniqueness of the problem. Just check if the
given matrix is a valid solution.

.. |N2| raw:: html

    <b>N<sup>2</sup></b>

Input
-----
The first line of the input gives the number of test cases, **T**. **T** test
cases follow. Each test case starts with an integer **N**. The next |N2| lines
describe a completed Sudoku solution, with each line contains [sic] exactly
|N2| integers. All input integers are positive and less than 1000.

Output
------
For each test case, output one line containing "Case #x: y", where x is the
case number (starting from 1) and y is "Yes" (quotes for clarity only) if it is
a valid solution, or "No" (quotes for clarity only) if it is invalid. Note that
the judge is case-sensitive, so answers of "yes" and "no" will not be accepted.

Limits
------
1 ≤ **T** ≤ 100.

Small dataset
~~~~~~~~~~~~~
**N** = 3.

Large dataset
~~~~~~~~~~~~~
3 ≤ **N** ≤ 6.

Sample
------

::

    Input                   Output

    3                       Case #1: Yes
    3                       Case #2: No
    5 3 4 6 7 8 9 1 2       Case #3: No
    6 7 2 1 9 5 3 4 8
    1 9 8 3 4 2 5 6 7
    8 5 9 7 6 1 4 2 3
    4 2 6 8 5 3 7 9 1
    7 1 3 9 2 4 8 5 6
    9 6 1 5 3 7 2 8 4
    2 8 7 4 1 9 6 3 5
    3 4 5 2 8 6 1 7 9
    3
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7 8 9
    3
    5 3 4 6 7 8 9 1 2
    6 7 2 1 9 5 3 4 8
    1 9 8 3 4 2 5 6 7
    8 5 9 7 6 1 4 2 3
    4 2 6 8 999 3 7 9 1
    7 1 3 9 2 4 8 5 6
    9 6 1 5 3 7 2 8 4
    2 8 7 4 1 9 6 3 5
    3 4 5 2 8 6 1 7 9
