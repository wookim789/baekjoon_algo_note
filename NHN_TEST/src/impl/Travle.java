package impl;

import java.util.*;

public class Travle {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();
        String[] ways = sc.nextLine().split(" ");
        sc.close();

        int[] dr = {0, 0, -1, 1};
        int[] dc = {-1, 1, 0, 0 };

        HashMap<String, Integer> dirMap = new HashMap<>();
        dirMap.put("L", 0);
        dirMap.put("R", 1);
        dirMap.put("U", 2);
        dirMap.put("D", 3);

        int [] codi = {1, 1};

        for(String dir : ways){
            int dirIdx = dirMap.get(dir);
            int next_r = codi[0] + dr[dirIdx];
            int next_c = codi[1] + dc[dirIdx];

            if(0 < next_r && next_r <= n && 0 < next_c && next_c <= n){
                codi[0] = next_r;
                codi[1] = next_c;
            }
        }
        System.out.println(codi[0] + " " + codi[1]);
    }
}
