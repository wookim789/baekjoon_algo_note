import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//public class Fibonachi {
class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        List<Integer> fibo = new ArrayList<Integer>();

        fibo.add(0);
        fibo.add(1);

        for(int idx = 2; idx < n + 1; idx++){
            int tmp = fibo.get(idx - 1) + fibo.get(idx - 2);
            fibo.add(tmp);
        }
        System.out.println(fibo.get(fibo.size()-1));
    }
}

