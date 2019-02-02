.. _Problem D. Cut Tiles:
    https://code.google.com/codejam/contest/3214486/dashboard#s=p3

=======================
`Problem D. Cut Tiles`_
=======================

Problem
-------
Enzo is doing renovation for his new house.
The most difficult part is to buy exactly the right number of tiles.
He wants **N** tiles of different sizes.
Of course they have to be cut from the tiles he bought.
All the required tiles are square.
The lengths of side of the tiles are |2S1|, |2S2|, ..., |2SN|.
He can only buy a lot of tiles sized **M**\*\ **M**,
and he decides to only cut tiles parallel to their sides for convenience.
How many tiles does he need to buy?

.. |2S1| raw:: html

    <b>2<sup>S<sub>1</sub></sup></b>

.. |2S2| raw:: html

    <b>2<sup>S<sub>2</sub></sup></b>

.. |2SN| raw:: html

    <b>2<sup>S<sub>N</sub></sup></b>

Input
-----
The first line of the input gives the number of test cases: **T**.
**T** lines follow.
Each line start with the number **N** and **M**, indicating
the number of required tiles and the size of the big tiles Enzo can buy.
**N** numbers follow:
|S1|, |S2|, ... |SN|, showing the sizes of the required tiles.

.. |S1| raw:: html

    <b>S<sub>1</sub></b>

.. |S2| raw:: html

    <b>S<sub>2</sub></b>

.. |SN| raw:: html

    <b>S<sub>N</sub></b>

Output
------
For each test case, output one line containing "Case #x: y",
where x is the test case number (starting from 1)
and y is the number of the big tiles Enzo need [sic] to buy.

Limits
------
1 ≤ |2Sk| ≤ **M** ≤ 2^31-1.

.. |2Sk| raw:: html

    <b>2<sup>S<sub>k</sub></sup></b>

Small dataset
-------------
| 1 ≤ **T** ≤ 100.
| 1 ≤ **N** ≤ 20.

Large dataset
-------------
| 1 ≤ **T** ≤ 1000.
| 1 ≤ **N** ≤ 500.

Sample
------

::

    Input                   Output
    
    4                       Case #1: 1
    1 6 2                   Case #2: 2
    2 6 2 2                 Case #3: 1
    3 6 2 1 1               Case #4: 2
    7 277 3 8 2 6 1 3 6
