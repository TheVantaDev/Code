import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while (t-- > 0) {
            int n = sc.nextInt(); // number of arrays
            int[][] matrix = new int[n][];
            
            for (int i = 0; i < n; i++) {
                int m = sc.nextInt(); // size of each array
                matrix[i] = new int[m];
                
                for (int j = 0; j < m; j++) {
                    matrix[i][j] = sc.nextInt();
                }
                Arrays.sort(matrix[i]);
            }
            
            // Find smallest second element
            int small = Integer.MAX_VALUE;
            int idx = 0;
            for (int i = 0; i < n; i++) {
                if (matrix[i].length > 1 && matrix[i][1] < small) {
                    small = matrix[i][1];
                    idx = i;
                }
            }
            
            int[] arr = new int[n - 1];
            int index = 0;
            int compare = 0;
            int sum = 0;
            
            for (int i = 0; i < n; i++) {
                if (i == idx) {
                    compare = matrix[i][0];
                    continue;
                }
                arr[index++] = matrix[i][0];
                if (matrix[i].length > 1) sum += matrix[i][1];
            }
            
            Arrays.sort(arr);
            sum += Math.min(compare, arr[0]);
            
            System.out.println(sum);
        }
    }
}
