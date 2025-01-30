import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();

        for (int tc=1; tc<=T; tc++) {
            int N = input.nextInt();
            int cur_acc = 0;
            int distance = 0;

            for (int i=0; i<N; i++) {
                int command = input.nextInt();
                if (command == 0) {
                    distance += cur_acc;
                    continue;
                }
                int accel = input.nextInt();

                if (command == 1) {
                    cur_acc += accel;
                    distance += cur_acc;
                }
                else if (command == 2) {
                    if (cur_acc < accel) {
                        cur_acc = 0;
                    }
                    else {
                        cur_acc -= accel;
                    }
                    distance += cur_acc;
                }
            }
            System.out.printf("#%d %d\n", tc, distance);
        }
    }
}