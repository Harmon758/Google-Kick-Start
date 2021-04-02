Problem
-------
Alex and Bob are brothers and they both enjoy reading very much. They have
widely different tastes on [sic] books so they keep their own books separately
[sic]. However, their father thinks it is good to promote exchanges if they can
put their books together. Thus he has bought an [sic] one-row bookshelf for
them today and put all his sons' books on it in random order. He labeled each
position of the bookshelf the owner of the corresponding book ('Alex' or
'Bob'). [sic]

Unfortunately, Alex and Bob went outside and didn't know what their father did.
When they were back, they came to realize the problem: they usually
arranged their books in their own orders, but the books seem to be in a great
mess on the bookshelf now. [sic] They have to sort them right now!!

Each book has its own *worth*, which is represented by an integer. Books with
odd values of worth belong to Alex and [sic] the books with even values of
worth belong to Bob. Alex has a habit of sorting his books from the left to the
right in an increasing order of worths, while Bob prefers to sort his books
from the left to the right in a decreasing order of worths.

At the same time, they do not want to change the positions of the labels, so
that after they have finished sorting the books according their rules [sic],
each book's owner's name should match with the label in its position.

Here comes the problem. A sequence of **N** values **s**\ |0|, **s**\ |1|, ...,
**s**\ |N-1| is given, which indicates the worths of the books from the left to
the right on the bookshelf currently. Please help the brothers to find out the
sequence of worths after sorting such that it satisfies the above description.
[sic]

.. |0| raw:: html

    <b><sub>0</sub></b>

.. |1| raw:: html

    <b><sub>1</sub></b>

.. |N-1| raw:: html

    <b><sub>N-1</sub></b>

Input
-----
The first line of input contains a single integer **T**, the number of test
cases. Each test case starts with a line containing an integer **N**, the
number of books on the bookshelf. The next line contains **N** integers
separated by spaces, representing **s** \ |0|, **s**\ |1|, ..., **s**\ |N-1|,
which are the worths of the books.

Output
------
For each test case, output one line containing "Case #\ **X**: ", followed by
**t**\ |0|, **t**\ |1|, ..., **t**\ |N-1| in order, and separated by spaces.
**X** is the test case number (starting from 1) and **t**\ |0|, **t**\ |1|,
..., **t**\ |N-1| forms the resulting sequence of worths of the books from the
left to the right.

Limits
------
| Time limit: 30 seconds per test set.
| Memory limit: 1GB.
| 1 ≤ **T** ≤ 30.

Test set 1 - Visible [sic]
~~~~~~~~~~~~~~~~~~~~~~~~~~
| 1 ≤ **N** ≤ 100
| -100 ≤ **s**\ |i| ≤ 100

Test set 2 - Hidden [sic]
~~~~~~~~~~~~~~~~~~~~~~~~~
| 1 ≤ **N** ≤ 1000
| -1000 ≤ **s**\ |i| ≤ 1000

.. |i| raw:: html

    <b><sub>i</sub></b>

Sample
------

::

    Input                   Output

    2
    5
    5 2 4 3 1               Case #1: 1 4 2 3 5
    7                       Case #2: -5 88 11 20 2 -12 87
    -5 -12 87 2 88 20 11
