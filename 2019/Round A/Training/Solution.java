import java.util.*;

public class Solution {
    public static String solve(Scanner scanner) {
        int N = scanner.nextInt();
        int P = scanner.nextInt();

        int[] S = new int[N];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            S[i] = scanner.nextInt();
            map.put(S[i], map.getOrDefault(S[i], 0) + 1);
        }
        Arrays.sort(S);

        for (int i = 0; i < N; i++) if (map.get(S[i]) >= P) return "0";

        long ans = Long.MAX_VALUE;
        long sum = 0;

        for (int i = 0; i < P - 1; i++) sum += S[i];

        for (int i = P - 1; i < N; i++) {
            sum += S[i];
            long tmp_ans = P * S[i] - sum;
            ans = Math.min(tmp_ans, ans);
            sum -= S[i-P+1];
        }

        return String.valueOf(ans);
    }

    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int caseNum = input.nextInt();
        for (int ks = 1; ks <= caseNum; ks++) {
            System.out.println(String.format("Case #%d: %s", ks, solve(input)));
        }
    }
}