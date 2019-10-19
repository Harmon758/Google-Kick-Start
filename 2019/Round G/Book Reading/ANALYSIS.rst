Analysis
--------
Test set 1
----------
We can solve this test set by naively computing the number of pages that each
lazy readers will read. We can do this by initially having an array ``torn`` of
**N** booleans, where ``torn[x]`` is true if and only if page x is torn out,
and then for each lazy reader i, we can iterate from 1 to **N**, incrementing
our answer only if the value that we iterate is a multiple of **R**\ |i| and
not torn out.

.. |i| raw:: html

    <b><sub>i</sub></b>

The running time of this solution is O(**N** × **Q**).

Test set 2
----------
Let f(x) be the number of pages that are multiples of x and not torn out. To
compute f(x), we can only check [sic] whether the pages x, 2x, 3x, ...,
floor(**N**/x)x are torn out. Therefore, we can do this in **N**/x time.

This means that we can compute f(1), f(2), ..., f(**N**) in a total of
**N**\ (1/1 + 1/2 + ... + 1/**N**) time. 1/1 + 1/2 + ... + 1/**N** is
approximately O(log **N**) (since the n-th `harmonic number`_ is approximately
O(log **N**)), so in total [sic] f(1), f(2), ..., f(**N**) can be computed in a
total of O(**N** log **N**) time.

.. _harmonic number: https://en.wikipedia.org/wiki/Harmonic_number

After precomputing f(x), we can easily count the number of pages that each lazy
readers [sic] will read in O(1). The running time of this solution is
O(**N** log **N** + **Q**).
