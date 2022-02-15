Problem
-------
Charles defines the goodness score of a string as the number of indices *i*
such that |Si| ≠ |SN−i+1| where 1 ≤ *i* ≤ **N**\ /2 (1-indexed). For example,
the string ``CABABC`` has a goodness score of 2 since |S2| ≠ |S5| and
|S3| ≠ |S4|.

.. |Si| raw:: html

    <b>S<sub>i</sub></b>

.. |SN−i+1| raw:: html

    <b>S<sub>N-<i>i</i>+1</sub></b>

.. |S2| raw:: html

    <b>S<sub>2</sub></b>

.. |S5| raw:: html

    <b>S<sub>5</sub></b>

.. |S3| raw:: html

    <b>S<sub>3</sub></b>

.. |S4| raw:: html

    <b>S<sub>4</sub></b>

Charles gave Ada a string **S** of length **N**, consisting of uppercase
letters and asked her to convert it into a string with a goodness score of
**K**. In one operation, Ada can change any character in the string to any
uppercase letter. Could you help Ada find the *minimum* number of operations
required to transform the given string into a string with goodness score equal
to **K**?

Input
-----
The first line of the input gives the number of test cases, **T**. **T** test
cases follow.

The first line of each test case contains two integers **N** and **K**. The
second line of each test case contains a string **S** of length **N**,
consisting of uppercase letters.

Output
------
For each test case, output one line containing |Case #x: y|, where *x* is the
test case number (starting from 1) and *y* is the minimum number of operations
required to transform the given string **S** into a string with goodness score
equal to **K**.

.. |Case #x: y| raw:: html

    <code>Case #<i>x</i>: <i>y</i></code>

Limits
------
| Memory limit: 1 GB.
| 1 ≤ **T** ≤ 100.
| 0 ≤ **K** ≤ **N**\ /2.

Test Set 1
^^^^^^^^^^
| Time limit: 20 seconds.
| 1 ≤ **N** ≤ 100.

Test Set 2
^^^^^^^^^^
| Time limit: 40 seconds.
| 1 ≤ **N** ≤ 2 × 10\ :sup:`5` for at most 10 test cases.
| For the remaining cases, 1 ≤ **N** ≤ 100.

Sample
------
`Sample Input <k-goodness_string_sample_ts1_input.txt>`_

`Sample Output <k-goodness_string_sample_ts1_output.txt>`_

In Sample Case #1, the given string already has a goodness score of 1.
Therefore the minimum number of operations required is 0.

In Sample Case #2, one option is to change the character at index 1 to ``B`` in
order to have a goodness score of 2. Therefore, the minimum number of
operations required is 1.
