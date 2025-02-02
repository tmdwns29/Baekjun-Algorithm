import java.util.Scanner;

class Solution {
    static int[] score, cal;
    static boolean[] sel;
    static int N, L, answer;

    static void recursive(int k) {

        // 선택 여부를 마친 상태에서 선택된 것들만 계산
        if (k == N) {
            int cal_sum = 0; // cal합이 L을 넘지 않는
            int score_sum = 0; // score합 중 가장 큰 score_합
            for (int i = 0; i < N; i++) {
                if (sel[i]) { // 선택된 것들만
                    score_sum += score[i];
                    cal_sum += cal[i];
                }
            }
            // cal_sum이 L을 넘지 않고, score_sum이 기존 값보다 큰 경우에 업데이트
            if (cal_sum <= L && answer < score_sum) {
                answer = score_sum;
            }
            return;
        }

        // 선택
        sel[k] = true;
        recursive(k+1);

        // 미선택
        sel[k] = false;
        recursive(k+1);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();

        for (int tc=1; tc<=T; tc++) {
            N = input.nextInt();
            L = input.nextInt();
            score = new int[N];
            cal = new int[N];
            sel = new boolean[N];
            answer = 0;

            for (int i=0; i<N; i++) {
                score[i] = input.nextInt();
                cal[i] = input.nextInt();
            }

            // 첫번째(0) 부터 시작, 선택여부 저장하는 배열
            recursive(0);

            System.out.printf("#%d %d\n", tc, answer);
        }
    }
}
