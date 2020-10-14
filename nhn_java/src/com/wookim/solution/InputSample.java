package com.wookim.solution;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class InputSample {
    public void InputSampleMethod() throws IOException {

        // scanner에서 next, nextInt 등을 사용하면
        // 공백 이후로 데이터를 받고 종료된 후에
        // nextLine으로 꼭 버퍼를 초기화할것

        // 기본 입력
        Scanner sc = new Scanner(System.in);

        // 입력받은 모든 라인 저장
        System.out.println("문자 입력");
        String s1 = sc.nextLine();
        System.out.println(s1);

        // 숫자 입력 받기
        System.out.println("2개의 숫자 공백구분하여 입력");
        // 1 2
        int i1 = sc.nextInt();
        int i2 = sc.nextInt();
        // 버퍼 초기화
        sc.nextLine();
        System.out.println(i1 + i2);

        // 문자열에서 공백으로 구분하여 받기
        System.out.println("공백 구분된 문자열 입력");
        String [] arr = sc.nextLine().split(" ");
        System.out.println(arr);

        // 문자열에서 공백으로 구분하여 숫자 받기
        System.out.println("숫자 입력 입력");
        int n = sc.nextInt();
        System.out.println(n);
        // 버퍼 초기화
        sc.nextLine();

        System.out.println("공백 구분된 숫자 입력");
        String [] iStrArr = sc.nextLine().split(" ");
        int [] intArr = new int[n];

        for(int i = 0; i < n; i++){
            intArr[i] = Integer.parseInt(iStrArr[i]);
        }

        for(int i : intArr){
            System.out.println(i);
        }

        /**
         * scanner을 이용한 입력보다 buffred 계열을 사용하면 성능이 좋은 이유
         *
         * 스캐너를 이용해 입력을 받으면 입력받는 문자 하나하나를 즉시 전송함
         *
         * 버퍼는 이와 다르게 크기가 정해진 버퍼에 입력을 임시로 저장하고
         * 입력이 끝나거나 버퍼가 다 채워지면 입력을 보냄
         *
         * 이 차이로 인해 성능차이가 발생함
         * 즉시 데이터를 보내는 스캐너는 cpu와 하드의 입출력 처리 cpu와 하드간의 속도차에 의해 성능 저하가 발생
         *
         * 이 단점을 보완하여 데이터의 입력을 가능한 많이 받고
         * 한번만 전달하면 위 단점을 어느정도 보완한다고 함
         *
         */

//
//        // java의 빠른 입력 클래스
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        // 문자열을 입력받는 sample
//        String s = br.readLine();
//
//        // 입력을 받아 정수로 변환하는 sample
//        int n2 = Integer.parseInt(br.readLine());
//
//
//
//        // 공백문자로 구분된 문자열 배열로 변환하기
//        String [] strArray = br.readLine().split("");
//
//        // java의 빠른 출력 클래스
//        BufferedWriter bw = new BufferedWriter(new FileWriter("bufferedWriterTest.txt"));
//        bw.write("print like system.out.print()");
//        bw.newLine(); // "\n" 문자 역할
//
//        bw.write("print like system.out.print()\n");
    }
}
