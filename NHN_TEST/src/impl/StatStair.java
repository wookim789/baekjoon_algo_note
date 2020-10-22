package impl;
import java.util.*;

public class StatStair {
//class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        String blank = "";
        String star = "";
        for(int i = 0; i < 2 * n -1; i++){
            star += "*";
        }

        for(int i = n; i > 0; i--){
            System.out.print(blank);
            blank += " ";
            System.out.print(star);
            if(star.length() > 2){
                star = star.substring(2);
            }
            System.out.println();
        }
    }
}
