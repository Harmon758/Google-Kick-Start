.. _Problem B. Super 2048:
    https://code.google.com/codejam/contest/3214486/dashboard#s=p1

========================
`Problem B. Super 2048`_
========================

Problem
-------
2048 is a famous single-player game in which the objective is to slide tiles
on a grid to combine them and create a tile with the number 2048.

2048 is played on a simple 4 x 4 grid with tiles that slide smoothly when a
player moves them. For each movement, the player can choose to move all tiles
in 4 directions, left, right, up, and down, as far as possible at the same
time. If two tiles of the same number collide while moving, they will merge
into a tile with the total value of the two tiles that collided. **In one
movement, one newly created tile can not be merged again and always is merged
with the tile next to it along the moving direction first.** E.g. if the three
"2" are in a row "2 2 2" and the player choose to move left, it will become
"4 2 0", the most left 2 "2" are merged.

.. image:: https://code.google.com/codejam/contest/images/?image=2048.png&p=5742336445251584&c=3214486

The above figure shows how 4 x 4 grid varies when player moves all tiles
'right'.

Alice and Bob accidentally find this game and love the feel when two tiles are
merged. After a few round [sic], they start to be bored about the size of the
board and decide to extend the size of board to **N** x **N**, which they
called [sic] the game "Super 2048".

The big board then makes them dazzled (no zuo no die -_-| ). They ask you to
write a program to help them figure out what the board will be looked [sic]
like after all tiles move to one specific direction on a given board.

Input
-----
The first line of the input gives the number of test cases, **T**.
**T** test cases follow. The first line of each test case gives the side
length of the board, **N**, and the direction the tiles will move to, **DIR**.
**N** and **DIR** are separated by a single space.
**DIR** will be one of four strings: "left", "right", "up", or "down".

The next **N** lines each contain **N** space-separated integers describing
the original state of the board. Each line represents a row of the board
(from top to bottom); each integer represents the value of a tile
(or 0 if there is no number at that position).

Output
------
For each test case, output one line containing "Case #x:",
where x is the test case number (starting from 1).
Then output **N** more lines, each containing **N** space-separated integers
which describe the board after the move in the same format as the input.

Limits
------
Each number in the grid is either 0 or a power of two between 2 and 1024,
inclusive.

Small dataset
-------------
| 1 ≤ **T** ≤ 20
| 1 ≤ **N** ≤ 4

Large dataset
-------------
| 1 ≤ **T** ≤ 100
| 1 ≤ **N** ≤ 20

Sample
------

::

    Input                   Output
    
    3                       Case #1:
    4 right                 0 0 4 4
    2 0 2 4                 0 2 4 2
    2 0 4 2                 0 4 4 8
    2 2 4 8                 0 0 4 8
    2 2 4 4                 Case #2:
    10 up                   4 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     4 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     4 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     4 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     4 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     0 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     0 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     0 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     0 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     0 0 0 0 0 0 0 0 0 0
    2 0 0 0 0 0 0 0 0 0     Case #3:
    3 right                 0 2 4
    2 2 2                   0 4 8
    4 4 4                   0 8 16
    8 8 8
