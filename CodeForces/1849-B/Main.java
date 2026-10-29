import java.util.*;
public class Main {
      public static void main(String[] args) {
        // cut down array constraint to 1 to k and after that let's move this elements higher element possible the choise 
        // so work on that and if tie use indexes

          Scanner sc = new Scanner(System.in);
          int t = sc.nextInt();
          while(t-- > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int arr[] = new int [n];
            for(int i = 0 ; i < n;i++) {
                arr[i] = sc.nextInt();
            } 
            List<int[]> list = new ArrayList<>();
            for(int i = 0; i < n; i++) {
                int rem = arr[i] % k;
                list.add(new int[]{rem, i});
            }

            // custom sort
            list.sort((a, b) -> {
                // remainder 0 comes first
                if (a[0] == 0 && b[0] != 0) return -1;
                if (b[0] == 0 && a[0] != 0) return 1;

                // sort by remainder descending
                if (a[0] != b[0]) return Integer.compare(b[0], a[0]);

                // tie-breaker: smaller index first
                return Integer.compare(a[1], b[1]);
            });

            // print indices +1 (since problem expects 1-based)
            for (int[] pair : list) {
                System.out.print((pair[1] + 1) + " ");
            }
            System.out.println();


          }
      }    
}
