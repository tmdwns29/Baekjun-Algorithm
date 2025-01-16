import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int A = input.nextInt();
        int B = input.nextInt();
        int C = input.nextInt();

        if (A+B == C) {
            System.out.println("correct!");
        }
        else {
            System.out.println("wrong!");
        }
        input.close();
    }
}