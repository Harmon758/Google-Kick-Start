.. _Problem A. Big Buttons:
    https://codejam.withgoogle.com/codejam/contest/3324486/dashboard#s=p0

=========================
`Problem A. Big Buttons`_
=========================

Problem
-------
You are a contestant on a popular new game show and are playing for the grand
prize!

There are two big buttons, a red one and a black one. You will make a sequence
of exactly **N** button presses.

There are lots of different sequences of presses you could make, but there are
**P** forbidden prefixes, each of length no greater than **N**. If you make a
sequence of presses which begins with *any* of the forbidden sequences, you
will not win the grand prize. It is fine for your sequence to contain one or
more forbidden prefixes as long as they do not appear at the start of your
sequence.

A *winning* sequence must consist of exactly **N** button presses and must not
begin with one of the forbidden prefixes. How many different winning sequences
are there?

Input
-----
The first line of the input gives the number of test cases, **T**. **T** test
cases follow. Each test case starts with a line containing two integers **N**
and **P**, as described above. Then, there are **P** more lines, each of which
contains a string of between 1 and **N** characters, inclusive, describing one
of the forbidden sequences of presses. An ``R`` represents pressing the red
button, whereas a ``B`` represents pressing the black button.

Output
------
For each test case, output one line containing ``Case #x: y``, where ``x`` is
the test case number (starting from 1) and ``y`` is the number of winning
sequences, as desribed [sic] above.

Limits
------
| 1 ≤ **T** ≤ 100.
| 1 ≤ **P** ≤ min(2\ |N|, 100).
| Each forbidden prefix is between 1 and **N** characters long, inclusive.
| No two forbidden prefixes will be the same.

.. |N| raw:: html

    <sup><b>N</b></sup>

Small dataset
-------------
1 ≤ **N** ≤ 10.

Large dataset
-------------
1 ≤ **N** ≤ 50.

Sample
------

::

    Input               Output
    
    4                   Case #1: 5
    3 2                 Case #2: 16
    BBB                 Case #3: 0
    RB                  Case #4: 1125556309458944
    5 1
    R
    4 3
    R
    B
    RBRB
    50 5
    BRBRBBBRBRRRBBB
    BRBRBRRRBRRRBRB
    BBBRBBBRBRRRBBB
    BRBRBRRRBRRRB
    BRBRBBBRBBBRB

Note that the last Sample case would not appear in the Small dataset.

In the first case, you must make a sequence of 3 presses. There are 8 possible
sequences of three presses, but some of them will cause you to lose the game.
They are listed below:

- ``RBB``. This is forbidden since it starts with the first forbidden sequence
  (``RB``).
- ``RBR``. This is forbidden since it starts with the first forbidden sequence
  (``RB``).
- ``BBB``. This is forbidden since it starts with the second forbidden sequence
  (``BBB``).

Thus, there are only 5 winning sequences.

In the second case, you must make a sequence of 5 presses. There is only one
forbidden sequence, which is ``R``. This means that the first press must be
``B``, and the next 4 presses can be either button. This gives a total of 16
different button presses.

In the third case, you must make a sequence of 4 presses. There are three
forbidden sequences, but since every possible sequence begins with either ``R``
(the first forbidden sequence) or ``B`` (the second forbidden sequence), there
are no winning sequences. So the answer is 0.
