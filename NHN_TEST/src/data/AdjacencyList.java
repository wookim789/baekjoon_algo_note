package data;

import java.util.*;
public class AdjacencyList {
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);

        int node = sc.nextInt();
        sc.nextLine();

        List<ArrayList<Integer>> adjacencyList = new ArrayList<ArrayList<Integer>>();

        for(int n = 0; n < node; n++){
            String[] tmp_list = sc.nextLine().split(" ");
            ArrayList<Integer> tmp_link_list = new ArrayList<>();

            for(String tmp : tmp_list){
                tmp_link_list.add(Integer.parseInt(tmp));
            }
            adjacencyList.add(tmp_link_list);
        }

        for(ArrayList<Integer> links : adjacencyList){
            for(int link : links){
                System.out.print(link + " ");
            }
            System.out.println();
        }
    }
}
