
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Main {
    public static int log2(int x) {
    if (x <= 0) {
        throw new IllegalArgumentException("Input must be greater than 0");
    }
    return 31 - Integer.numberOfLeadingZeros(x);
}

    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        // first bit of a number we cant change that 
        // Argument is x should equal to == 2 power MSB
        // most signgificant bit we have to calculate.
        while(t-- > 0) {
            int n = sc.nextInt();
            n--;
            // int a = sc.nextInt();
            int msb = log2(n);
            int num =(int) Math.pow(2 , msb)  - 1;
            List <Integer> l = new ArrayList<>();
            while(num >= 0){
                  l.add(num);
                  num--;
            }
            num = (int ) Math.pow(2, msb);
            while(num <= n) {
                l.add(num);
                num++;
            }

          for(int i : l){
            System.out.println(i + " ");
          }

        }
    }
}
