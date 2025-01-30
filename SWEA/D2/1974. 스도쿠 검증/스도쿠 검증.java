import java.util.Scanner;

class Solution {
    static int[][] sudoku;
    static int[] dr = {-1, -1, -1, 0, 0, 0, 1, 1, 1};
    static int[] dc = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
    static boolean[] check_num;

    static boolean check_rows() {
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                int sel_num = sudoku[i][j];
                if (!check_num[sel_num]) {
                    check_num[sel_num] = true;
                }
                else {
                    return false;
                }
            }
            check_num = new boolean[10];
        }
        return true;
    }

    static boolean check_3x3() {

        for (int i=1; i<=7; i+=3) {
            for (int j=1; j<=7; j+=3) {
                int cur_r;
                int cur_c;
                int sel_num;
                for (int d=0; d<9; d++) {
                    cur_r = i + dr[d];
                    cur_c = j + dc[d];
                    sel_num = sudoku[cur_r][cur_c];
                    if (!check_num[sel_num]) {
                        check_num[sel_num] = true;
                    }
                    else {
                        return false;
                    }
                }
                check_num = new boolean[10];
            }
        }
        return true;
    }

    static boolean check_cols() {
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                int sel_num = sudoku[j][i];
                if (!check_num[sel_num]) {
                    check_num[sel_num] = true;
                }
                else {
                    return false;
                }
            }
            check_num = new boolean[10];
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();

        for (int tc=1; tc<=T; tc++) {
            check_num = new boolean[10];
            sudoku = new int[9][9];

            for (int i=0; i<9; i++) {
                for (int j=0; j<9; j++) {
                    sudoku[i][j] = input.nextInt();
                }
            }
            System.out.printf("#%d ",tc);
            if (check_rows() && check_cols() && check_3x3()) {
                System.out.println(1);
            }
            else {
                System.out.println(0);
            }
        }
    }
}