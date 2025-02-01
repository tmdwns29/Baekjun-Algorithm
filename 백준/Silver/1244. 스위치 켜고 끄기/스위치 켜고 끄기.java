import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        /*
            남학생 : 스위치 번호가 자기가 받은 수의 배수 -> 스위치 상태 바꿈 ex) 3-> 3,6
            여학생 : 자기가 받은 수와 같은 번호가 붙은 스위치 중심 좌우 대칭, 가장 많은 스위치 포함 구간-> 모두 바꿈
                    그 구간의 스위치 개수는 항상 홀수

            1 2 3 4 5 6 7 8
            0 1 1 1 0 1 0 1

         */

        int switch_num = input.nextInt();
        int[] switch_status = new int[switch_num+1];

        for (int i=1; i<=switch_num; i++) {
            switch_status[i] = input.nextInt();
        }

        int student_num = input.nextInt();
        int gender, number;

        for (int i=0; i<student_num; i++) {
            gender = input.nextInt();
            number = input.nextInt();

            if (gender == 1) {
                for (int n=1; n<switch_status.length; n++) {
                    if (n % number == 0) {
                        if (switch_status[n] == 0) switch_status[n] = 1;
                        else switch_status[n] = 0;
                    }
                }
            }
            else if (gender == 2) {
                int left_idx = number - 1;
                int right_idx = number + 1;

                if (switch_status[number] == 0) switch_status[number] = 1;
                else switch_status[number] = 0;

                while (true) {
                    if (left_idx>=1 && left_idx<=switch_num && right_idx>=1 && right_idx<=switch_num) {
                        if (switch_status[left_idx] == switch_status[right_idx]) {
                            if (switch_status[left_idx] == 0) switch_status[left_idx] = 1;
                            else switch_status[left_idx] = 0;

                            if (switch_status[right_idx] == 0) switch_status[right_idx] = 1;
                            else switch_status[right_idx] = 0;
                        }
                        else {
                            break;
                        }
                    }
                    else {
                        break;
                    }
                    left_idx--;
                    right_idx++;
                }
            }
        }
        for (int a=1; a<=switch_num; a++) {

            System.out.print(switch_status[a]);
            if (a % 20 == 0) System.out.println();
            if (a != switch_num && a % 20 != 0) {
                System.out.print(' ');
            }
        }
        System.out.println();
    }
}