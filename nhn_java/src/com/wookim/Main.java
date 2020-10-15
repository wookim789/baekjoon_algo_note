package src.com.wookim;

import src.com.wookim.solution.InputSample;

import java.io.IOException;

public class Main {

    public static void main(String[] args) {
	// write your code here
        InputSample input = new InputSample();
        try{
            input.InputSampleMethod();
        }catch (IOException e){
            e.printStackTrace();
        }

    }
}
