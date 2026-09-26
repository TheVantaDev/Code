import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- >0){
            int n = sc.nextInt();
            int k = sc.nextInt();
            String s = sc.next();
            int prefix [] = new int[n+1];
            int sum = 0;
            for(int i =0;i < n;i++){
                if(s.charAt(i)=='W') sum++;
                prefix[i+1] = sum;
            }
            int min = Integer.MAX_VALUE;
            for(int i =0 ; i+k<=n;i++ ){
                min = Math.min(min , prefix[i+k] - prefix[i]);
            }
            if(min == Integer.MAX_VALUE) min = 0;
            System.out.println(min);
        }
    }
}
