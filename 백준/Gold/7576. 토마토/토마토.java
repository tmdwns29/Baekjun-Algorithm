import java.awt.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import static java.lang.System.exit;

class Main {

    static int M, N;
    static int[][] box;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    static Queue<Point> check_start_tomato() {
        Queue<Point> queue = new LinkedList<>();
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (box[i][j] == 1) {
                    queue.add(new Point(i, j));
                }
            }
        }
        return queue;
    }

    static int check_tomato() {
        Queue<Point> queue = check_start_tomato();
        int day = 0;

        while (!queue.isEmpty()) {
            Point p = queue.poll();
            int x = p.x;
            int y = p.y;

            for (int d=0; d<4; d++) {
                int nx = x + dr[d];
                int ny = y + dc[d];

                if (nx>=0 && nx<N && ny>=0 && ny<M && box[nx][ny] == 0) {
                    box[nx][ny] = box[x][y] + 1;
                    day = box[nx][ny];
                    queue.add(new Point(nx, ny));
                }
            }
        }
        return day - 1;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        M = input.nextInt();
        N = input.nextInt();
        box = new int[N][M];
        int answer;

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                box[i][j] = input.nextInt();
            }
        }
        
        if ((answer = check_tomato()) < 0) answer = 0;

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (box[i][j] == 0) {
                    System.out.println(-1);
                    exit(0);
                }
            }
        }
        System.out.println(answer);
    }
}