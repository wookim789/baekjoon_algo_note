package dp;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Wave {
// class Main{
    public static void main(String [] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());
        int [] kArr = new int [testCase];
        int dpSize = 0;

        for(int idx = 0; idx < testCase; idx++){
            kArr[idx] = Integer.parseInt(br.readLine());
            dpSize = Math.max(dpSize, kArr[idx]);
        }

        long [] dpTable = new long[dpSize];
        dpTable[0] = 1;
        dpTable[1] = 1;
        dpTable[2] = 1;
        dpTable[3] = 2;
        dpTable[4] = 2;

        for(int idx = 5; idx < dpSize; idx++){
            dpTable[idx] = dpTable[idx - 1] + dpTable[idx - 5];
        }

        for(int k : kArr){
            System.out.println(dpTable[k-1]);
        }
    }
}