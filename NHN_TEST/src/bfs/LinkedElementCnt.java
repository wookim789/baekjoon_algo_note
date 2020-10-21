package bfs;
import java.util.*;

class Main {
    private static int n, m, cnt;
    private static boolean[] visited;
    private static ArrayList<ArrayList<Integer>> list;

    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        cnt = 0;
        sc.nextLine();
        visited = new boolean[n+1];
        list = new ArrayList<>();
        for(int i = 0; i < n + 1; i++){
            list.add(new ArrayList<>());
        }

        for(int i = 1; i < m + 1; i ++){
            int node = sc.nextInt();
            int ele = sc.nextInt();
            sc.nextLine();

            ArrayList<Integer> arrF = list.get(node);
            ArrayList<Integer> arrB = list.get(ele);
            arrF.add(ele);
            arrB.add(node);
        }

        for(int i = 1; i < n + 1; i++){
            Collections.sort(list.get(i));
        }
        for(int i = 1; i < n + 1; i++){
            bfs(i);
        }
        System.out.println(cnt);
    }
    private static void bfs(int node){

        if(visited[node]){
            return;
        }
        visited[node] = true;
        Queue<Integer> que = new LinkedList<>();

        for(int n_node : list.get(node)){
            que.offer(n_node);
        }

        while (!que.isEmpty()){
            int c_node = que.poll();
            if(visited[c_node]){
                continue;
            }

            visited[c_node] = true;
            for (int n_node : list.get(c_node)){
                que.offer(n_node);
            }
        }
        cnt++;
    }

}
