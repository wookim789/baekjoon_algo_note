import java.util.Scanner;

public class StarStair {
//class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        sc.close();

        for(int i = 1; i < n + 1; i++){
            print(n - i, " ");
            print(2 * i - 1, "*");
        }
        for(int i = n - 1; i > 0; i--){
            print(n - i, " ");
            print(2 * i - 1, "*");
        }
    }

    private static void print(int num, String str){
        for(int i = 0; i < num; i++){
            System.out.print(str);
        }
        if(str.equals("*")){
            System.out.println();
        }
    }
}
