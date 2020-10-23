package nhn;

import java.util.*;
public class Vtest {
    private static int sizeOfMatrix, sectionTot, tmpSecCnt;
    private static int[][] matrix;
    private static boolean[][] visited;
    private static List<Integer> sectionCountArr;

    private static void solution(int sizeOfMatrixI, int[][] matrixI) {
        // TODO: 이곳에 코드를 작성하세요.
        sizeOfMatrix = sizeOfMatrixI;
        matrix = matrixI;
        visited = new boolean[sizeOfMatrix][sizeOfMatrix];
        sectionTot = 0;

        sectionCountArr = new ArrayList<>();

        for(int r = 0; r < sizeOfMatrix; r++){
            for(int c = 0; c < sizeOfMatrix; c++){
                tmpSecCnt = 0;
                dfs(r, c);
                if(tmpSecCnt != 0){
                    sectionCountArr.add(tmpSecCnt);
                    sectionTot++;
                }
            }
        }
        Collections.sort(sectionCountArr);
        System.out.println(sectionTot);
        for(int i : sectionCountArr){
            System.out.print(i + " ");
        }
    }
    private static void dfs(int r, int c){
        // 재귀 종료 조건
        if(visited[r][c]){
            return;
        }
        // 방문 처리
        visited[r][c] = true;

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0 , 1, 0, -1};

        // 영역 카운트 조건
        if(matrix[r][c] == 1){
            // 영역 수 카운트 조건
            tmpSecCnt++;
            for(int i = 0; i < 4; i++){
                int nextR = r + dx[i];
                int nextC = c + dy[i];
                // 재귀 호출
                if(0 <= nextR && nextR < sizeOfMatrix && 0 <= nextC && nextC < sizeOfMatrix){
                    dfs(nextR, nextC);
                }
            }
        }
    }

    private static class InputData {
        int sizeOfMatrix;
        int[][] matrix;
    }

    private static InputData processStdin() {
        InputData inputData = new InputData();

        try (Scanner scanner = new Scanner(System.in)) {
            inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

            inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
            for (int i = 0; i < inputData.sizeOfMatrix; i++) {
                String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
                for (int j = 0; j < inputData.sizeOfMatrix; j++) {
                    inputData.matrix[i][j] = Integer.parseInt(buf[j]);
                }
            }
        } catch (Exception e) {
            throw e;
        }

        return inputData;
    }

    public static void main(String[] args) throws Exception {
        InputData inputData = processStdin();

        solution(inputData.sizeOfMatrix, inputData.matrix);
    }
}
