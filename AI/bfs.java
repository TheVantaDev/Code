 class bfs{
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
        int curr=0;
        int goal=4;
        while(curr!=goal)
        {
            visit[curr]=true;
            System.out.println("Node:"+curr);
            int next=-1;
            int min=Integer.MAX_VALUE;
            for(int i=0;i<N;i++)
            {
                if(cost[curr][i]!=0 && !visit[i])
                { if ( h[i] < min)
                {  min=h[i];
                   next=i;
                }
                
                                }
            }
            curr=next;
        }
        System.out.println("Goal:"+goal);
    }
}