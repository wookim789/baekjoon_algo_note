package sort;
import java.util.*;

public class SwapArr {
    public static void main(String[]args){
        int n = 5;
        int k = 3;

        ArrayList<Integer> a = new ArrayList<>();
        ArrayList<Integer> b = new ArrayList<>();

        a.add(1);
        a.add(2);
        a.add(5);
        a.add(4);
        a.add(3);
        b.add(5);
        b.add(5);
        b.add(6);
        b.add(6);
        b.add(5);

        Collections.sort(a);
        Collections.reverse(b);

        for(int i = 0; i < k; i++){
            a.set(i, b.get(i));
        }
        int result = 0;
        for(int i = 0; i < n; i++){
            result += a.get(i);
        }
        System.out.println(result);
    }
}
