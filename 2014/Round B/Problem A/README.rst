.. _Problem A. Password Attacker:
    https://code.google.com/codejam/contest/4214486/dashboard#s=p0

===============================
`Problem A. Password Attacker`_
===============================

Problem
-------
Passwords are widely used in our lives: for ATMs, online forum logins, mobile
device unlock and door access. Everyone cares about password security. However,
attackers always find ways to steal our passwords. Here is one possible
situation:

Assume that Eve, the attacker, wants to steal a password from the victim Alice.
Eve cleans up the keyboard beforehand. After Alice types the password and
leaves, Eve collects the fingerprints on the keyboard. Now she knows which keys
are used in the password. However, Eve won't know how many times each key has
been pressed or the order of the keystroke sequence.

To simplify the problem, let's assume that Eve finds Alice's fingerprints only
occurs on **M** keys. And she knows, by another method, that Alice's password
contains **N** characters. Furthermore, every keystroke on the keyboard only
generates a single, unique character. Also, Alice won't press other irrelevant
keys like 'left', 'home', 'backspace' and etc [sic].

Here's an example. Assume that Eve finds Alice's fingerprints on **M**\ =3 key
[sic] '3', '7' and '5', and she knows that Alice's password is **N**\ =4-digit
[sic] in length. So all the following passwords are possible: 3577, 3557, 7353
and 5735. (And, in fact, there are 32 more possible passwords.)

However, these passwords are not possible::

    1357  // There is no fingerprint on key '1'
    3355  // There is fingerprint [sic] on key '7',
             so '7' must occur at least once.
    357   // Eve knows the password must be a 4-digit number.

With the information, please count that [sic] how many possible passwords
satisfy the statements above. Since the result could be large, please output
the answer modulo 1000000007(10\ :sup:`9`\ +7).

Input
-----
| The first line of the input gives the number of test cases, **T**.
| For the next **T** lines, each contains two space-separated numbers **M** and
  **N**, indicating a test case.

Output
------
For each test case, output one line containing "Case #x: y", where x is the
test case number (starting from 1) and y is the total number of possible
passwords modulo 1000000007(10\ :sup:`9`\ +7).

Limits
------

Small dataset
~~~~~~~~~~~~~
| **T** = 15.
| 1 ≤ **M** ≤ **N** ≤ 7.

Large dataset
~~~~~~~~~~~~~
| **T** = 100.
| 1 ≤ **M** ≤ **N** ≤ 100.

Sample
------

::

    Input   Output
    
    4       Case #1: 1
    1 1     Case #2: 36
    3 4     Case #3: 120
    5 5     Case #4: 674358851
    15 15
