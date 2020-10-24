package nhn;

import java.util.*;

public class NhnTest2 {
    // [참고 도서] : 이것이 취업을 위한 코딩 테스트다
    private static void solution(){
//        for(String str : orderArr){
//            System.out.println(dfs(str));
//        }

    }
    public static void main(String[]args){
//        System.out.println(dfs("ab(cd)"));
//        System.out.println(dfs("2(ab)"));
//        System.out.println(dfs("r(gb)"));
//        System.out.println(dfs("3(g)"));
//        System.out.println(dfs("BRGRG"));
//        System.out.println(dfs("3(BR2(R))"));
//        System.out.println(dfs("B(RGB(RG))"));
        String a = dfs("1B2R3G");
        System.out.println(affterP(a));
    }
    private static String affterP(String str){
        for(int i = str.length()-1; i >= 0 ; i--){
            int gap = str.charAt(i) - '0';
            if(0 <= gap && gap < 10){
                String f = str.substring(0, i);
                String b = str.substring(i + 1, i + 2);
                String l = str.substring(i + 2);
                String tmp = "";
                for(int j = 0; j < gap; j++){
                    tmp += b;
                }
                str = f + tmp + l;
            }
        }
        return str;
    }
    private static String dfs(String str){
        if(str.indexOf("(") == -1){
            return str;
        }

        String result = "";
        int fIdx = str.indexOf("(");
        String f = str.substring(0, fIdx);
        String b = str.substring(fIdx + 1);
        b = dfs(b);
        b = b.replaceAll("\\)", "");
        result += f.substring(0, fIdx - 1);
//        System.out.println(result);
        int lastF = f.charAt(f.length()-1);
//        System.out.println(lastF);


        if( 0 <= lastF - '0' && lastF - '0' < 10){
            String tmp = b;
            for(int i = 0; i < lastF - '0' - 1; i++){
                b += tmp;
            }
            result += b;
        }else{
            String sum = Character.toString(lastF);
            String tmp = "";
            for(int bIdx = 0; bIdx < b.length(); bIdx++){
                if(b.charAt(bIdx) - ')' == 0){
                    break;
                }
                tmp += sum;
                tmp += Character.toString(b.charAt(bIdx));
//                System.out.println(tmp);
            }
            result += tmp;
        }
        return result;
    }
}
