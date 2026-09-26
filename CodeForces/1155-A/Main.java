
import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        // #1 string should not be same
        // #2 ascending order is not make any sense
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // for(int i=0;i<n;i++){
        //     c[i] = sc.next().charAt(0);
        // }
        String s = sc.next();
        char c[] = s.toCharArray();
        boolean flag = false;
       for(int i =0 ;i < n-1;i++){
          if(c[i] > c[i+1]){
             System.out.println("YES");
             System.out.println((i+1) + " " + (i+2));
             flag = true;
             break;
          }
       }
       if(!flag) System.out.println("NO");
    }
}