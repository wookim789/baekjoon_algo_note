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
