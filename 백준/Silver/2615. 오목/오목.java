import java.util.Scanner;

class Main {
    static int[] dr = {-1, 0, 1, 1};
    static int[] dc = {1, 1, 1, 0};
    static int[][] board = new int[19][19];
    static int ans1;
    static int ans_r, ans_c;

    static void check_point(int color, int dir, int i, int j) {
        int r = i, c = j;
        for (int s=1; s<5; s++) {
//            System.out.print(s+"번 "+r+","+c+"\n");
            if (r>=0 && r<19 && c>=0 && c<19 && board[r][c] == color) {
                if (s == 4) {
                    int chk_e_r = r+dr[dir];
                    int chk_e_c = c+dc[dir];
                    int chk_s_r = i-dr[dir]*2;
                    int chk_s_c = j-dc[dir]*2;
//                    System.out.println("끝부분 걸림");
                    if (chk_e_r>=0 && chk_e_r<19 && chk_e_c>=0 && chk_e_c<19) {
                        if (board[chk_e_r][chk_e_c] == color) {
                            break;
                        }
                    }
//                    System.out.println("앞부분 걸림");
                    if (chk_s_r>=0 && chk_s_r<19 && chk_s_c>=0 && chk_s_c<19) {
                        if (board[chk_s_r][chk_s_c] == color) {
//                            System.out.printf("웽? %d, %d = %d\n", chk_s_r, chk_s_c, color);
                            break;
                        }
                    }
//                    System.out.println("오목이다씨발");
                    ans1 = color;
                    ans_r = i-dr[dir] + 1;
                    ans_c = j-dc[dir] + 1;
                    break;
                }
                r += dr[dir];
                c += dc[dir];
//                System.out.println(""+s);
            }
            else {
                break;
            }
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        for (int i=0; i<19; i++) {
            for (int j=0; j<19; j++) {
                board[i][j] = input.nextInt();
            }
        }

        for (int i=0; i<19; i++) {
            for (int j=0; j<19; j++) {
                int color = board[i][j];
                if (color != 0) {

                    for (int d=0; d<4; d++) {
                        int nr = i+dr[d];
                        int nc = j+dc[d];
                        if (nr>=0 && nr<19 && nc>=0 && nc<19) {
                            check_point(color, d, nr, nc);
                        }
                    }

                }

            }
        }
        System.out.println(ans1);
        if (ans1 != 0) {
            System.out.printf("%d %d\n", ans_r, ans_c);
        }
    }
}