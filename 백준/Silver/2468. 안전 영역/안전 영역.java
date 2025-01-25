import java.awt.*;
import java.util.*;

class Main {
    static int N;
    static int[][] area;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static void check_safety_area(int r, int c) {
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(r, c));

        while (!queue.isEmpty()) {
            Point p = queue.poll();
            int x = p.x;
            int y = p.y;

            for (int i=0; i<4; i++) {
                int nr = x + dr[i];
                int nc = y + dc[i];

                if (nr>=0 && nr<N && nc>=0 && nc<N && visited[nr][nc]) {
                    visited[nr][nc] = false;
                    queue.add(new Point(nr, nc));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        N = input.nextInt();
        int max_num = Integer.MIN_VALUE;
        int answer = Integer.MIN_VALUE;
        int cnt = 0;
        area = new int[N][N];
        visited = new boolean[N][N];

        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                area[i][j] = input.nextInt();
                max_num = Math.max(area[i][j], max_num);
            }
        }

        for (int n=1; n<=max_num; n++) {
            cnt = 0;
            visited = new boolean[N][N];
            for (int i=0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    if (area[i][j] > n) {
                        visited[i][j] = true;
                    }
                }
            }

            for (int i=0; i<N; i++) {
                for (int j=0; j<N; j++) {
                    if (visited[i][j]) {
                        check_safety_area(i, j);
                        cnt++;
                    }
                }
            }
            answer = Math.max(answer, cnt);
        }
        if (answer == 0) answer = 1;
        System.out.println(answer);

        input.close();
    }
}