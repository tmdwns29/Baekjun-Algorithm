import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt();
        if (N == 1) System.out.println(2);
        else {
            int answer = ((N/2)+1) * ((N-N/2)+1);
            System.out.println(answer);
        }
    }
}