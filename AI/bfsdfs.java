package AI;
import java.util.*;

public class bfsdfs {

class Solution {
    void bfs(int start, List<List<Integer>> adj) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[adj.size()];

        visited[start] = true;
        q.add(start);

        while (!q.isEmpty()) {
            int node = q.poll();  
            System.out.print(node + " ");  
            for (int neighbor : adj.get(node)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.add(neighbor);
                }
            }
        }
    }
    void dfs(int node, List<List<Integer>> adj, boolean[] visited) {
        visited[node] = true;
        System.out.print(node + " ");

        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited);
            }
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int V = 5; 
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }
        adj.get(0).add(1);
        adj.get(0).add(2);
        adj.get(1).add(3);
        adj.get(2).add(4);
        System.out.println("BFS Traversal:");
        sol.bfs(0, adj);
    }
}
}
