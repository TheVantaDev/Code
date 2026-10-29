import java.util.Scanner;

public class Main{
    public static void main(String []args){
        Scanner sc = new Scanner (System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            int n = sc.nextInt();
            int k = sc.nextInt();
            int q = sc.nextInt();
            int arr [] = new int [n];
            for(int i = 0 ;i < n ;i++){
                arr[i] = sc.nextInt();
            }
            int cnt = 0;
            long ans = 0;
            // arr [i] is greater than q then reset it cnt to zero
            for(int i = 0 ; i < n ;i++) {
               if (arr[i] <= q) {
                    cnt++;
                    if (cnt >= k) {
                        ans += cnt - k + 1;
                    }
                } else {
                    cnt = 0;
                }
            }
            System.out.println(ans);
        }
    }
}