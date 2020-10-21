package dfs;
import java.util.*;

public class IcecreamCnt {
    private static boolean[][] visited;
    private static boolean isIcecream;
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();

        int [][] map = new int[n][m];
        visited = new boolean[n][m];

        for(int r = 0; r < n; r++){
            String row = sc.nextLine();
            for(int c = 0; c < m; c++){
                map[r][c] = row.charAt(c) - '0';
            }
        }
        sc.close();
        int tot = 0;
        for(int r = 0; r < n; r++){
            for(int c = 0; c < m; c ++){
                isIcecream = false;
                dfs(r, c, n, m, map);
                if(isIcecream){
                    tot++;
                }
            }
        }
        System.out.println(tot);
    }
    private static void dfs(int r, int c, int n, int m, int[][]map){
        if(visited[r][c]){
            return;
        }

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        visited[r][c] = true;

        if(map[r][c] == 0){
            isIcecream = true;

            for(int i = 0; i < 4; i++){
                int next_r = r + dx[i];
                int next_c = c + dy[i];

                if(0 <= next_r && next_r < n && 0 <= next_c && next_c < m){
                    dfs(next_r, next_c, n, m, map);
                }
            }
        }
        return;
    }
}
//00110
//00011
//11111
//00000