package gready;

import java.util.Scanner;

public class SugarDelivery {
//class Main{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();
        sc.close();

        int five_cnt = n / 5;
        while(true){
            if(five_cnt > 0 && (n - five_cnt * 5) % 3 != 0){
                five_cnt -= 1;
            }else if((n - five_cnt * 5) % 3 == 0){
                n = n - five_cnt * 5;
                int tree_cnt = n/3;
                System.out.println(five_cnt + tree_cnt);
                break;
            }else if (five_cnt == 0 || n % 3 != 0){
                System.out.println(-1);
                break;
            }
        }
    }
}
