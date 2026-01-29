import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> l=new ArrayList<>();



        back(nums,0,l);
        Set<List<Integer>> s=new HashSet<>(l);
        List<List<Integer>> l1=new ArrayList<>(s);

        
        return l1;

    }
    void back(int arr[],int start,List<List<Integer>> l)
    {  if(start==arr.length)
    {
        l.add(arraytolist(arr));
        return;
    }
    for(int i=start;i<arr.length;i++)
    {  swap(arr, start, i);
        back(arr, start+1, l);
        swap(arr, start, i);

     

        }    }
    List<Integer> arraytolist(int arr[])
    { List<Integer> l=new ArrayList<Integer>();
        for(int i:arr) l.get(i);
        return l; 

    }
    void swap(int nums[],int i,int j)
    {
        int temp=nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
    }
}