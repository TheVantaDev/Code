
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char arr[] = {'h', 'e', 'l', 'l', 'o'};
        int i = 0, j = 0;
        while (j < s.length() && i < arr.length) {
            if (arr[i] == s.charAt(j)) {
                i++;
                j++;
            } else {
                j++;
            }
        }
        if (i == arr.length) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

    }
}
