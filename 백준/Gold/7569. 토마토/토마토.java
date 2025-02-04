import java.awt.Point;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
	static int M, N, H, day;
	static int[][][] boxes;
	static int[] dr = {-1, 1, 0, 0, 0, 0};
	static int[] dc = {0, 0, -1, 1, 0, 0};
	static int[] dh = {0, 0, 0, 0, -1, 1};
	static Queue<Integer> hq = new LinkedList<>();
	
	static Queue<Point> check_start_rc() {
		Queue<Point> queue = new LinkedList<>();
		for (int h=0; h<H; h++) {
			for (int n=0; n<N; n++) {
				for (int m=0; m<M; m++) {
					if (boxes[h][n][m] == 1) {
						queue.add(new Point(n,m));
						hq.add(h);
					}
				}
			}
		}
		return queue;
	}
	
	static void count_tomato() {
		Queue<Point> queue = check_start_rc();
		Queue<Integer> hqueue = hq;

		while (!queue.isEmpty() && !hqueue.isEmpty()) {
			Point p = queue.poll();
			
			int r = p.x;
			int c = p.y;
			int l = hqueue.poll();
			
			for (int d=0; d<6; d++) {
				int nr = r + dr[d];
				int nc = c + dc[d];
				int nh = l + dh[d];
				
				if (nr>=0 && nr<N && nc>=0 && nc<M && nh>=0 && nh<H) {
					if (boxes[nh][nr][nc] == 0) {
						queue.add(new Point(nr, nc));
						hqueue.add(nh);
						
						boxes[nh][nr][nc] = boxes[l][r][c] + 1;
						day = boxes[nh][nr][nc];
					}
				}
			}	
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		M = sc.nextInt();
		N = sc.nextInt();
		H = sc.nextInt();
		
		boxes = new int[H][N][M];
		
		for (int h=0; h<H; h++) {
			for (int n=0; n<N; n++) {
				for (int m=0; m<M; m++) {
					boxes[h][n][m] = sc.nextInt();
				}
			}
		}
		count_tomato();
		boolean flag = true;
		for (int h=0; h<H; h++) {
			for (int n=0; n<N; n++) {
				for (int m=0; m<M; m++) {
					if (boxes[h][n][m] == 0) {
						flag = false;
						break;
					}
				}
			}
		}
		if (flag) {
			if (day == 0) System.out.println(0);
			else System.out.println(day-1);
		}
		else System.out.println(-1);
	}
}