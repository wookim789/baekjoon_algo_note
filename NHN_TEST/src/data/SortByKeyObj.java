package data;

import java.util.*;

public class SortByKeyObj {
    public static void main(String[]args){
        List<SortedObj> list = new ArrayList<>();
        list.add(new SortedObj(4, "이"));
        list.add(new SortedObj(1, "김"));
        list.add(new SortedObj(3, "박"));
        list.add(new SortedObj(2, "나"));

        Collections.sort(list);

        for(int i = 0; i < list.size(); i++){
            System.out.println(list.get(i).getName());
        }
    }
}

class SortedObj implements Comparable<SortedObj>{
    int cnt;
    String name;

    public SortedObj(int cnt, String name){
        this.cnt = cnt;
        this.name = name;
    }

    public int getCnt() {
        return cnt;
    }

    public String getName() {
        return name;
    }

    @Override
    public int compareTo(SortedObj other) {
        if(this.cnt < other.cnt){
            return -1;
        }
        return 1;
    }
}
