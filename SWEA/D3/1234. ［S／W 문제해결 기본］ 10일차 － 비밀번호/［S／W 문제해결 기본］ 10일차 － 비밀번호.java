import java.util.ArrayList;
import java.util.Scanner;

class Solution {
    static int N;
    static ArrayList<Integer> password;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        for (int tc=1; tc<=10; tc++) {
            N = input.nextInt();
            String[] temp = input.next().split("");
            password = new ArrayList<>();

            for (int i=0; i<N; i++) {
                password.add(Integer.parseInt(temp[i]));
            }

            int i = 1;
            while (i < password.size()) {
                if (password.get(i - 1).equals(password.get(i))) {
                    password.remove(i - 1);
                    password.remove(i - 1);
                    i = 1;
                    continue;
                }
                i++;
            }
            System.out.printf("#%d ", tc);
            for (int s: password) {
                System.out.print(s);
            }
            System.out.println();
        }
    }
}