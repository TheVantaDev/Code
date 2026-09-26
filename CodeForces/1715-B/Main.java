import java.util.Scanner;

public class Main {
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            long n = sc.nextLong();
            long k = sc.nextLong();
            long b = sc.nextLong();
            long s = sc.nextLong();
            if(b * k <= s && s <= (k*b) + n*(k-1)) 
            {
                
                long arr [] = new long [(int) n];
                arr[0] = k * b;
                s -= k*b;
                for(int i = 0;i < n;i++){
                    long add = Math.min(k-1, s);
                    arr[i] += add;
                    s -= add;
                }
               
                for(int i = 0;i < n;i++){
                    System.out.print(arr[i]+" ");
                }
            }
            else System.out.println(-1);
            


        }
    }

}
