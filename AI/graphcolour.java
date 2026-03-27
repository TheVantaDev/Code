import java.util.*;

 class GraphColoringCSP {

    static int V = 4; // number of vertices
    static char[] colors = {'R', 'G', 'B'};
    static int[][] graph = new int[V][V];

    public static void main(String[] args) {

        // Adjacency matrix (based on constraints)
        // 1-based indexing adjusted to 0-based
        addEdge(0, 1); // 1 ≠ 2
        addEdge(0, 2); // 1 ≠ 3
        addEdge(0, 3); // 1 ≠ 4
        addEdge(1, 3); // 2 ≠ 4
        addEdge(2, 3); // 3 ≠ 4

        char[] result = new char[V];

        if (solve(0, result)) {
            System.out.println("Solution found:");
            for (int i = 0; i < V; i++) {
                System.out.println("Vertex " + (i + 1) + " -> " + result[i]);
            }
        } else {
            System.out.println("No solution exists");
        }
    }

    static void addEdge(int u, int v) {
        graph[u][v] = 1;
        graph[v][u] = 1;
    }

    static boolean isSafe(int node, char color, char[] result) {
        for (int i = 0; i < V; i++) {
            if (graph[node][i] == 1 && result[i] == color) {
                return false;
            }
        }
        return true;
    }

    static boolean solve(int node, char[] result) {
        // Base case
        if (node == V) return true;

        for (char color : colors) {
            if (isSafe(node, color, result)) {
                result[node] = color;

                if (solve(node + 1, result))
                    return true;

                // Backtrack
                result[node] = '\0';
            }
        }
        return false;
    }
}