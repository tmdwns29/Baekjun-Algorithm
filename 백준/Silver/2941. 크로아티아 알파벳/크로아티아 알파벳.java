import java.util.Scanner;

class Main {
    public static boolean check_two_abt(String abt) {
        String[] c_abt = {"c=", "c-", "d-", "lj", "nj", "s=", "z="};
        boolean flag = false;
        for (String s: c_abt) {
            if (abt.equals(s)) {
                flag = true;
                break;
            }
        }
        return flag;
    }

    public static boolean check_three_abt(String abt) {
        return abt.equals("dz=");
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String[] word = input.next().split("");

        int idx = 0, cnt = 0;
        while (idx < word.length) {
            if (idx < word.length - 1) {
                String temp = word[idx] + word[idx + 1];
                if (check_two_abt(temp)) {
                    idx += 2;
                    cnt++;
                    continue;
                }
                if (idx < word.length - 2) {
                    String temp2 = word[idx] + word[idx + 1] + word[idx + 2];
                    if (check_three_abt(temp2)) {
                        idx += 3;
                        cnt++;
                        continue;
                    }
                }
            }
            idx++;
            cnt++;
        }
        System.out.println(cnt);
    }
}