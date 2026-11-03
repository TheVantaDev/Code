import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long m = sc.nextLong();
        long a = sc.nextLong();

        long ans = ((n + a - 1) / a) * ((m + a - 1) / a);

        System.out.println(ans);
    }
}