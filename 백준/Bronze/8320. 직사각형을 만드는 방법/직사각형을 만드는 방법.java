import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();
        int cnt = n;
        /*
        1*n : n*1 -> 6
        2*n : n / 2 >= 2 -> 2
        3*n : n / 3 >= 3

        9

        1*n

        2*2
        2*3
        2*4

        3*3


        6 / 2 == 3
        6 / 3 == 2
        6 / 4 == 1.5
        6 / 5 == 1.2
        6 / 6 == 1
         */
        for (int x = 2; x < n; x++) {
            for (int y = x; y < n; y++) {
                if (x*y <= n) cnt++;
            }
        }
        System.out.println(cnt);
    }
}