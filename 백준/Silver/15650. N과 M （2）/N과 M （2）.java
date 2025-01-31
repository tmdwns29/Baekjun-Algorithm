import java.util.Scanner;

class Main {
    static int N, M;
    static int[] arr;

    static void recursive(int idx, int depth, int[] sel) {

        // basis part
        if (depth == M) {
            for (int i=0; i<M; i++) {
                System.out.print(sel[i]);
                if (i != M-1) {
                    System.out.print(' ');
                }
            }
            System.out.println();
            return;
        }

        if (idx == arr.length) {
            return;
        }

        // inductive part
        sel[depth] = arr[idx];
        recursive(idx+1, depth+1, sel);
        recursive(idx+1, depth, sel);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        N = input.nextInt();
        M = input.nextInt();
        arr = new int[N];

        for (int i=1; i<=N; i++) {
            arr[i-1] = i;
        }

        recursive(0, 0, new int[M]);
    }

}