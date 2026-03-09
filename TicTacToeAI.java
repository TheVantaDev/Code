import java.util.LinkedList;
import java.util.Queue;

class TreeNode {
    String value;
    TreeNode left;
    TreeNode right;

    TreeNode(String value) {
        this.value = value;
    }
}

 class TreeBfsDfsDemo {

    // Build a small tree:
    //        A
    //      /   \
    //     B     C
    //    / \     \
    //   D   E     F
    private static TreeNode buildSampleTree() {
        TreeNode A = new TreeNode("A");
        TreeNode B = new TreeNode("B");
        TreeNode C = new TreeNode("C");
        TreeNode D = new TreeNode("D");
        TreeNode E = new TreeNode("E");
        TreeNode F = new TreeNode("F");

        A.left = B;
        A.right = C;
        B.left = D;
        B.right = E;
        C.right = F;

        return A;
    }

    // -------- BFS (level-order) on tree --------
    public static boolean bfs(TreeNode root, String goal) {
        if (root == null) return false;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        System.out.print("BFS order: ");

        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            System.out.print(node.value + " ");

            if (node.value.equals(goal)) {
                System.out.println("\nGoal Found (BFS)");
                return true;
            }

            if (node.left != null) q.add(node.left);
            if (node.right != null) q.add(node.right);
        }

        System.out.println("\nGoal Not Found (BFS)");
        return false;
    }

    // -------- DFS (preorder) on tree --------
    public static boolean dfs(TreeNode root, String goal) {
        System.out.print("DFS order: ");
        boolean found = dfsRec(root, goal);
        if (found) {
            System.out.println("\nGoal Found (DFS)");
        } else {
            System.out.println("\nGoal Not Found (DFS)");
        }
        return found;
    }

    private static boolean dfsRec(TreeNode node, String goal) {
        if (node == null) return false;

        System.out.print(node.value + " ");

        if (node.value.equals(goal)) {
            return true;
        }

        // go deep on left, then right
        if (dfsRec(node.left, goal)) return true;
        if (dfsRec(node.right, goal)) return true;

        return false;
    }

    public static void main(String[] args) {
        TreeNode root = buildSampleTree();
        String goal = "F";

        System.out.println("Tree BFS/DFS demo, goal = " + goal);
        bfs(root, goal);  // level-order: A B C D E F
        dfs(root, goal);  // depth-first (preorder): A B D E C F
    }
}
