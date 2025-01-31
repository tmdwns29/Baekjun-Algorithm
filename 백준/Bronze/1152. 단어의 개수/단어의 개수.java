import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String[] str = input.nextLine().split(" ");
        int cnt = 0;
        for (String s: str) {
            if (s.isEmpty()) {
                continue;
            }
            cnt++;
        }
        System.out.println(cnt);
    }
}