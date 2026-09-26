import java.util.Scanner;

public class Main {

   static   boolean f(long n){
        long num = n;
        while(num > 0){
            long x = num % 10 ;
            if(x != 0 && n % x != 0) return false;
            num = num /10;
        }
        return true;
    }
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int t  = sc.nextInt();
        while(t-- > 0){
            long n = sc.nextLong();
            while(!f(n)){
                
                 n +=1;
            }
            System.out.println(n);

        }
    }
}
