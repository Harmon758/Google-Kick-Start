Analysis
--------
As per the given definition of operation, Ada can only change the goodness
score by one in a single move. Therefore to get a string with the required
goodness score in the minimum number of operations Ada can either increase or
decrease the goodness score by one in each step. Let us assume there are *X*
indices(≤ **N**\ /2 (1-indexed)) *i* in the given string **S** such that
|Si| ≠ |SN−i+1|. We have 3 cases now.

.. |Si| raw:: html

    <b>S<sub>i</sub></b>

.. |SN−i+1| raw:: html

    <b>S<sub>N-<i>i</i>+1</sub></b>

- | Case 1: *X* = **K**,
  In this case, Ada already has the string which has a goodness score of **K**.
  Therefore number of operations required is 0.
- | Case 2: *X* > **K**,
  In this case, Ada can change (*X* − **K**) letters at indices *i*
  (1 ≤ *i* ≤ **N**\ /2 (1-indexed)) that satisfy |Si| ≠ |SN−i+1| to the letter
  at |SN−i+1|. Then she will have a string with a goodness score of **K**.
  Therefore the minimum number of operations is (*X* − **K**).
- | Case 3: *X* < **K**,
  In this case, Ada can change (**K** − *X*) letters at indices *i*
  (1 ≤ *i* ≤ **N**\ /2 (1-indexed)) that satisfy |Si| = |SN−i+1| to any other
  uppercase letter other than the one at |SN−i+1|. As a result, she will have a
  string with a goodness score of **K**. Therefore the minimum number of
  operations is (**K** − *X*).

All the above described operations can be done in *O*\ (**N**) complexity.
Therefore the overall complexity is *O*\ (**N**).

Sample Code (C++)
^^^^^^^^^^^^^^^^^

::

    int kGoodnessString(string s, int k) {
    int minOperations = 0, x = 0;
    for(int i = 0; i < s.size() / 2; i++) {
        if(s[i] != s[s.size() - i - 1]) {
            x++;
        }
    }

    if(x == k) {
        minOperations = 0;
    }
    else if(x > k) {
        minOperations = x - k;
    }
    else {
        minOperations = k - x;
    }
    return minOperations;
    }

`Test Data <test_data>`_
