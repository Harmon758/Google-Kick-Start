Problem
-------
Ada gives John a positive integer **N**. She challenges him to construct a new
number (without leading zeros), that is a multiple of 9, by inserting *exactly*
one digit (``0`` … ``9``) anywhere in the given number **N**. It is guaranteed
that **N** does not have any leading zeros.

As John prefers smaller numbers, he wants to construct the *smallest* such
number possible. Can you help John?

Input
-----
The first line of the input gives the number of test cases, **T**. **T** test
cases follow.

Each test case has a single line containing a positive integer **N**: the
number Ada gives John.

Output
------
For each test case, output one line containing |Case #x: y|, where *x* is the
test case number (starting from 1) and *y* is the new number constructed by
John. As mentioned earlier, *y* cannot have leading zeros.

.. |Case #x: y| raw:: html

    <code>Case #<i>x</i>: <i>y</i></code>

Limits
------
| Memory limit: 1 GB.
| 1 ≤ **T** ≤ 100.

Test Set 1
^^^^^^^^^^
| Time limit: 20 seconds.
| 1 ≤ **N** ≤ 10\ :sup:`5`.

Test Set 2
^^^^^^^^^^
| Time limit: 40 seconds.
| For at most 10 cases:
| 1 ≤ **N** ≤ 10\ :sup:`123456`.
| For the remaining cases:
| 1 ≤ **N** ≤ 10\ :sup:`5`.

Sample
------

`Sample Input <challenge_nine_sample_ts1_input.txt>`_

`Sample Output <challenge_nine_sample_ts1_output.txt>`_

In Sample Case #1, there are only two numbers that can be constructed
satisfying the divisibility constraint: 45 and 54. John chooses the smaller
number.

In Sample Case #2, 333 is the only number possible.

In Sample Case #3, there are four possible options - 212121, 122121, 121221 and
121212 - out of which the smallest number is 121212.
