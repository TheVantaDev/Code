import java.util.Scanner;

public class Main {
    public static void main(String []args){
        Scanner sc = new Scanner (System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int cnt  = 0 ; 
        int arr [] = new int [n];
        for(int i = 0 ; i < n ;i++) {
            arr[i] = sc.nextInt();
        }
        int target  = arr [k-1];
        for(int i = 0 ; i < n ; i++) if(arr[i] >= target && arr[i] > 0) cnt++;
        System.out.println(cnt);
    }
}
