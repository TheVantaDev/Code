import java.util.Scanner;

public class Main {
       public static void main(String []args){
          Scanner sc = new Scanner(System.in);
          int t = sc.nextInt();
          while(t-- > 0) {
            int  n = sc.nextInt();
            int k = sc.nextInt();
            String s = sc.next();
            int K = k;
            // if n is odd then one odd is allowed
            // if n is even then all character should be even
            int freq[] = new int [26];
            for (char ch : s.toCharArray()) {
                freq[ch-'a']++;
            }
              int odd = 0 ;
              for(int i : freq){
                if(i %2 != 0) odd++;
              }
              if(odd <= k+1) System.out.println("YEs");
              else System.out.println("No");

          }
       }  
}
