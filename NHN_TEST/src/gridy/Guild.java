package gridy;
import java.util.*;

public class Guild {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int [] fearList = new int[n];

        for(int i = 0; i < n; i++){
            fearList[i] = sc.nextInt();
        }

        // 공포도가 낮은 사람 부터 그룹핑
        int result = 0;
        Arrays.sort(fearList);
        int minFear = fearList[0];
        int tmp = 0;
        for(int i = 0; i < fearList.length; i++){
            tmp++;
            if(tmp >= i){
                tmp = 0;
                result ++;
                minFear = fearList[i];
            }
        }
        System.out.println(result);
    }
}
