class Solution {
    public int repeatedNTimes(int[] nums) {
        int v[]=new int[10001];
        int n=nums.length/2;
        for(int i=0;i<nums.length;i++)
        {
            v[nums[i]]++;
        }
        for(int i=0;i<v.length;i++)
        {
            if(v[i]==n) return i;
        }
        return -1;
    }
    void main()
    {

    }
}