import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        int tc = 0;
        while(T-- > 0) {
            tc++;
            int ans = 0;
            int N = scan.nextInt();
            int Q = scan.nextInt();
            String S = scan.next();

            int[][] prefixSum = new int[N][26];
            for(int i=0; i<N; i++) {
                if(i>0) {
                    for(int j=0; j<26; j++) {
                        prefixSum[i][j] = prefixSum[i-1][j];
                    }
                }
                prefixSum[i][S.charAt(i) - 'A']++;
            }

            int[][] query = new int[Q][2];
            for(int i=0; i<Q; i++) {
                int[] diff = new int[26];
                for(int j=0; j<2; j++) {
                    query[i][j] = scan.nextInt();
                }

                int L = query[i][0]-1;
                int R = query[i][1]-1;
                if(L > 0) {
                    for(int k=0; k<26; k++) {
                        diff[k] -= prefixSum[L-1][k];
                    }
                }
                for(int k=0; k<26; k++) {
                    diff[k] += prefixSum[R][k];
                }
                
                int count = 0;
                for(int num: diff) {
                    if(num%2!=0) {
                        count++;
                    }
                }

                if(count < 2) {
                    ans++;
                }
            }
            System.out.println("Case #" + tc + ": " + ans);
        }
        scan.close();
    }
}