
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int mat[][] = new int[n][2];
        for (int i = 0; i < n; i++) {
            mat[i][0] = sc.nextInt();
            mat[i][1] = sc.nextInt();
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {          // host team
            for (int j = 0; j < n; j++) {      // guest team
                if (i != j && mat[i][0] == mat[j][1]) {
                    ans++;
                }
            }
        }

        System.out.println(ans);

    }
}
