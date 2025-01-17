import java.util.ArrayList;
import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int K = input.nextInt();
		int num, sum=0, cnt=-1;
		ArrayList<Integer> arr = new ArrayList<>();
		
		for (int k=0; k<K; k++) {
			num = input.nextInt();
			
			if (num == 0) {
				arr.remove(cnt);
				cnt--;
				continue;
			}
			arr.add(num);
			cnt++;
		}
		
		if (arr.isEmpty()) {
			System.out.println(0);
		}
		else {
			for (int s: arr) {
				sum += s;
			}
			System.out.println(sum);
		}
		input.close();
	}
}