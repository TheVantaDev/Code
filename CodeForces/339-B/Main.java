import java.util.Scanner;

public class Main {
        public static void main(String []args) {
            Scanner sc = new Scanner (System.in);
            long n =sc.nextLong();
            long m = sc.nextLong();
            // int arr [] = new int [m];
            long curr = 1 , total = 0; 
            for(int i = 0 ; i < m ; i++) {
                long input = sc.nextLong();
                 if(input >= curr){
                     total += (input - curr);
                 }
                 else {
                     total += (input - curr + n);
                 }
                curr = input;
            }

            System.out.println(total);
        }    
}
