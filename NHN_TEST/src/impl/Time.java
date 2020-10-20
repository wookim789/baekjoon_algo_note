package impl;
import java.util.*;

public class Time {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        int result = 0;
        for(int h = 0; h < n + 1 ; h++){
            for(int m = 0; m < 60; m++){
                for(int s = 0; s < 60; s++){
                    String time = Integer.toString(h) + Integer.toString(m) + Integer.toString(s);
                    if(time.indexOf("3") != -1){
                        result ++;
                    }
                }
            }
        }
        System.out.println(result);
    }
}
