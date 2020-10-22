package impl;
import java.util.*;

public class YoutPlay {
//class Main{
    public static void main(String[]args){
            Scanner sc = new Scanner(System.in);


            for(int i = 0; i < 3; i++){
                int score = 0;
                for(int j = 0; j < 4; j++){
                    score += sc.nextInt();
                }
                if(score == 4){
                    System.out.println("E");
                }else if (score == 3){
                    System.out.println("A");
                }else if (score == 2){
                    System.out.println("B");
                }else if (score == 1){
                    System.out.println("C");
                }else if (score == 0){
                    System.out.println("D");
                }
                sc.nextLine();
            }
    }
}
