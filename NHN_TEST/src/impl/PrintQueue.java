package impl;
import java.util.*;

public class PrintQueue {
//class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int tc = sc.nextInt();
        sc.nextLine();

        for (int t = 0; t < tc; t++) {
            // 반복 지점
            int n = sc.nextInt();
            int m = sc.nextInt();

            sc.nextLine();

            Deque<HashMap<Integer, Integer>> deque = new ArrayDeque<>();
            ArrayList<Integer> maxArr = new ArrayList<>();
            for (int idx = 0; idx < n; idx++) {

                int data = sc.nextInt();
                maxArr.add(data);

                HashMap<Integer, Integer> map = new HashMap<>();
                map.put(idx, data);
                deque.add(map);
            }
            Collections.sort(maxArr, Collections.reverseOrder());
            boolean isPopMax = true;
            int max = 0;
            for (int i = 0; i < n; i++) {
                if (isPopMax) {
                    max = maxArr.get(0);
                    maxArr.remove(0);
                    isPopMax = false;
                }

                HashMap<Integer, Integer> mapData = deque.pollFirst();

                if (!mapData.containsValue(max)) {
                    deque.offerLast(mapData);
                    i--;
                } else if (mapData.containsKey(m)) {
                    System.out.println(i + 1);
                    break;
                } else {
                    isPopMax = true;
                }
            }
        }
        sc.close();
    }
}


// 1 2 9 3 4 5

// 9
// 2
// 3
// 4
// 5
// 1