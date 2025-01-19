import java.util.Scanner;

class Solution {

    public static boolean check_Zero_hole(char a, char b) {
        boolean flag1 = false, flag2 = false;
        char[] no_hole = {
                'C','E','F','G','H','I','J','K','L','M','N','S','T','U','V','W','X','Y','Z'
        };
        for (char c: no_hole) {
            if (a == c) {
                flag1 = true;
                break;
            }
        }
        for (char c: no_hole) {
            if (b == c) {
                flag2 = true;
                break;
            }
        }
        if (flag1 && flag2){
            return true;
        }
        else {
            return false;
        }
    }

    public static boolean check_one_hole(char a, char b) {
        boolean flag1 = false, flag2 = false;
        char[] one_hole = {'A','D','O','P','Q','R'};

        for (char c: one_hole) {
            if (a == c) {
                flag1 = true;
                break;
            }
        }
        for (char c: one_hole) {
            if (b == c) {
                flag2 = true;
                break;
            }
        }
        if (flag1 && flag2){
            return true;
        }
        else {
            return false;
        }
    }

    public static boolean check_two_hole(char a, char b) {
        return a == 'B' && b == 'B';
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int T = input.nextInt();

        for (int tc=1; tc<=T; tc++) {
            char[] str1 = input.next().toCharArray();
            char[] str2 = input.next().toCharArray();
            int str1_cnt = 0, str2_cnt = 0;
            boolean position = true;

            if (str1.length != str2.length) {
                System.out.printf("#%d DIFF\n", tc);
                continue;
            }
            for (int i=0; i<str1.length; i++) {
                if (str1[i]=='A'||str1[i]=='D'||str1[i]=='O'||str1[i]=='P'||str1[i]=='Q'||str1[i]=='R') {
                    str1_cnt++;
                }
                else if (str1[i] == 'B') {
                    str1_cnt += 2;
                }

                if (str2[i]=='A'||str2[i]=='D'||str2[i]=='O'||str2[i]=='P'||str2[i]=='Q'||str2[i]=='R') {
                    str2_cnt++;
                }
                else if (str2[i] == 'B') {
                    str2_cnt += 2;
                }

                if (!check_Zero_hole(str1[i], str2[i]) && !check_one_hole(str1[i], str2[i]) && !check_two_hole(str1[i], str2[i])) {
                    position = false;
                }

            }

            if (str1_cnt == str2_cnt && position) {
                System.out.printf("#%d SAME\n", tc);
            }
            else {
                System.out.printf("#%d DIFF\n", tc);
            }
        }

    }
}