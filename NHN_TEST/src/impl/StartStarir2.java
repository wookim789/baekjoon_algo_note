package impl;
import java.util.*;

public class StartStarir2 {
//class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();


        for(int rIdx = 0; rIdx < n; rIdx++){
            if(n == 1){
                System.out.println("*");
                break;
            }
            // 앞 공백
            String fS = "";
            // 중간 공백
            String mS = "";
            for(int i = 0; i < n - 2; i++){
                mS += " ";
            }

            if(n % 2 == 0){
                mS += " ";
            }

            for(int i = 0; i < 2 * n - 1 ; i++){
                System.out.print(fS);
                System.out.print("*");
                System.out.print(mS);
                if(!(i == 0 && n % 2 == 0)){
                    System.out.println("*");
                }else{
                    System.out.println();
                }
                fS += " ";
                if(mS.length() > 1){
                    mS = mS.substring(1, mS.length() - 1);
                }else{
                    System.out.print(fS);
                    System.out.println("*");
                    break;
                }
            }
        }

    }
}
