class Solution {
    public int reverseBits(int n) {
        StringBuilder sb=new StringBuilder();
        int temp=n;
        while(temp>0)
        { int rem=temp%2;
            sb.append(rem);
            temp=temp/2;
        }
        String s = sb.reverse().toString();
 while (s.length() < 32) {
            s = "0" + s;
        }
       String reverse=new StringBuilder(s).reverse().toString();
       int num=(int) Long.parseLong(s);
        return num;
    }
}