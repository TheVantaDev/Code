class Solution {
    public int numPrimeArrangements(int n) {
        int p = 0;
      for (int i = 1; i <= n; i++) {
    int cnt = 0;

    for (int j = 1; j <= i; j++) {
        if (i % j == 0) {
            cnt++;
        }
        if(cnt==2) p++;
    }


        
    
}
return facto(p)*facto(n-p) ;
    }
 int facto(int n)
 {
    if(n <=1) return 1;
    return n*facto(n-1);
 }

}