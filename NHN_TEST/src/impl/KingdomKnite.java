package impl;
import java.util.*;

public class KingdomKnite {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        String codiStr = sc.nextLine();
        sc.close();

        int[] codi = new int[2];

        codi[0] = codiStr.charAt(0) - 'a' + 1;
        codi[1] = codiStr.charAt(1) - '0';

        int result = 0;
        if(codi[0] - 2 > 0){
            result += check(1, codi);
        }
        if(codi[0] + 2 < 9){
            result += check(1, codi);
        }
        if(codi[1] - 2 > 0){
            result += check(0, codi);
        }
        if(codi[1] + 2 < 9){
            result += check(0, codi);
        }
        System.out.println(result);
    }

    public static int check(int idx, int[] codi){
        int result = 0;
        if(0 < codi[idx] - 1){
            result ++;
        }
        if(codi[idx] + 1 < 9){
            result ++;
        }
        return result;
    }
}
