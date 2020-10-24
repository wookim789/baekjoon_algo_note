package impl;
import java.util.*;

public class Alpa {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String tgt = sc.nextLine();
        sc.close();

        int z = 'z' - 'a';

        int[] result = new int[z + 1];

        for(int i = 0; i < tgt.length(); i++){
            result[tgt.charAt(i) - 'a'] += 1;
        }

        for(int i = 0; i < result.length; i++){
            System.out.print(result[i] + " ");
        }
    }
}
