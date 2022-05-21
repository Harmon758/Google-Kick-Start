#### Analysis

For each of the checkpoints, we can determine if it is a peak in O(1) time by
comparing its height to the heights of the checkpoints before and after it.

There are **N** checkpoints, so the total time complexity of this approach is
O(**N**), which is sufficient for both Test Set 1 and Test Set 2.

##### Sample Code(C++)

```C++
int countPeaks(vector<int> checkpoints) {
  int peaks = 0;
  for(int i = 1; i < checkpoints.size() - 1; i++) {
     if(checkpoints[i-1] < checkpoints[i] && checkpoints[i+1] < checkpoints[i]) {
        peaks++;
     }
  }
  return peaks;
}
```

[Test Data](test_data)
