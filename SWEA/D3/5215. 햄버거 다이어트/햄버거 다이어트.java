import java.util.Scanner;

class Solution {
    static int[] score, cal;
    static int N, L, answer;

    static void recursive(int idx, int k, boolean[] sel) {
        if (k == N) {
            int cal_sum = 0;
            int score_sum = 0;
            for (int i = 0; i < N; i++) {
                if (sel[i]) {
                    score_sum += score[i];
                    cal_sum += cal[i];
                }
            }
            if (cal_sum <= L && answer < score_sum) {
                answer = score_sum;
            }
        }
        if (idx == N || k == N) return;

        sel[k] = true;
        recursive(idx+1, k+1, sel);
        sel[k] = false;
        recursive(idx, k+1, sel);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();

        for (int tc=1; tc<=T; tc++) {
            N = input.nextInt();
            L = input.nextInt();
            score = new int[N];
            cal = new int[N];
            answer = 0;

            for (int i=0; i<N; i++) {
                score[i] = input.nextInt();
                cal[i] = input.nextInt();
            }

            recursive(0, 0, new boolean[N]);

            System.out.printf("#%d %d\n", tc, answer);
        }
    }
}