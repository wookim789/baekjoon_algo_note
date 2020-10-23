package impl;
import java.util.*;

public class StarStair3 {
//class Main{
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();

        for(int rIdx = 0; rIdx < n; rIdx++){
            // 앞공백
            String fS = "";
            // 총 숫자 계산을 위한 숫자

            for(int i = 1; n - 2 * i > 0; i++ ){
                System.out.println(fS + "* *");
                fS += " ";
            }
            if(n % 2 == 0){
                if(n - 2 == 0){
                    System.out.println("*");
                    System.out.println(" *");
                }else{
                    System.out.println(fS + "* *");
                }
            }else{
                System.out.println(fS + "*");
            }
        }
    }
}
