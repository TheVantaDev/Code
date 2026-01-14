import java.util.LinkedList;
import java.util.List;

class Solution {
    public static int minimumPairRemoval(int[] nums) {
        List <Integer> l=new LinkedList<Integer>();
        int cnt=0;
        while(!issorted(l))
        {  int idx=0;
            // int sum=0;
            for(int i=0;i<l.size()-1;i++)
            {
              int sum=l.get(i)+l.get(i+1);
              if(sum<l.get(i))
              {
                l.set(i, sum);
                cnt++;
              }
                
            }
        


        }
         return cnt;
    }
   static boolean issorted(List <Integer> l)
        { 
            for(int i=1;i<l.size();i++)
            {
                if(l.get(i)<l.get(i-1)) return false;
            }
            return true;
        }
    void main()
    { System.out.println(minimumPairRemoval(new int[]{5,2,3,1}));

    }
}