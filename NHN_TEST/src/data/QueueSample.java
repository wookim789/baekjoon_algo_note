package data;

import java.util.*;
public class QueueSample {
    public void queue(){
        Queue<Integer> que = new LinkedList<>();

        que.offer(1);
        que.offer(2);
        que.offer(3);
        que.offer(4);
        que.offer(5);

        while(!que.isEmpty()){
            System.out.println(que.poll());
        }
    }
}
