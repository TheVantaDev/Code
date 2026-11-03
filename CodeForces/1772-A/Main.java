import java.util.Arrays;
import java.util.Scanner;

public class Main {
     public static void main(String []args){
        Scanner sc = new Scanner(System.in);
         char[] targetArray = "Timur".toCharArray();
        Arrays.sort(targetArray);
        String target = new String(targetArray);
        int t = sc.nextInt();
        while(t -- > 0) {
            int n = sc.nextInt();
            String s= sc.next();
            if (n != 5) {
                System.out.println("NO");
                continue;
            }

            // Sort the input string characters
            char[] sArray = s.toCharArray();
            Arrays.sort(sArray);
            String sortedS = new String(sArray);

            // Compare sorted strings
            if (sortedS.equals(target)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
     }    
}
