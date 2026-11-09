
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // maximum non decreasing
        int ans = 1;
        int cnt = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i - 1] <= arr[i]) {
                cnt++;
                ans = Math.max(ans, cnt);

            } else {
                cnt = 1;
            }
        }
        System.out.println(ans);
    }
}
