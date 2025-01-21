import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[] sticks = sc.next().toCharArray();
		Stack<Character> stack = new Stack<Character>();
		int cnt = 0;
		
		for (int i=0; i<sticks.length; i++) {
			if (sticks[i] == '(') {
				stack.push(sticks[i]);
			}
			else {
				stack.pop();
				if (sticks[i-1] == '(') {
					cnt += stack.size();
				}
				else {
					cnt += 1;
				}
			}
		}
        System.out.println(cnt);
		sc.close();
	}
}
