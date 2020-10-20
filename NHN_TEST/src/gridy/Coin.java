package gridy;

import java.util.*;

public class Coin {
    public static void main(String[]args){
        // 500 100 50 10
        // n 은 항상 10의 배수
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();

        int result = 0;
        int [] coins = {500, 100, 50, 10};
        for(int i = 0; i < coins.length; i++){
            result += n / coins[i];
            n %= coins[i];
        }

        System.out.println(result + " " + n);
    }
}
