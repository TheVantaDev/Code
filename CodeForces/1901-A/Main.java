
import java.util.Scanner;

public class Main {
      public static void main( String []args){
        Scanner sc = new Scanner (System.in);
        int t = sc.nextInt();
        while(t -- > 0){
            // ani - an 
            int n = sc.nextInt();
            int x = sc.nextInt();
            int arr[] = new int [n];
            for(int i = 0 ; i < n ; i++){
                arr[i] = sc.nextInt();
            }
            int ans = 0  , prev = 0 ; 
            for(int i = 0 ; i < n ; i++){
                int a = arr[i];
                ans = Math.max(ans , a-prev);
                prev = a;
            }
            ans = Math.max(ans , 2 *(x-prev) );
            System.out.println(ans);
        }

      }   
}
