.. _Problem A. Read Phone Number:
    https://code.google.com/codejam/contest/2924486/dashboard#s=p0

===============================
`Problem A. Read Phone Number`_
===============================

Problem
-------
Do you know how to read the phone numbers in English? Now let me tell you.

For example, In [sic] China, the phone numbers are 11 digits, like:
15012233444. Someone divides the numbers into 3-4-4 format, i.e. 150 1223 3444.
While someone divides the numbers into 3-3-5 format, i.e. 150 122 33444.
Different formats lead to different ways to read these numbers:

150 1223 3444 reads one five zero one double two three three triple four.

150 122 33444 reads one five zero one double two double three triple four.

Here comes the problem:

Given a list of phone numbers and the dividing formats, output the right ways
to read these numbers.

Rules:

Single numbers just read them separately.

2 successive numbers use double.

3 successive numbers use triple.

4 successive numbers use quadruple.

5 successive numbers use quintuple.

6 successive numbers use sextuple.

7 successive numbers use septuple.

8 successive numbers use octuple.

9 successive numbers use nonuple.

10 successive numbers use decuple.

More than 10 successive numbers read them all separately.

Input
-----
The first line of the input gives the number of test cases, **T**. **T**
lines|test cases follow. Each line contains a phone number **N** and the
dividing format **F**, one or more positive integers separated by dashes (-),
without leading zeros and whose sum always equals the number of digits in the
phone number.

Output
------
For each test case, output one line containing "Case #x: y", where x is the
case number (starting from 1) and y is the reading sentence [sic] in English
whose words are separated by a space.

Limits
------
1 ≤ **T** ≤ 100.

Small dataset
~~~~~~~~~~~~~
1 ≤ **length of N** ≤ 10.

Large dataset
~~~~~~~~~~~~~
1 ≤ **length of N** ≤ 100.

Sample
------

|sample_start|
Input\ |newline|
3
15012233444 3-4-4
15012233444 3-3-5
12223 2-3
|hr|\ Output\ |newline|
Case #1: one five zero one double two three three triple four
Case #2: one five zero one double two double three triple four
Case #3: one two double two three\ |newline|
|sample_end|

.. |sample_start| raw:: html

    <pre>

.. |newline| raw:: html

    <br>

.. |hr| raw:: html

    <hr>

.. |sample_end| raw:: html

    </pre>
