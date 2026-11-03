import java.util.*;
public class Main{
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            int n = sc.nextInt();
            int m = sc.nextInt();
            String x = sc.next();
            String s = sc.next();
           int cnt = -1;
            for (int p = 0; p <= 6; p++) {
                if (x.contains(s)) {
                    cnt = p;
                    break;
                }
                x += x; // Double the string x
            }
            
            System.out.println(cnt);
        }
        sc.close();

            
            
        }
    }
   
