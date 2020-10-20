package data;

import java.util.*;
public class AdjacencyMatrix {
    public void inputMatrix(){

        Scanner sc = new Scanner(System.in);
        System.out.println("start");
        int m = sc.nextInt();
        int n = sc.nextInt();
        sc.nextLine();

        int [][] adjMatrix = new int[m][n];
        for(int r = 0; r < m; r++){
            for(int c = 0; c < n; c++){
                adjMatrix[r][c] = sc.nextInt();
            }
            sc.nextLine();
        }

        for(int r = 0; r < m; r++){
            for(int c = 0; c < n; c++){
                System.out.print(adjMatrix[r][c] + " ");
            }
            System.out.println();
        }
    }
}
