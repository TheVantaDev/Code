import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int xSum = 0 , ySum = 0 , zSum = 0;
        while(n -- > 0){
            xSum += sc.nextInt();
            ySum += sc.nextInt();
            zSum += sc.nextInt();
        }
        if(xSum ==0 && ySum == 0 && zSum == 0) System.out.println("YES");
        else System.out.println("NO");
    }
}
