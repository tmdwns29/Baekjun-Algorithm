import java.util.Scanner;

class Solution {
    static int R, C, max_cnt;
    static char[][] map;
    static boolean[] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static void search_alphabet(int i, int j, int depth) {

        if (depth > max_cnt) {
            max_cnt = depth;
        }

        for (int d=0; d<4; d++) {
            int nx = i + dr[d];
            int ny = j + dc[d];
            if (nx>=0 && nx<R && ny>=0 && ny<C) {
                int alphabet = map[nx][ny]-'A';
                if (!visited[alphabet]) {
                    visited[alphabet] = true;
                    search_alphabet(nx, ny, depth+1);
                    visited[alphabet] = false;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();

        for (int tc=1; tc<=T; tc++) {
            R = input.nextInt();
            C = input.nextInt();
            map = new char[R][C];
            visited = new boolean[26]; // 알파벳 개수
            max_cnt = 0;
            for (int i=0; i<R; i++) {
                String tmp = input.next();
                for (int j = 0; j < C; j++) {
                    map[i][j] = tmp.charAt(j);
                }
            }
            visited[map[0][0]-'A'] = true;

            search_alphabet(0, 0, 1);

            System.out.printf("#%d %d\n", tc, max_cnt);
        }
    }
}