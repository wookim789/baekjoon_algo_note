package impl;
import java.util.*;

public class NumberSet {
// class Main{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        sc.close();

        int[] data = new int[str.length()];
        for(int i = 0; i < str.length(); i++){
            data[i] = str.charAt(i) - '0';
        }

        Arrays.sort(data);
        int[] countArr = {0,0,0,0,0,0,0,0,0,0};

        int result = 0;
        for(int i = 0; i < data.length; i++){
            if(countArr[data[i]] > 0){
                countArr[data[i]]--;
                continue;
            }else if(data[i] == 6 && countArr[9] > 0){
                countArr[9]--;
                continue;
            }else if(data[i] == 9 && countArr[6] > 0){
                countArr[6]--;
                continue;
            }else{
                for(int idx = 0; idx < 10; idx++){
                    countArr[idx]++;
                }
                countArr[data[i]]--;
                result++;
            }
        }
        System.out.println(result);
    }
}
