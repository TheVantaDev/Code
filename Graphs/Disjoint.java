 class Disjoint{
    int rank [] , parent [];
    public Disjoint(int n ){
         rank = new int [n+1];
         parent = new int [n+1];
         for(int i = 0 ;i<=n;i++){
            parent[i] = i;
         }
    }
    int findParent(int node){
        if(node == parent[node]){
            return node;
        }
        return parent[node] = findParent(parent[node]);
    }
    void union_bank(int u , int v){
        int ult_u = findParent(u);
        int ult_v= findParent(v);
        if(ult_u==ult_v) return ;
        if(rank[ult_u] < rank[ult_v]){
            parent[ult_u] = ult_v;
        }
        else if(rank[ult_v] < rank[ult_u]) {
            parent[ult_v] = ult_u;
        }
        else {
            parent[ult_v] = ult_u;
            rank[ult_u]++;
        }
    }
    public static void main(String[] args) {
        Disjoint set = new Disjoint(7);
        set.union_bank(1, 2);
        set.union_bank(2, 3);
        set.union_bank(4, 5);
        set.union_bank(6, 7);
        set.union_bank(5, 6);
        // 3 and 7 belong to same class or not ?
        if(set.findParent(3) == set. findParent(7)) {
            System.out.println("Yes it has");
        }
        else System.out.println("No it dont have node attached to it");
        set.union_bank(3, 7);
        if(set.findParent(3) == set. findParent(7)) {
            System.out.println("Yes it has");
        }
        
    }
}