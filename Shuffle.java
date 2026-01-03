import java.util.*;
public class Shuffle {
    public static void main(String[] args) {
        shuffleArray(args);
        for (String x : args) {
            System.out.print(x + " ");
        }
        System.out.println();
        Integer[] array = {1, 2, 3, 4};
        shuffleArray(array);
        for (int x : array) {
            System.out.print(x + " ");
        }
    }

    public static void shuffleArray(Object[] arr) {
        Random random = new Random();
        for (int i = 0; i < arr.length; i++) {
            int k = random.nextInt(arr.length - i);
            int index = k + i;
            swap(arr, i, index);
        }
    }

    public static void swap(Object[] arr, int index1, int index2) {
        Object temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}