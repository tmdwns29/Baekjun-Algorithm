import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int A = input.nextInt();
        int B = input.nextInt();
        int cnt = 0;
        while (true) {
            if (A >= 2 && B >= 1) {
                A -= 2;
                B -= 1;
                cnt++;
            }
            else {
                break;
            }
        }
        System.out.println(cnt);
    }
}