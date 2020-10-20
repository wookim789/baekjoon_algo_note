package impl;


import java.util.*;
public class StringSort {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        sc.close();

        int tot = 0;
        List<String> result = new ArrayList<>();

        for(int i = 0; i < str.length(); i++){
            int aski = str.charAt(i) - '0';

            if(0 <= aski && aski <= 9){
                tot += aski;
            }else{
                result.add(Character.toString(str.charAt(i)));
            }
        }
        Collections.sort(result);
        for(String s : result){
            System.out.print(s);
        }
        System.out.println(Integer.toString(tot));
    }
}

