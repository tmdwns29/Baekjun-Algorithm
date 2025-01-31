import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
    static int w,h;
    static int[][] map;
    static int[] dr = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int[] dc = {-1, 0, 1, -1, 1, -1, 0, 1};
    static boolean[][] visited;

    static void count_ground(int i, int j) {
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(i, j));
        visited[i][j] = true;

        while (!queue.isEmpty()) {
            Point p = queue.poll();
            int x = p.x;
            int y = p.y;

            for (int d=0; d<8; d++) {
                int nx = x + dr[d];
                int ny = y + dc[d];

                if (nx>=0 && nx<h && ny>=0 && ny<w && !visited[nx][ny] && map[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    queue.add(new Point(nx, ny));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            w = input.nextInt();
            h = input.nextInt();
            if (w==0 && h==0) {
                break;
            }
            map = new int[h][w];
            visited = new boolean[h][w];
            int cnt = 0;

            for (int i=0; i<h; i++) {
                for (int j=0; j<w; j++) {
                    map[i][j] = input.nextInt();
                }
            }

            for (int i=0; i<h; i++) {
                for (int j=0; j<w; j++) {
                    if (map[i][j] == 1 && !visited[i][j]) {
                        count_ground(i, j);
                        cnt++;
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}