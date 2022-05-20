#### Analysis

The idea is to use brute force. You can simulate the multiplication and
division operations and stop when $\mathbf{R}$ reaches zero. As it is integer
division, it is guaranteed that after a finite number of steps, $\mathbf{R}$
will eventually become zero. At first it might look like that it will exceed
the TL, but the $2 \times \mathbf{A} \leq \mathbf{B}$ condition ensures that
the value of $\mathbf{R}$ will be halved each time a division by $\mathbf{B}$
occurs. The area of a circle with radius $\mathbf{R}$ is $\pi\mathbf{R}^{2}$
which can be calculated in $O(1)$. So, if the value of $\mathbf{R}$ is halved
with each division, it leads to a final time complexity of
$O(\log(\mathbf{R}))$.

A pseudocode would look something like this:

```
  ans = R*R
  while R > 0:
    R *= A
    ans += R*R
    R /= B
    ans += R*R
  return ans*pi
```

[Test Data](test_data)
