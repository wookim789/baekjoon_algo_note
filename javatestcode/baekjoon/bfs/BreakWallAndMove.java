package bfs;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class BreakWallAndMove {
//class Main {
    private static int[][]map;
    private static int n, m;
    public static void main(String[] args) throws IOException, Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] size = br.readLine().split(" ");
        n = Integer.parseInt(size[0]);
        m = Integer.parseInt(size[1]);
        map = new int[n][m];

        for(int row = 0; row < n; row++){
            String[] rowMap = br.readLine().split("");
            for(int col = 0; col < m; col++){
                map[row][col] = Integer.parseInt(rowMap[col]);
            }
        }
        br.close();
        System.out.println(bfs());
    }
    private static int bfs(){
        Queue<Integer[]> nextQue = new LinkedList<>();
        nextQue.add(new Integer[]{0, 0, 0, 1}); //[0]x, [1]y,  [2]0: 안부셨음, 1: 부셨음
//        bollean [][][] hasBeen = new bollean[2][n][m];

        while(!nextQue.isEmpty()){
            Integer[] curPoint = nextQue.poll();

            int row = curPoint[0];
            int col = curPoint[1];
            int isBreak = curPoint[2];
            int result = curPoint[3];
            String point = Integer.toString(row) + "." + Integer.toString(col);
//            hasBeen.put(point, "1");
            System.out.println(point);
            if(row == n-1 && col == m-1){
                return result;
            }

            int[] dx = {1, 0, -1, 0};
            int[] dy = {0, 1, 0, -1};

            for(int dir = 0; dir < 4; dir++){
                int nextRow = row + dx[dir];
                int nextCol = col + dy[dir];
                String nextPoint = Integer.toString(nextRow) + "." + Integer.toString(nextCol);
//                if(0 <= nextRow && nextRow < n && 0 <= nextCol && nextCol < m && !hasBeen.containsKey(nextPoint)){
//                    if(map[nextRow][nextCol] == 0){
//                        nextQue.add(new Integer[]{nextRow, nextCol, isBreak, result + 1});
////                        hasBeen.put(nextPoint, "1");
//                    }else if(isBreak == 0){
//                        isBreak = 1;
//                        nextQue.add(new Integer[]{nextRow, nextCol, isBreak, result + 1});
////                        hasBeen.put(nextPoint, "1");
//                    }
//                }
            }
        }
        return -1;
    }
}

