import java.util.Scanner;

public class Main {
    static int N;
    static int M;
    static char[][] board;
    static int cnt = Integer.MAX_VALUE;

    static void check_point(int i, int j) {
        char[] ch = {'W', 'B'};
        for (int a: ch) {

            int cur_cnt = 0;
            for (int r = i; r < i + 8; r++) {
                for (int c = j; c < j + 8; c++) {
                    if (r % 2 == 0) {
                        if (c % 2 == 0 && board[r][c] != a) {
                            cur_cnt++;
                        } else if (c % 2 == 1 && board[r][c] == a) {
                            cur_cnt++;
                        }
                    } else {
                        if (c % 2 == 0 && board[r][c] == a) {
                            cur_cnt++;
                        } else if (c % 2 == 1 && board[r][c] != a) {
                            cur_cnt++;
                        }
                    }
                }
            }
            cnt = Math.min(cnt, cur_cnt);
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        N = input.nextInt();
        M = input.nextInt();
        board = new char[N][M];

        for (int i=0; i<N; i++) {
            char[] temp = input.next().toCharArray();
            for (int j=0; j<M; j++) {
                board[i][j] = temp[j];
            }
        }
        int min_value = Integer.MAX_VALUE;
        for (int i=0; i<N-7; i++) {
            for (int j=0; j<M-7; j++) {
                check_point(i, j);
                min_value = Math.min(cnt, min_value);
            }
        }
        System.out.println(min_value);
    }
}