import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        // distinct means no same means yes
        while(t-- > 0){
        int n = sc.nextInt();
        int arr [] = new int[n];
        for(int i =0 ;i < n;i++){
            arr[i] = sc.nextInt();
        }
            Set <Integer> s = new HashSet<>();
              for(int i =0 ;i < n;i++){
                s.add(arr[i]);
              }
            if(s.size() == n) {
            System.out.println("NO");
        }
        else {
            System.out.println("YES");
        }

        }
        
    }
}
