package data;

import java.util.*;

public class StackSample{
    public void stack(){
        Stack<Integer> st = new Stack<Integer>();

        st.push(1);
        st.push(2);
        st.push(3);
        st.push(4);
        st.push(5);
        
        // peek은 읽기
        int idx = 0;
        while(idx < 5){
            System.out.println(st.peek());
            idx += 1;
        }
        // pop은 읽은 후 제거
        while(!st.empty()){
            System.out.println(st.peek());
            st.pop();
        }
    }
}