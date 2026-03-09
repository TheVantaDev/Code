public class Solution {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}import java.util.Arrays;

class Skiplist {
class Node{
    int val;
    Node[] forward;
    int key;
    Node (int level,int key)
    { this.val=1;
      this.key=key;
      forward=new Node[level];
    }

}
Node head;
int currlevel;
    public Skiplist() {
        head=new Node(16,-1);
        Arrays.fill(head.forward,new Node(0,Integer.MAX_VALUE));
        currlevel=1;
    }
    
    public boolean search(int target) {
        Node temp=head;
       for(int i=currlevel-1;i>=0;i--)
       {
         while(temp.forward[i].key<target) temp=temp.forward[i];
       }
       return temp.forward[0].key==target;
    }
    Node [] predecessors(int target)
    { Node v[]=new Node [16];
       Node temp=head;
      for(int i=currlevel-1;i>=0;i--)
      {
        while(temp.forward[i].val < target) temp=temp.forward[i];
        v[i]=temp;
      }
        return v;
    }
    int randomlevel()
    {
        int level=1;
        while(Math.random()<0.5 && level < Math.min(16,currlevel+1))
        {
            level++;
        }
        return level;
    }
    
    public void add(int num) {
        Node[] v=predecessors(num);
        Node temp=v[0].forward[0];
        if(temp.key==num)
        {
            ++temp.val;
        }
        else{
            int level=randomlevel();
            if(level>currlevel)
            {
                for(int i=currlevel-1;i<level;++i)
                { v[i]=head;
                }
                currlevel=level;
            }
            temp=new Node (level,num);
            for(int i=0;i<level;++i)
            {
                temp.forward[i]=v[i].forward[i];
                v[i].forward[i]=temp;
            }
        }

    }
    
    public boolean erase(int num) {
         Node[] update = predecessors(num);
        Node cur = update[0].forward[0];
        if (cur.key != num) {
            return false;
        } else {
            if (cur.val > 1) {
                --cur.val;
            } else {
                for (int i = 0; i < currlevel; ++i) {
                    if (update[i].forward[i] != cur) {
                        break;
                    }
                    update[i].forward[i] = cur.forward[i];
                }
                while (currlevel > 1 && header.forward[currlevel - 1] == new Node(0,Integer.MAX_VALUE)) ;{
                    --currlevel;
                }
            }
            return true;
    }
}
}
/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * boolean param_1 = obj.search(target);
 * obj.add(num);
 * boolean param_3 = obj.erase(num);
 */