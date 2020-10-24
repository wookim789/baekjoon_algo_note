package nhn;

import java.util.*;
public class NhnTest1 {
    // [참고 도서] : 이것이 취업을 위한 코딩 테스트다
    private static void solution(int day, int width, int[][] blocks){

        int tot = 0;
        int[] widthArr = new int[day];
        for(int d = 0; d < day; d++){
            for(int w = 0; w < width; w++){
                widthArr[w] += blocks[d][w];
            }

            // 왼쪽 기둥 설정
            int left = widthArr[0];
            int lIdx = 0;
            int right = 0;
            for(int b = 1; b < widthArr.length; b++){

                if(left > widthArr[b]){
                    right = widthArr[b];
                }else if(b < widthArr.length - 1){
                    for(int k = lIdx + 1; k < b; k++){
                        int gap = (left - widthArr[k]);
                        tot += gap;
                        widthArr[b] += gap;
                    }
                    left = widthArr[b];
                    lIdx = b;
                }
            }
        }


    }
}

