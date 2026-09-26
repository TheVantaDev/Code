import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int d = sc.nextInt();
        int arr[] = new int [n];
        for(int i =0 ;i < n;i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        int l = -1 , r = n-1;
        int cnt = 1;
        int team = 0;
        while(l < r){
                 if(arr[r]*cnt <= d && l < r){
                    l++;
                    cnt++;
                 }
                 else{
                    team++;
                    cnt =1;
                    r--;
                 }
        }
        System.out.println(team);
    }
}
