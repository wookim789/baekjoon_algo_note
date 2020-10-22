package impl;
import java.util.*;

public class Train {
//class Main{
    public static void
        main(String[]args){
        Scanner sc = new Scanner(System.in);

        int result = 0;
        int tot = 0;
        for(int i = 0; i < 4; i++){
            int off = sc.nextInt();
            int on = sc.nextInt();
            sc.nextLine();
            tot += (on - off);
            result = Math.max(result, tot);
        }
        sc.close();
        System.out.println(result);
    }
}
