package array;

import java.io.BufferedReader;
import java.io.InputStreamReader;

//public class Array1 {
class Main{
    public static void main(String []args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long tot = Integer.parseInt(br.readLine());
        tot *= Integer.parseInt(br.readLine());
        tot *= Integer.parseInt(br.readLine());
        String[] result = Long.toString(tot).split("");
        int[] countArr = new int[10];

        for(String num : result){
            countArr[Integer.parseInt(num)] += 1;
        }

        for(int idx: countArr){
            System.out.println(idx);
        }
    }
}
