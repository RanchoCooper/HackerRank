package interview_preparation.arrays.left.rotation;

/**
 * @author rancho
 * @date 2019/9/17
 */
public class Solution {

    static int[] rotLeft(int[] a, int d) {
        if (a == null) {
            return null;
        }
        if (d <= 0) {
            return a;
        }

        // newLocation = (currentIndex + rotationK) % lengthOfArray
        int[] result = new int[a.length];
        for (int i = 0; i < a.length; i++) {
            int index = (i + d) % a.length;
            result[i] = a[index];
        }
        return result;
    }

}
