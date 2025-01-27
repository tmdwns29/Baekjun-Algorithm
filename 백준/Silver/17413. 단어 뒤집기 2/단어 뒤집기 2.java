import java.util.Scanner;
import java.util.Stack;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        char[] S = input.nextLine().toCharArray();
        Stack<Character> word = new Stack<>();
        boolean flag = false;

        for (int i=0; i<S.length; i++) {
            if (S[i] == '<') {
                while (!word.isEmpty()) {
                    System.out.print(word.pop());
                }
                flag = true;
            } else if (S[i] == '>') {
                System.out.print('>');
                flag = false;
                continue;
            }

            if (flag) {
                System.out.print(S[i]);
            }
            else {
                word.push(S[i]);
                if (S[i] == ' ' || i == S.length-1) {
                    if (S[i] == ' ') word.pop();
                    while (!word.isEmpty()) {
                        System.out.print(word.pop());
                    }
                    if (i != S.length-1) {
                        System.out.print(' ');
                    }
                }
            }
        }
    }
}