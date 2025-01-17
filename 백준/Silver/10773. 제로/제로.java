import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int K = input.nextInt();
        Stack<Integer> stacks = new Stack<>();

        for (int k=0; k<K; k++) {
            int num = input.nextInt();
            if (num == 0) {
                stacks.pop();
                continue;
            }
            stacks.add(num);
        }
        if (stacks.isEmpty()) {
            System.out.println(0);
        }
        else {
            int answer = 0;
            for (int s : stacks) {
                answer += s;
            }
            System.out.println(answer);
        }
    }
}
