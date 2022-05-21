### Problem

Li has planned a bike tour through the mountains of Switzerland. His tour
consists of **N** checkpoints, numbered from 1 to **N** in the order he will
visit them. The i-th checkpoint has a height of <b>H<sub>i</sub></b>.

A checkpoint is a *peak* if:

- It is not the 1st checkpoint or the **N**-th checkpoint, and
- The height of the checkpoint is *strictly greater than* the checkpoint
  immediately before it and the checkpoint immediately after it.

Please help Li find out the number of peaks.

### Input

The first line of the input gives the number of test cases, **T**. **T** test
cases follow. Each test case begins with a line containing the integer **N**.
The second line contains **N** integers. The i-th integer is
<b>H<sub>i</sub></b>.

### Output

For each test case, output one line containing `Case #x: y`, where `x` is the
test case number (starting from 1) and `y` is the number of peaks in Li's bike
tour.

### Limits

Time limit: 10 seconds.  
Memory limit: 1 GB.  
1 ≤ **T** ≤ 100.  
1 ≤ <b>H<sub>i</sub></b> ≤ 100.

#### Test Set 1

3 ≤ **N** ≤ 5.

#### Test Set 2

3 ≤ **N** ≤ 100.

### Sample

[Sample Input](bike_tour_sample_ts1_input.txt)

[Sample Output](bike_tour_sample_ts1_output.txt)

- In sample case #1, the 2nd checkpoint is a peak.
- In sample case #2, there are no peaks.
- In sample case #3, the 2nd and 4th checkpoint are peaks.
- In sample case #4, there are no peaks.
