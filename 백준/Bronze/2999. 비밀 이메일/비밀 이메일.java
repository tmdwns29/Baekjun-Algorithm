import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        char[] message = input.next().toCharArray();
        int R = 1, C = message.length;

        for (int i=1; i<=message.length; i++) {
            if (message.length % i == 0) {
                if ((int)(message.length / i) >= i) {
                    R = i;
                    C = (int)(message.length / i);
                }
            }
        }

        char[][] encrypt_msg = new char[R][C];
        int idx = 0;
        for (int i=0; i<C; i++) {
            for (int j=0; j<R; j++) {
                encrypt_msg[j][i] = message[idx++];
            }
        }

        for (int i=0; i<R; i++) {
            for (char m: encrypt_msg[i]) {
                System.out.print(m);
            }
        }
    }
}