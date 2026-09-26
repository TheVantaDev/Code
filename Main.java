import java.util.*;

public class Main {
    public static void main(String[] args) {
        // assume we have one array
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
       while(t-- > 0){
            int n = sc.nextInt();
            int arr[] = new int[n];
            for(int i = 0; i < n; i++){
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);
            f(arr);
            for(int i = 0; i < n; i++){
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }

    }
   static void f(int arr[]){
         int start = 0;
         int end = arr.length-1;
         while(start < end){
            int t = arr[start];
            arr[start] = arr[end];
            arr[end] = t;
            start++;
            end--;
         }
    }
}