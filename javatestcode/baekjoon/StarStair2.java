import java.util.Scanner;

public class StarStair2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        sc.close();

        for(int i = 1; i <= n; i++){
            print(i,"*");
            print(n-i, " ");
            print(n-i, " ");
            print(i,"*");
            System.out.println();
        }
        for(int i = n-1; i > 0; i--){
            print(i,"*");
            print(n-i, " ");
            print(n-i, " ");
            print(i,"*");
            System.out.println();
        }
    }

    public static void print(int num, String str){
        for(int i = 0; i < num; i++){
            System.out.print(str);
        }
    }
}
