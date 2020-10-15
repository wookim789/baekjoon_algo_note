// import java.util.Stack;

// public class StackSample{
//     public static void main(String args[]) {
//         Stack<Integer> st = new Stack<>();

//         st.push(1);
//         st.push(2);
//         st.push(3);
//         st.push(4);
//         st.push(5);

//         while(!st.empty()){
//             System.out.println(st.peek(););
//             st.pop();
//         }
//     }
// }

import java.util.Scanner;

class ContinuousIOx {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        for(int idx = 0; idx < n; idx++) {
            int tot = 0;
            String[] oList = sc.nextLine().split("X");
            for(String o : oList){
                int size = o.length();
                for(int sum_idx = 1; sum_idx <= size; sum_idx++){
                    tot += sum_idx;
                }
            }
            System.out.println(tot);
        }
        sc.close();
    }
}
