import java.util.HashMap;
import java.util.Scanner;

public class Main {
      public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          int t = sc.nextInt();
        //   final int freqN = 200000;
          while(t-- > 0) {
            int n = sc.nextInt();
            int ans = -1;
              HashMap <Integer , Integer> mp = new HashMap <>();
              for(int i = 0 ; i < n ;i++) {
                  int x = sc.nextInt();
                  mp.put(x , mp.getOrDefault(x , 0)+1);
                  if(mp.get(x) >= 3) ans = x;
                  
              }
              System.out.println(ans);
        }
      }
}
