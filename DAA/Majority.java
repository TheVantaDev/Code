import java.util.*;

public class Majority{

      static Integer bruteForce(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            int count = 0;

            for (int j = 0; j < n; j++) {
                if (arr[i] == arr[j])
                    count++;
            }

            if (count > n / 2)
                return arr[i];
        }

        return null;
    }

    
    static Integer sortMethod(int[] arr) {
        int[] temp = arr.clone();
        Arrays.sort(temp);

        int candidate = temp[temp.length / 2];
        int count = 0;

        for (int num : temp) {
            if (num == candidate)
                count++;
        }

        if (count > temp.length / 2)
            return candidate;

        return null;
    }

    
    static int countOccurrences(int[] arr, int candidate, int left, int right) {
        int count = 0;

        for (int i = left; i <= right; i++) {
            if (arr[i] == candidate)
                count++;
        }

        return count;
    }

    static int majorityRec(int[] arr, int left, int right) {

        if (left == right)
            return arr[left];

        int mid = (left + right) / 2;

        int leftMajor = majorityRec(arr, left, mid);
        int rightMajor = majorityRec(arr, mid + 1, right);

        if (leftMajor == rightMajor)
            return leftMajor;

        int leftCount = countOccurrences(arr, leftMajor, left, right);
        int rightCount = countOccurrences(arr, rightMajor, left, right);

        return (leftCount > rightCount) ? leftMajor : rightMajor;
    }

    static Integer divideAndConquer(int[] arr) {
        int candidate = majorityRec(arr, 0, arr.length - 1);

        int count = 0;
        for (int num : arr) {
            if (num == candidate)
                count++;
        }

        if (count > arr.length / 2)
            return candidate;

        return null;
    }

    
    static Integer boyerMoore(int[] arr) {
        int candidate = -1;
        int count = 0;

        for (int num : arr) {

            if (count == 0)
                candidate = num;

            if (candidate == num)
                count++;
            else
                count--;
        }

        count = 0;

        for (int num : arr) {
            if (num == candidate)
                count++;
        }

        if (count > arr.length / 2)
            return candidate;

        return null;
    }


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }


        int choice;
do {
    System.out.println("\n===== Majority Element Menu =====");
    System.out.println("1. Brute Force");
    System.out.println("2. Sort Method");
    System.out.println("3. Divide and Conquer");
    System.out.println("4. Boyer-Moore Voting");
    System.out.println("5. Exit");
    System.out.print("Enter your choice: ");

    choice = sc.nextInt();

    Integer result = null;

    switch (choice) {
        case 1:
            result = bruteForce(arr);
            break;

        case 2:
            result = sortMethod(arr);
            break;

        case 3:
            result = divideAndConquer(arr);
            break;

        case 4:
            result = boyerMoore(arr);
            break;

        case 5:
            System.out.println("Exiting...");
            break;

        default:
            System.out.println("Invalid Choice!");
    }

    if (choice >= 1 && choice <= 4) {
        if (result != null)
            System.out.println("Majority Element = " + result);
        else
            System.out.println("No Majority Element Found.");
    }

} while (choice != 5);

sc.close();
    }
}