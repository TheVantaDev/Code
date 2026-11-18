
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String arr[] = s.split("WUB");
        StringBuilder sb = new StringBuilder();
        for (String x : arr) {
            if (!x.equals(" ")) {
                if (sb.length() > 0) {
                    sb.append(" ");
                }
                sb.append(x);
            }
        }
        System.out.println(sb);
    }
}
