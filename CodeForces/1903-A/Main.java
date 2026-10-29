import java.util.Scanner;

public class Main {
    public static void main(String []args) {
        Scanner sc = new Scanner (System.in);
        int t = sc.nextInt();
        while(t-- > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int arr [] = new int [n];
            for(int i = 0 ; i < n ; i++) {
                arr[i] = sc.nextInt();
            }
             if(f(arr) || k >= 2) System.out.println("YES");
            else System.out.println("NO");
        }
    }    
   static boolean f(int arr[]) {
        int n = arr.length;
        for(int i = 1 ; i < n ; i++){
            if(arr[i-1] > arr[i]) return false;
        }
        return true;
    }
}
