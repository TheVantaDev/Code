public class coordination {
    public static long countpaths(int i,int j,int n,int m)
    {if(i==n||j==m)
        {
            return 0;
        }
        if (i==n-1&&j==m-1)
        {return 1;
        }
    //move downwards
    long downwards=countpaths(i +1, j, n, m);
    //move rights
    long right=countpaths(i, j+1, n, m);
    return downwards+right;
    }
    public static void main(String[] args) {
       int m=21;int n=21;
        long ans=countpaths(0, 0, n, m);
        System.out.println(ans);
    }
    
}
