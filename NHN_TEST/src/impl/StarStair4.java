package impl;
import java.util.*;

public class StarStair4 {
//class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        String up = "*";
        String down = "";
        String nStar = " *";
        boolean isUp = false;

        for(int i = 1; i < n; i++){
            if(isUp){
                up += nStar;
                isUp = false;
            }else{
                down += nStar;
                isUp = true;
            }
        }
        for(int i = 0; i < n; i++){
            System.out.println(up);
            System.out.println(down);
        }
    }
}
