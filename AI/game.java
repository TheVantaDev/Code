

public class game {
   static int minimax(int currdepth, boolean isMax, int scores[], 
                       int currnodeIndex, int h)
   {if(currdepth==h) return scores[currnodeIndex];
    if(isMax)
    { return Math.max(
        minimax(currdepth+1, false, scores, currnodeIndex*2, h),
        minimax(currdepth+1, false, scores, currnodeIndex*2+1, h)
    );
}
   else{
    return Math.min(
        minimax(currdepth+1, true, scores, currnodeIndex*2, h),
        minimax(currdepth+1, true, scores, currnodeIndex*2+1, h)
    );
   }
   }
   static int calculate(int n)
   {
            return (n==1) ? 0 : 1 + calculate(n/2);

   }
    public static void main(String[] args) {
        int scores[]={1, 1, 2, -3, 5, 7, -2, -4};
        int n=scores.length;
        int h=calculate(n/2);
        int ans=minimax(0, false, scores, 0, h);
        System.out.println("The optimal Value is :"+ans);

    }
}
