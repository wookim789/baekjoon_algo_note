package gridy;
import java.util.*;

/**
 * 1이 될 때 까지
 */
public class BeOne {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        int result = 0;
        sc.close();

        while(n != 1){
            if(n % k == 0){
                n /= k;
            }else{
                n --;
            }
            result ++;
        }
        System.out.println(result);
    }
}
