class Solution {
    public long maxArrayValue(int[] nums) {
        long ans=nums[0];
        long curr=ans;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]<=nums[i+1])
            {
                curr=curr+nums[i];
            }
            else ans=curr;
        }
    return ans;
    }
}