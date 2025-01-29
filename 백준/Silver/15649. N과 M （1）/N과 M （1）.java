import java.util.Scanner;

public class Main {
    static int N, M;
    static int[] arr;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        N = input.nextInt();
        M = input.nextInt();
        arr = new int[N];

        for (int i=1; i<=N; i++) {
            arr[i-1] = i;
        }

        recursive(new int[M], 0, new boolean[N]);
    }

    private static void recursive(int[] sel, int k, boolean[] v) {
        // basis part
        if (k == M) {
            for (int i=0; i<M; i++) {
                System.out.print(sel[i]);
                if (i != M-1) System.out.print(' ');
            }
            System.out.println();
            return;
        }

        // inductive part
        for (int i=0; i<N; i++) {
            if (!v[i]) {
                v[i] = true;
                sel[k] = arr[i];
                recursive(sel, k+1, v);
                v[i] = false;
            }
        }
    }
}