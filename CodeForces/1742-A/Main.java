
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int big = Math.max(a, Math.max(b, c));
            if (big == a) {
                if (b + c == a) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            } else if (big == b) {
                if (a + c == b) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            } else {
                if (b + a == c) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
    }
}
