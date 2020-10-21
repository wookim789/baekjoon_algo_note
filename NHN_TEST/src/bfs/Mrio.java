package bfs;
import java.util.*;

public class Mrio {
    private static int n, m;
    private static int[][]map;
    public static void main(String[]args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();

        map = new int[n][m];

        for (int r = 0; r < n; r++) {
            String row = sc.nextLine();
            for (int c = 0; c < m; c++) {
                map[r][c] = row.charAt(c) - '0';
            }
        }
        System.out.println(bfs());
    }
    private static int bfs(){
        int cnt = 1;

        Integer[] firstCodi = {0,0, cnt};
        boolean[][] visited = new boolean[n][m];

        Queue<Integer[]> que = new LinkedList<>();
        que.offer(firstCodi);

        int dx[] = {1,0,-1,0};
        int dy[] = {0,1,0,-1};

        while(!que.isEmpty()){
            Integer[] codi = que.poll();
            int r = codi[0];
            int c = codi[1];

            if(r == n - 1 && c == m - 1){
                return codi[2];
            }
            if(visited[r][c]){
                continue;
            }
            visited[r][c] = true;

            if(map[r][c] == 1){
                codi[2]++;

                for(int i = 0; i < 4; i++){
                    int next_r = r + dx[i];
                    int next_c = c + dy[i];
                    if(0 <= next_r && next_r < n && 0 <= next_c && next_c < m){
                        if(map[next_r][next_c]==1){
                            que.offer(new Integer[]{next_r, next_c, codi[2]});
                        }
                    }
                }
            }
        }
        return 0;
    }
}
//
//5 6
//101010
//111111
//000001
//111111
//111111
//10
//5 6
//111101
//000111
//010010
//011010
//000111