
import java.util.Scanner;


public class lab1 {
    static  void f(int a[][] , int b[][] , int n){
            int ans [][] = new int [n][n];
            for(int i = 0 ;i<n;i++){
                for(int j = 0;j<n;j++){
                    for(int k = 0; k<n;k++){
                       ans[i][j] += a[i][k]*b[k][j];
                    }
                }
            }
            System.out.println("Product of two matrix looks like ");
               for(int i = 0 ;i<n;i++){
                for(int j = 0;j<n;j++){
                    System.out.print(ans[i][j]+ " ");
                }
                System.out.println();
            }
      }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // printArray(arr);
        System.out.println("Which order do you prefer");
        int n = sc.nextInt();
        int a [][] = new int [n][n];
        int b [] [] = new int [n][n];
        System.out.println("Enter value of A matrix ");
        for(int i = 0 ;i<n;i++){
            for(int j =0 ;j<n ;j++){
                 a[i][j] = sc.nextInt();
            }
        }
        System.out.println("Enter value of B matrix ");
        for(int i = 0 ;i<n;i++){
            for(int j =0 ;j<n ;j++){
                 b[i][j] = sc.nextInt();
            }
        }
        f(a , b , n);
        System.out.println("Hi");
    }
}
