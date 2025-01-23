import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();
        int[] A;
        int[] B;

        for (int t=0; t<T; t++) {
            int N = input.nextInt();
            int M = input.nextInt();
            int answer = 0;
            A = new int[N];
            B = new int[M];

            for (int i=0; i<N; i++) {
                A[i] = input.nextInt();
            }
            for (int i=0; i<M; i++) {
                B[i] = input.nextInt();
            }
            Arrays.sort(B);

            for (int A_val: A) {
                int start = 0;
                int end = M-1;
                int cnt = 0;

                while (start<=end) {
                    int mid = (start+end) / 2;

                    if (B[mid] < A_val) {
                        start = mid + 1;
                        cnt = mid + 1;
                    }
                    else {
                        end = mid - 1;
                    }
                }
                answer += cnt;
            }
            System.out.println(answer);
        }
    }
}