Analysis
--------
For simplicity, let us use *L* to represent the number of digits in **N**, note
the scale of *L* is actually *O*\(*log*\ :sub:`10`\ **N**). And let us use
{|aL−1|,\ |aL−2|,…,\ *a*\ :sub:`1`,\ *a*\ :sub:`0`} to represent the digits of
**N**, where |aL−1| is the most significant digit and *a*\ :sub:`0` is the
least significant digit (0 ≤ |ai| ≤ 9 for all *i* < *L*\−1, and
1 ≤ |aL−1| ≤ 9). We can read **N** as a string, where the characters in the
string {*s*\[0],\ *s*\[1],…,\ *s*\[*L*\−2],\ *s*\[*L*\−1]} represent
{|aL−1|,\ |aL−2|,…,\ *a*\ :sub:`1`,\ *a* :sub:`0`}. Or, we can read **N** as an
integer, whose value equals
|aL−1| × |10L−1| + |aL−2| × |10L−2| + ⋯ + *a*\ :sub:`1` × 10 + *a*\ :sub:`0`.
Inserting a new digit *d* in the *k*\−th position in **N** means inserting it
after the first *L* − *k* digits (on the left side) and before the last *k*
digits (on the right side) of **N**. If **N** is string type, then the new
number can be built by slicing and concatenating the string as
*s*\[0…*L* − *k*] + *string*\(*d*) + *s*\[*L* − *k*…*L*] in linear time, where
*s*\[*i*…*j*] means characters of string *s* from index *i* to index *j*. On
the other hand, if **N** is integer type, then the new number can be calculated
as (**N**\−\ **N**\%\ |10k|) × 10 + *d* × |10k| + (**N**\%\ |10k|) in constant
time.

.. |aL−1| raw:: html

    <i>a</i><sub><i>L</i>−1</sub>

.. |aL−2| raw:: html

    <i>a</i><sub><i>L</i>−2</sub>

.. |ai| raw:: html

    <i>a</i><sub><i>i</i></sub>

.. |10L−1| raw:: html

    10<sup><i>L</i>−1</sup>

.. |10L−2| raw:: html

    10<sup><i>L</i>−2</sup>

.. |10k| raw:: html

    10<sup><i>k</i></sup>

Test Set 1
----------
Since **N** ≤ 10\ :sup:`5`, the number of digits of **N** is at most 6, which
means there are at most 7 positions to insert a new digit. As for the new
digit, there are at most 10 options (``0`` … ``9``), therefore the total number
of results is at most 70. We can enumerate all these 70 results, eliminate
those ones which are not multiples of 9 or have leading zeros, then find the
smallest one from them.

In this solution, there are *O*\(*L*) positions to insert a new digit, and a
constant number of choices for the new digit (``0`` … ``9``). If **N** is read
as an integer, then we need constant time to insert a new digit, decide if the
inserted result is a multiple of 9 and compare the candidates, so the time
complexity of this solution is *O*\(*L*). If **N** is read as a string, then
every operation such as the insertion of a new digit or value comparison among
candidates will take *O*\(*L*) time, so the time complexity will be
*O*\(*L*\ :sup:`2`).

Test Set 2
----------
Now that **N** is at most 10\ :sup:`123456`, we cannot read **N** as
32-bit/64-bit integer [sic]. Instead, we should read **N** as string [sic]
where each character represents a digit of **N**. Since *L* is at most
123456 + 1, the brute force enumeration method with time complexity
*O*\(*L*\ :sup:`2`) is unacceptable. We need a more efficient algorithm.

First, let us decide which digit to insert. In fact, a number is a multiple of
9 if and only if the sum of its all digits is a multiple of 9. Therefore, we
can add up all the *L* digits of the given **N**, and use 9 − (*sum mod* 9) to
get the new digit we want. Wherever we insert it, the sum of all digits of the
new number and the new number itself will be a multiple of 9. Note that when
*sum mod* 9 = 0, adding either a new 0 or a new 9 can make the result be a
multiple of 9, but 0 is always more preferable than 9 because we are looking
for the smallest answer.

Secondly, let us decide where to insert the new digit. Let us use *d* to
represent the new digit we are going to insert. We can start from the most
significant digit |aL−1|, then |aL−2|, and then use this order to visit all the
digits in **N**, to find the first digit in **N** that is larger than *d*. Then
we should insert *d* right before this digit. In other words, say |ak| is the
first digit in **N** that is larger than *d* (i.e.
|ai| ≤ *d* for all *k* + 1 ≤ *i* ≤ *L* − 1), then the new number we are going
to make is {|aL−1|,\ |aL−2|,…,\ |ak+1|,\ *d*,\ |ak|,…,\ *a*\ :sub:`0`}, whose
value equals to
|Ng| = |aL−1| × |10L| + |aL−2| × |10L−1| + ⋯ + |ak+1| × |10k+2| + *d* ×
|10k+1| + |ak| × |10k| + ⋯ + *a*\ :sub:`0`.

.. |ak| raw:: html

    <i>a</i><sub><i>k</i></sub>

.. |ak+1| raw:: html

    <i>a</i><sub><i>k</i>+1</sub>

.. |Ng| raw:: html

    <i>N</i><sub><i>g</i></sub>

.. |10L| raw:: html

    10<sup><i>L</i></sup>

.. |10k+2| raw:: html

    10<sup><i>k</i>+2</sup>

.. |10k+1| raw:: html

    10<sup><i>k</i>+1</sup>

Is this always the best choice? Yes, let us prove it. If we insert *d* to a
more significant position, i.e. between |aq+1| and |aq| where *q* > *k*, then
the new number we are going to make is
{|aL−1|,\ |aL−2|,…,\ |aq+1|,\ *d*,\ |aq|,…,\ |ak|,…,\ *a*\ :sub:`0`} with value
|No| = |aL−1| × |10L| + |aL−2| × |10L−1| + ⋯ + |aq+1| × |10q+2| + *d* ×
|10q+1| + |aq| × |10q| + ⋯ |ak| × |10k| + ⋯ + *a*\ :sub:`0`. The difference
between this solution and the solution we claimed is
|No| − |Ng| = *d* × |10q+1| − 9 × (|aq| × |10q| + |aq−1| × |10q−1| + ⋯ +
|ak+2| × |10k+2| + |ak+1| × |10k+1|) − d × |10k+1|. Since we have that |aq| is
always no greater than *d*, we can make sure that
9 × (|aq| × |10q| + |aq−1| × |10q−1| + ⋯ + |ak+2| × |10k+2| + |ak+1| ×
|10k+1|) + *d* × |10k+1| is always no greater than *d* × |10q+1|. Therefore, no
matter what other position *q* we choose to insert *d*, the result is always no
less than inserting at *k*.

.. |aq+1| raw:: html

    <i>a</i><sub><i>q</i>+1</sub>

.. |aq| raw:: html

    <i>a</i><sub><i>q</i></sub>

.. |No| raw:: html

    <i>N</i><sub><i>o</i></sub>

.. |10q+2| raw:: html

    10<sup><i>q</i>+2</sup>

.. |10q+1| raw:: html

    10<sup><i>q</i>+1</sup>

.. |10q| raw:: html

    10<sup><i>q</i></sup>

.. |aq−1| raw:: html

    <i>a</i><sub><i>q</i>-1</sub>

.. |10q−1| raw:: html

    10<sup><i>q</i>-1</sup>

.. |ak+2| raw:: html

    <i>a</i><sub><i>k</i>+2</sub>

On the other hand, if we insert *d* to a less significant position, i.e.
between |ap+1| and |ap| where *p* < *k*, then the new number we are going to
make is {|aL−1|,\ |aL−2|,…,\ |ak|,…,\ |ap+1|,\ *d*,\ |ap|,…,\ *a*\ :sub:`0`}
with value
|No| = |aL−1| × |10L| + |aL−2| × |10L−1| + ⋯ + |ak| × |10k+1| + ⋯ + |ap+1| ×
|10p+2| + *d* × |10p+1| + |ap| × |10p| + ⋯ + *a*\ :sub:`0`. The difference
between this solution and the solution we claimed is
|No| − |Ng| = −\ *d* × |10k+1| + 9 × (|ak| × |10k| + ⋯ + |ap+1| ×
|10p+1|) + *d* × |10p+1|. Since we have that |ak| > *d*, we can make sure that
9 × (|ak| × |10k| + ⋯ + |ap+1| × |10p+1|) + *d* × |10p+1| is always greater
than *d* × |10k+1|. Therefore, no matter what other position *p* we choose to
insert *d*, the result is always greater than inserting at *k*.

.. |ap+1| raw:: html

    <i>a</i><sub><i>p</i>+1</sub>

.. |ap| raw:: html

    <i>a</i><sub><i>p</i></sub>

.. |10p+2| raw:: html

    10<sup><i>p</i>+2</sup>

.. |10p+1| raw:: html

    10<sup><i>p</i>+1</sup>

.. |10p| raw:: html

    10<sup><i>p</i></sup>

Note that there are some edge cases. For example, all digits in **N** are less
than *d*. In this case, we should append *d* to the end of **N**. And if *d* is
0, we will find that the first digit in **N** that is larger than *d* is the
leading digit. Be careful that we should not put *d* before it because the
result cannot have leading zeros. In this case, we should put 0 right after the
leading digit of **N** to get the smallest result.

The time complexity for finding out which *d* to insert is *O*\(*L*) because we
need to add up all digits of **N** to get the remainder of **N** divided by 9.
Then to find where to insert *d*, we also need *O*\(*L*) time to visit all the
digits to find the first digit that is larger than *d* (or find out all the
digits are no larger than *d*). Therefore, the total time complexity of this
solution is *O*\(*L* + *L*) = *O*\(*L*).

`Test Data <test_data>`_
