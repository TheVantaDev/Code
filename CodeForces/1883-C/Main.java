import java.util.*;

public class Main {
    static int factorsOf2(int x) {
        int cnt = 0;
        while (x % 2 == 0) {
            cnt++;
            x /= 2;
        }
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();

            int[] a = new int[n];

            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }

            int ans = Integer.MAX_VALUE;

            if (k == 2) {
                ans = 1;

                for (int x : a) {
                    if (x % 2 == 0) {
                        ans = 0;
                        break;
                    }
                }
            }

            else if (k == 3) {
                ans = Integer.MAX_VALUE;

                for (int x : a) {
                    ans = Math.min(ans, (3 - x % 3) % 3);
                }
            }

            else if (k == 5) {
                ans = Integer.MAX_VALUE;

                for (int x : a) {
                    ans = Math.min(ans, (5 - x % 5) % 5);
                }
            }

            else { // k == 4

                int twos = 0;

                for (int x : a) {
                    twos += factorsOf2(x);
                }

                if (twos >= 2) {
                    ans = 0;
                } else {

                    int makeMultipleOf4 = Integer.MAX_VALUE;

                    for (int x : a) {
                        makeMultipleOf4 =
                                Math.min(makeMultipleOf4,
                                         (4 - x % 4) % 4);
                    }

                    int even1 = Integer.MAX_VALUE;
                    int even2 = Integer.MAX_VALUE;

                    for (int x : a) {
                        int cost = x % 2;

                        if (cost < even1) {
                            even2 = even1;
                            even1 = cost;
                        } else if (cost < even2) {
                            even2 = cost;
                        }
                    }

                    int twoEvens = even1 + even2;

                    ans = Math.min(makeMultipleOf4, twoEvens);
                }
            }

            System.out.println(ans);
        }
    }
}