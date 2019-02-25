.. _Problem B. Mural:
    https://codejam.withgoogle.com/codejam/contest/3324486/dashboard#s=p1

===================
`Problem B. Mural`_
===================

Problem
-------
Thanh wants to paint a wonderful mural on a wall that is **N** sections long.
Each section of the wall has a *beauty score*, which indicates how beautiful
it will look if it is painted. Unfortunately, the wall is starting to crumble
due to a recent flood, so he will need to work fast!

At the beginning of each day, Thanh will paint one of the sections of the
wall. On the first day, he is free to paint any section he likes. On each
subsequent day, he must paint a new section that is next to a section he has
already painted, since he does not want to split up the mural.

At the end of each day, one section of the wall will be destroyed.
It is always a section of wall that is adjacent to only one other section and
is unpainted (Thanh is using a waterproof paint, so painted sections can't be
destroyed).

The *total beauty* of Thanh's mural will be equal to the sum of the beauty
scores of the sections he has painted. Thanh would like to guarantee that,
no matter how the wall is destroyed, he can still achieve a total beauty of
at least B.
What's the maximum value of B for which he can make this guarantee?

Input
-----
The first line of the input gives the number of test cases, **T**.
**T** test cases follow.
Each test case starts with a line containing an integer **N**.
Then, another line follows containing a string of **N** digits from 0 to 9.
The i-th digit represents the beauty score of the i-th section of the wall.

Output
------
For each test case, output one line containing ``Case #x: y``,
where ``x`` is the test case number (starting from 1) and ``y`` is
the maximum beauty score that Thanh can guarantee that he can achieve,
as described above.

Limits
------
1 ≤ **T** ≤ 100.

Small dataset
-------------
2 ≤ **N** ≤ 100.

Large dataset
-------------
For exactly 1 case, **N** = 5 × 10\ :sup:`6`;
for the other **T** - 1 cases, 2 ≤ **N** ≤ 100.

Sample
------

::

    Input       Output
    
    4           Case #1: 6
    4           Case #2: 14
    1332        Case #3: 7
    4           Case #4: 31
    9583
    3
    616
    10
    1029384756

In the first sample case, Thanh can get a total beauty of 6, no matter how
the wall is destroyed. On the first day, he can paint either section of wall
with beauty score 3. At the end of the day, either the 1st section or
the 4th section will be destroyed, but it does not matter which one.
On the second day, he can paint the other section with beauty score 3.

In the second sample case, Thanh can get a total beauty of 14,
by painting the leftmost section of wall (with beauty score 9).
The only section of wall that can be destroyed is the rightmost one,
since the leftmost one is painted. On the second day,
he can paint the second leftmost section with beauty score 5.
Then the last unpainted section of wall on the right is destroyed.
Note that on the second day, Thanh cannot choose to paint the third section of
wall (with beauty score 8), since it is not adjacent to any other painted
sections.

In the third sample case, Thanh can get a total beauty of 7.
He begins by painting the section in the middle (with beauty score 1).
Whichever section is destroyed at the end of the day,
he can paint the remaining wall at the start of the second day.
