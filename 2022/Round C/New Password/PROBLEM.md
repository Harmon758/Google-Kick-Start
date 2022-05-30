### Problem

A company named Gooli has issued a new policy that their employees account
passwords must contain:

1. At least $7$ characters.
2. At least one uppercase English alphabet letter.
3. At least one lowercase English alphabet letter.
4. At least one digit.
5. At least one special character. There are four special characters: `#`, `@`,
   `*`, and `&`.

The company has asked all the employees to change their passwords if the above
requirements are not satisfied. Charles, an employee at Gooli, really likes his
old password. In case his old password does not satisfy the above requirements,
Charles will fix it by appending letters, digits, and special characters. Can
you help Charles to find the shortest possible new password that satisfies his
company's requirements?

### Input

The first line of the input gives the number of test cases, $\mathbf{T}$.
$\mathbf{T}$ test cases follow. Each test case consists of two lines. The first
line of each test case contains an integer $\mathbf{N}$, denoting the length of
the old password. The second line of each test case contains the old password
of length $\mathbf{N}$. Old password contains only digits, letters, and special
characters.

### Output

For each test case, output one line containing
<code>Case #<i>x</i>: <i>y</i></code>, where $x$ is the test case number
(starting from 1) and $y$ is a valid new password, obtained by possibly fixing
the old password in the way that Charles wants and satisfying the company's
requirements.

It is guaranteed that at least one solution exists. If there are multiple
solutions, you may output any one of them.

### Limits

Time limit: 20 seconds.  
Memory limit: 1 GB.  
$1 \le \mathbf{T} \le 100$.

#### Test Set 1

$7 \le \mathbf{N} \le 10^4$.  
The old password contains only digits.

#### Test Set 2

$1 \le \mathbf{N} \le 10^4$.  
The old password contains only digits, letters, and special characters.

### Sample

*Note: there are additional samples that are not run on submissions down
below.*

[Sample Input](new_password_sample_ts1_input.txt)

[Sample Output](new_password_sample_ts1_output.txt)

In Sample Case #1, the old password does not satisfy requirements $2$, $3$, and
$5$. One possible shortest new password is `1234567aA&`.

In Sample Case #2, the old password does not satisfy requirements $2$, $3$, and
$5$. One possible shortest new password is `1111234567@Rc`.

### Additional Sample - Test Set 2

*The following additional sample fits the limits of Test Set 2. It will not be
run against your submitted solutions.*

[Sample Input](new_password_sample_ts2_input.txt)

[Sample Output](new_password_sample_ts2_output.txt)

In Sample Case #1, the old password does not satisfy requirements $1$, $3$,
$4$, and $5$. One possible shortest new password is `Aa1*111`.

In Sample Case #2, the old password does not satisfy requirements $1$, $2$, and
$3$. One possible shortest new password is `1*abAA*`.

In Sample Case #3, the old password already meets all the requirements so
Charles does not have to change his password.
