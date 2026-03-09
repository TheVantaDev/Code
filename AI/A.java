package AI;

 class A {
    static int N=5;
static int h[] = {7, 6, 2, 1, 0};   // Heuristic values
static int cost[][] = {
    {0, 1, 4, 0, 0},
    {1, 0, 2, 5, 0},
    {4, 2, 0, 1, 3},
    {0, 5, 1, 0, 2},
    {0, 0, 3, 2, 0}
};
  public static void main(String[]args)
    {  boolean visit[]=new boolean[N];
       int f[]=new int[N];
       int g[]=new int[N];
       for(int i=0;i<N;i++)
       {
         f[i]=Integer.MAX_VALUE;
         g[i]=Integer.MAX_VALUE;
       }
    int start=0,goal=0,curr=start;

       g[start]=0;
       f[start]=h[start];
       while(curr!=goal)
       { visit[curr]=true; 
        System.out.println("Node:"+curr);
        int next=-1,min=Integer.MAX_VALUE;
        for(int i=0;i<N;i++)
        {
            if(cost[curr][i]!=0 && !visit[i])
            {
                int t=g[curr]+cost[curr][i];
                int a=t+h[i];
                if(a<min)
                {
                    min=a;
                    next=i;
                   g[i]=t;
                   f[i]=a;

                }
            }
        }
        curr=next;
       }
       System.out.println("Goa"+goal);

    }
}
