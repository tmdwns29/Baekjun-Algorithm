import java.util.Scanner;

class Solution {

    static int T, N, B, ans;
    static int[] H;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        T = input.nextInt();
        for (int t=1; t<=T; t++) {

            N = input.nextInt();
            B = input.nextInt();
            H = new int[N];
            ans = N * 10000;

            for (int i=0; i<N; i++) {
                H[i] = input.nextInt();
            }

            DFS(0, 0);
            System.out.printf("#%d %d\n", t, ans);
        }
    }

    public static void DFS(int n, int sum) {
        if (n == N) {
            if (sum >= B) {
                int D = sum - B;
                ans = Math.min(D, ans);
            }
            return;
        }

        DFS(n+1, sum);
        DFS(n+1, sum + H[n]);
    }
}