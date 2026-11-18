
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void Main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int n = sc.nextInt();
        int arr[][] = new int[n][2];
        for (int i = 0; i < n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
        }
        // sort dragons by x
        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 0; i < n; i++) {
            int x = arr[i][0];
            int y = arr[i][1];
            if (s >= x) {
                s += y;
            } else {
                System.out.println("NO");
                break;
            }
        }
        System.out.println("YES");
    }
}
