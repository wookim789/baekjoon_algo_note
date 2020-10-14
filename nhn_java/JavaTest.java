import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class JavaTest {
    private static int section_cnt;
    private static int tot;
    private static int n;
    private static List<Integer> section_tot_num;
    private static int [][]map;
    public static void main(String args[]) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            n = Integer.parseInt(br.readLine());
            map = new int[n][n];
            for(int i = 0; i < n; i++){
                String [] arr = br.readLine().split(" ");
                int[] row_list = new int[n];
                int idx = 0;
                for(String s : arr){
                    row_list[idx] = Integer.parseInt(s);
                    idx += 1;
                }
                map[i] = row_list;
            }
        } catch (NumberFormatException | IOException e) {
            e.printStackTrace();
        }

        section_tot_num = new ArrayList<>();
        for(int r = 0; r < n; r++){
            for(int c = 0; c < n; c++){
                // 영역의 칸 수
                tot = 0;
                dfs(r, c);
                if (tot != 0){
                    section_cnt += 1;
                    section_tot_num.add(tot);
                }
            }
        }
        System.out.println(section_cnt);
        Collections.sort(section_tot_num);
        for(int tot : section_tot_num){
            System.out.print(tot);
            System.out.print(" ");
        }

    }

    public static void dfs(int r, int c){
        // 재귀 종료처리
        if (map[r][c] == -1){
            return;
        }
        if (map[r][c] == 0){
            map[r][c] = -1;
            return;
        }
        int [] dx = {1, -1, 0, 0};
        int [] dy = {0, 0, 1, -1};

        if (map[r][c] == 1){
            // 영역이면 영역 증가 처리
            tot += 1;

            // 방문처리
            map[r][c] = -1;

            // 4방향에 대해 재귀 호출

            for (int i = 0; i < 4; i++){
                int x = r + dx[i];
                int y = c + dy[i];

                if (x >= 0 && x < n && y >=0 && y < n ){
                    dfs(x, y);
                }
            }

        }
    }
}