
import java.util.Scanner;


public class Main {
      public static void main(String []args) {
         Scanner scanner = new Scanner(System.in);
        
        if (!scanner.hasNextInt()) return;
        int n = scanner.nextInt();
        int solvedCount = 0;
        
        for (int i = 0; i < n; i++) {
            int petya = scanner.nextInt();
            int vasya = scanner.nextInt();
            int tonya = scanner.nextInt();
            
            if (petya + vasya + tonya >= 2) {
                solvedCount++;
            }
        }
        
        System.out.println(solvedCount);
        scanner.close();
      }    
}
