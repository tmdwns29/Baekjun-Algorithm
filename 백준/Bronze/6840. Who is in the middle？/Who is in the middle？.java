import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int[] bear = new int[3];
        int answer = 0;

        for (int i=0; i<3; i++) {
            bear[i] = input.nextInt();
        }

        Arrays.sort(bear);

        System.out.println(bear[1]);
    }
}