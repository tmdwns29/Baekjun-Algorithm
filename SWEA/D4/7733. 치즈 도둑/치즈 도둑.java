import java.awt.*;
import java.util.*;

class Solution {
    static int N;
    static int[][] cheese;
    static boolean[][] visited;
    static int[] dr = {0, 0, -1, 1};
    static int[] dc = {-1, 1, 0, 0};

    static void count_cheese(int r, int c) {
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(r, c));
        visited[r][c] = true;

        while (!queue.isEmpty()) {
            Point p = queue.poll();
            int x = p.x;
            int y = p.y;

            for (int d=0; d<4; d++) {
                int nx = x + dr[d];
                int ny = y + dc[d];

                if (nx>=0 && nx<N && ny>=0 && ny<N && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.add(new Point(nx, ny));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();

        for (int tc=1; tc<=T; tc++) {
            N = input.nextInt();
            int max_num = 0;
            int max_cheese = 0;
            cheese = new int[N][N];

            for (int i=0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    cheese[i][j] = input.nextInt();
                    max_num = Math.max(cheese[i][j], max_num);
                }
            }

            for (int taste=1; taste<=max_num; taste++) {
                visited = new boolean[N][N];
                for (int i=0; i<N; i++) {
                    for (int j=0; j<N; j++) {
                        if (cheese[i][j] <= taste) {
                            visited[i][j] = true;
                        }
                    }
                }

                int cnt = 0;
                for (int i=0; i<N; i++) {
                    for (int j=0; j<N; j++) {
                        if (!visited[i][j]) {
                            count_cheese(i, j);
                            cnt++;
                        }
                    }
                }
                max_cheese = Math.max(max_cheese, cnt);
            }
            if (max_cheese == 0) max_cheese = 1;
            System.out.printf("#%d %d\n", tc, max_cheese);
        }
    }
}