package bfs;

import java.util.Scanner;
import java.util.*;

//public class HideAndSearch {

class Main{
    private static Queue<Integer> que;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.nextLine();
        sc.close();

        if(n >= k){
            System.out.println(n - k);
        }else{
            int result = bfs(n, k);
            System.out.println(result);
        }
    }

    public static int bfs(int n, int k) {
        int[] dpTable = new int[100001];
        dpTable[n] = 0;

        Queue<Integer> curPointQue = new LinkedList<>();
        curPointQue.add(n);

        while(!curPointQue.isEmpty()){
            int curPoint = curPointQue.poll();
            if (curPoint == k){
                return dpTable[curPoint];
            }
            int [] nextPointArr = {curPoint - 1, curPoint + 1, 2 * curPoint};

            for(int nextPoint : nextPointArr){
                if(0 <= nextPoint && nextPoint <= 100000){
                    if(dpTable[nextPoint] == 0 && nextPoint != k){
                        dpTable[nextPoint] = dpTable[curPoint] + 1;
                        curPointQue.add(nextPoint);
                    }else if(nextPoint == k){
                        return dpTable[curPoint] + 1;
                    }
                }
            }
        }
        return 0;
    }
}
