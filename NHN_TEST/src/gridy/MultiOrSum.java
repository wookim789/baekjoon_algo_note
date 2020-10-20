package gridy;

import java.util.*;

public class MultiOrSum {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);

        String data = sc.nextLine();
        sc.close();

        int result = data.charAt(0) - '0';

        for(int i = 1; i < data.length(); i++){
            int next = data.charAt(i) - '0';
            if(result <= 1 || next <= 1){
                result += next;
            }else{
                result *= next;
            }
        }
        System.out.println(result);
    }
}

