package impl;
import java.util.*;
public class Tetrimeno {
//class Main{
    private static int [][] map;
    private static int n, m, tot;
    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, 1, 0, -1};
    private static boolean[][] visited;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();

        map = new int[n][m];

        for(int r = 0; r < n; r++){
            for(int c = 0; c < m; c++){
                map[r][c] = sc.nextInt();
            }
            sc.nextLine();
        }
        tot = 0;
        visited = new boolean[n][m];
        for(int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {

                dfs(r, c, 0, 0);
                exceptionCase(r,c);
            }
        }
        System.out.println(tot);

    }
    private static void dfs(int r, int c, int depth, int tmp_tot){
        if(depth == 4){
            tot = Math.max(tot, tmp_tot);
            return;
        }

        if(!(0 <= r && r < n && 0 <= c && c < m)){
            return;
        }

        if(visited[r][c]){
            return;
        }

        depth++;

        tmp_tot += map[r][c];

        for(int i = 0; i < 4; i++){
            int nR = r + dx[i];
            int nC = c + dy[i];
            visited[r][c] = true;
            dfs(nR, nC, depth, tmp_tot);
            visited[r][c] = false;
        }
    }
    private static void exceptionCase(int r, int c){
        int [] dx = {-1, 0, 1};
        int [] dy = {1, 0, -1};

        int tmp_tot = 0;
        int sum_cnt = 0;
        for(int i = 0; i < 3; i++){
            int nR = r + dx[i];
            if(0 <= nR && nR < n){
                tmp_tot += map[nR][c];
                sum_cnt++;
            }
        }
        for(int i = 0; i < 3; i++){
            int nC = c + dy[i];
            if(0 <= nC && nC < m){
                tmp_tot += map[r][nC];
                sum_cnt++;
            }
        }
        tmp_tot -= map[r][c];
        int [] dr = {-1, 0, 1, 0};
        int [] dc = {0, 1, 0, -1};
        if(sum_cnt == 6){
            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                tot = Math.max(tot, tmp_tot - map[nr][nc]);
            }
        }else if(sum_cnt == 5){
            tot = Math.max(tot, tmp_tot);
        }
    }
}

//5 5
//1 200 0 0 200
//9 10 0 300 0
//2 10 0 0 0
//5 10 0 0 0
//100 1 0 0 0