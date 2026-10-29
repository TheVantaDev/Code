import java.util.Scanner;

public class Main{
    public static void main(String []args){
          Scanner sc = new Scanner (System.in);
          int t = sc.nextInt();
          while(t-- > 0){
             int n = sc.nextInt();
             int a [] = new int [n];
             int b [] = new int [n];
             for(int i = 0 ;i < n;i++) a[i] = sc.nextInt();
             for(int i = 0; i < n;i++) b[i] = sc.nextInt();
             int[] x = new int[2 * n + 1];
            int[] y = new int[2 * n + 1];

            int cnt = 1;

            for (int i = 1; i < n; i++) {
                if (a[i] == a[i - 1]) {
                    cnt++;
                } else {
                    x[a[i - 1]] = Math.max(x[a[i - 1]], cnt);
                    cnt = 1;
                }
            }
            x[a[n - 1]] = Math.max(x[a[n - 1]], cnt);

            cnt = 1;

            for (int i = 1; i < n; i++) {
                if (b[i] == b[i - 1]) {
                    cnt++;
                } else {
                    y[b[i - 1]] = Math.max(y[b[i - 1]], cnt);
                    cnt = 1;
                }
            }
            y[b[n - 1]] = Math.max(y[b[n - 1]], cnt);

            int ans = 0;

            for (int i = 1; i <= 2 * n; i++) {
                ans = Math.max(ans, x[i] + y[i]);
            }

            System.out.println(ans);
        }

        sc.close();
    
    }
}