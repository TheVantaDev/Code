import java.util.Arrays;
import java.util.Scanner;

public class Main {
   boolean f(int arr[]) {
        for(int i =1 ; i < arr.length ; i++) {
            if(arr[i] - arr[i-1] > 1) return false;
        }
        return true;
    }
    public static void main(String []args) {
        Scanner sc = new Scanner (System.in);
        int t = sc.nextInt();
        while(t-- > 0) {
            int  n = sc.nextInt();
            int arr [] = new int [n];
            for(int i = 0 ; i < n ; i++) {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);
            Main m = new Main();
            if(m.f(arr)){
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
        }
        
    }
}
