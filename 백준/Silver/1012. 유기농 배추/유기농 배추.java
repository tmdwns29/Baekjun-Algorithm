import java.awt.Point;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int M, N, K;
	static int[][] bat;
	static boolean[][] visited;
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};
	
	static void Search_BaeChu(int r, int c) {
		Queue<Point> queue = new LinkedList<>();
		queue.add(new Point(r, c));
		
		while (!queue.isEmpty()) {
			Point p = queue.poll();
			int x = p.x;
			int y = p.y;
			
			for (int d=0; d<4; d++) {
				int nx = x+dx[d];
				int ny = y+dy[d];
				
				if (nx>=0 && nx<M && ny>=0 && ny<N && !visited[nx][ny]) {
					if (bat[nx][ny] == 1) {
						visited[nx][ny] = true;
						queue.add(new Point(nx, ny));
					}
				}
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int tc=0; tc<T; tc++) {
			M = sc.nextInt();
			N = sc.nextInt();
			K = sc.nextInt();
			bat = new int[M][N];
			visited = new boolean[M][N];
			for (int k=0; k<K; k++) {
				int X = sc.nextInt();
				int Y = sc.nextInt();
				
				bat[X][Y] = 1;
			}
			int cnt = 0;
			for (int i=0; i<M; i++) {
				for (int j=0; j<N; j++) {
					if (bat[i][j] == 1 && !visited[i][j]) {
						Search_BaeChu(i, j);
						cnt++;
					}
				}
			}
			System.out.println(cnt);
		}
		sc.close();
	}
}