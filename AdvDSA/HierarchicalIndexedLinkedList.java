
import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class HierarchicalIndexedLinkedList {
    
    // Node class with multiple level pointers
    static class Node {
        int data;
        Node[] levels;  // Array of pointers for each level
        
        Node(int data, int maxHeight) {
            this.data = data;
            this.levels = new Node[maxHeight];
        }
        
        @Override
        public String toString() {
            return String.valueOf(data);
        }
    }
    
    // Main list class
    static class HierarchicalList {
        private Node head;
        private int maxHeight;
        private int k;  // Fanout factor
        private int size;
        
        // Constructor
        public HierarchicalList(int k) {
            this.k = k;
            this.head = null;
            this.size = 0;
            this.maxHeight = 1;
        }
        
        // Build from sorted array - O(n)
        public void buildFromArray(int[] arr) {
            if (arr.length == 0) return;
            
            size = arr.length;
            maxHeight = calculateHeight(size);
            
            System.out.println("\n=== Building Hierarchical Indexed List ===");
            System.out.println("Size: " + size);
            System.out.println("Fanout k: " + k);
            System.out.println("Height: " + maxHeight + " levels");
            
            // Create all nodes
            Node[] nodes = new Node[size];
            for (int i = 0; i < size; i++) {
                nodes[i] = new Node(arr[i], maxHeight);
            }
            
            // Build each level
            for (int level = 0; level < maxHeight; level++) {
                int step = (int) Math.pow(k, level);
                
                for (int i = 0; i < size; i += step) {
                    int nextIndex = i + step;
                    if (nextIndex < size) {
                        nodes[i].levels[level] = nodes[nextIndex];
                    }
                }
            }
            
            head = nodes[0];
            printStructure();
        }
        
        // Search operation - O(log n)
        public Node search(int target) {
            if (head == null) return null;
            
            Node current = head;
            int comparisons = 0;
            
            System.out.println("\n--- Searching for: " + target + " ---");
            
            // Start from highest level, work down
            for (int level = maxHeight - 1; level >= 0; level--) {
                System.out.print("Level " + level + ": " + current.data);
                
                // Move forward at this level
                while (current.levels[level] != null && 
                       current.levels[level].data < target) {
                    current = current.levels[level];
                    comparisons++;
                    System.out.print(" → " + current.data);
                }
                
                // Check if we found it
                if (current.levels[level] != null && 
                    current.levels[level].data == target) {
                    current = current.levels[level];
                    comparisons++;
                    System.out.println(" → " + current.data + " ✓ FOUND!");
                    System.out.println("Comparisons: " + comparisons);
                    return current;
                }
                
                System.out.println(" (drop down)");
            }
            
            // Check current node
            if (current.data == target) {
                System.out.println("Found at current: " + current.data);
                return current;
            }
            
            System.out.println("Not found. Comparisons: " + comparisons);
            return null;
        }
        
        // Insert operation - O(log n)
        public void insert(int value) {
            System.out.println("\n--- Inserting: " + value + " ---");
            
            // Recalculate height if needed
            int newHeight = calculateHeight(size + 1);
            if (newHeight > maxHeight) {
                rebuildWithNewHeight(newHeight);
            }
            
            // Find insertion path
            Node current = head;
            Node[] update = new Node[maxHeight];
            
            for (int level = maxHeight - 1; level >= 0; level--) {
                while (current.levels[level] != null && 
                       current.levels[level].data < value) {
                    current = current.levels[level];
                }
                update[level] = current;
            }
            
            // Create new node
            Node newNode = new Node(value, maxHeight);
            
            // Insert at appropriate levels based on k-spacing
            int nodePosition = size;
            for (int level = 0; level < maxHeight; level++) {
                int step = (int) Math.pow(k, level);
                if (nodePosition % step == 0) {
                    newNode.levels[level] = update[level].levels[level];
                    update[level].levels[level] = newNode;
                }
            }
            
            size++;
            System.out.println("Inserted successfully. New size: " + size);
        }
        
        // Delete operation - O(log n)
        public boolean delete(int value) {
            System.out.println("\n--- Deleting: " + value + " ---");
            
            if (head == null) return false;
            
            // Find deletion path
            Node current = head;
            Node[] update = new Node[maxHeight];
            
            for (int level = maxHeight - 1; level >= 0; level--) {
                while (current.levels[level] != null && 
                       current.levels[level].data < value) {
                    current = current.levels[level];
                }
                update[level] = current;
            }
            
            // Get target node
            Node target = current.levels[0];
            if (target == null || target.data != value) {
                System.out.println("Value not found!");
                return false;
            }
            
            // Remove from all levels
            for (int level = 0; level < maxHeight; level++) {
                if (update[level].levels[level] == target) {
                    update[level].levels[level] = target.levels[level];
                }
            }
            
            size--;
            System.out.println("Deleted successfully. New size: " + size);
            return true;
        }
        
        // Calculate required height
        private int calculateHeight(int n) {
            if (n <= 1) return 1;
            return (int) Math.ceil(Math.log(n) / Math.log(k)) + 1;
        }
        
        // Rebuild with new height (when size grows significantly)
        private void rebuildWithNewHeight(int newHeight) {
            System.out.println("Rebuilding with new height: " + newHeight);
            List<Integer> values = toList();
            maxHeight = newHeight;
            buildFromArray(values.stream().mapToInt(i -> i).toArray());
        }
        
        // Convert to list
        private List<Integer> toList() {
            List<Integer> result = new ArrayList<>();
            Node current = head;
            while (current != null) {
                result.add(current.data);
                current = current.levels[0];
            }
            return result;
        }
        
        // Print structure
        public void printStructure() {
            System.out.println("\n=== Structure ===");
            for (int level = maxHeight - 1; level >= 0; level--) {
                int step = (int) Math.pow(k, level);
                System.out.print("Level " + level + " (step=" + step + "): ");
                
                Node current = head;
                int position = 0;
                while (current != null) {
                    if (position % step == 0) {
                        System.out.print(current.data + " → ");
                    }
                    current = current.levels[0];
                    position++;
                }
                System.out.println("null");
            }
        }
        
        // Print all elements
        public void printList() {
            System.out.print("List: ");
            Node current = head;
            while (current != null) {
                System.out.print(current.data + " ");
                current = current.levels[0];
            }
            System.out.println();
        }
        
        // Get size
        public int getSize() {
            return size;
        }
    }
    
    // Main method with comprehensive testing
    public static void main(String[] args) {
        System.out.println("╔════════════════════════════════════════════════════════╗");
        System.out.println("║  Hierarchical Indexed Linked List Implementation     ║");
        System.out.println("╚════════════════════════════════════════════════════════╝");
        
        // Test 1: Build from array
        System.out.println("\n■ TEST 1: Build from sorted array");
        int[] arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160};
        HierarchicalList list = new HierarchicalList(4);
        list.buildFromArray(arr);
        
        // Test 2: Multiple searches
        System.out.println("\n■ TEST 2: Search operations");
        list.search(70);
        list.search(150);
        list.search(10);
        list.search(160);
        list.search(999);  // Not found
        
        // Test 3: Build larger list
        System.out.println("\n\n■ TEST 3: Larger list (n=100)");
        int[] largeArr = new int[100];
        for (int i = 0; i < 100; i++) {
            largeArr[i] = (i + 1) * 10;
        }
        HierarchicalList largeList = new HierarchicalList(4);
        largeList.buildFromArray(largeArr);
        
        largeList.search(500);
        largeList.search(250);
        
        // Test 4: Performance comparison
        System.out.println("\n\n■ TEST 4: Performance Analysis");
        performanceTest(1000, 4);
        performanceTest(10000, 4);
        
        // Test 5: Different k values
        System.out.println("\n\n■ TEST 5: Different fanout values");
        testDifferentK(1000);
    }
    
    // Performance testing
    private static void performanceTest(int n, int k) {
        System.out.println("\n--- Performance Test: n=" + n + ", k=" + k + " ---");
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }
        
        HierarchicalList list = new HierarchicalList(k);
        
        long startTime = System.nanoTime();
        list.buildFromArray(arr);
        long buildTime = System.nanoTime() - startTime;
        
        // Search for random elements
        Random rand = new Random(42);
        int searches = 1000;
        startTime = System.nanoTime();
        for (int i = 0; i < searches; i++) {
            int target = rand.nextInt(n) + 1;
            list.search(target);
        }
        long searchTime = System.nanoTime() - startTime;
        
        System.out.println("Build time: " + buildTime / 1_000_000.0 + " ms");
        System.out.println("Avg search time: " + (searchTime / searches) / 1000.0 + " μs");
        System.out.println("Theoretical comparisons: ~" + 
            (int)(k * Math.ceil(Math.log(n) / Math.log(k))));
    }
    
    // Test different k values
    private static void testDifferentK(int n) {
        int[] kValues = {2, 3, 4, 8};
        
        System.out.println("\nComparison for n=" + n + ":");
        System.out.println("k\tLevels\tTheoretical Comparisons");
        System.out.println("─────────────────────────────────────");
        
        for (int k : kValues) {
            int height = (int) Math.ceil(Math.log(n) / Math.log(k)) + 1;
            int comparisons = (int)(k * Math.ceil(Math.log(n) / Math.log(k)));
            System.out.printf("%d\t%d\t%d\n", k, height, comparisons);
        }
    }
}
