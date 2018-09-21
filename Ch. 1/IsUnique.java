import java.util.*;

/**
 * Check if a string has unique characters
 */

public class IsUnique {

   public static void main (String[] args) {
      Scanner scanner = new Scanner(System.in);
      String s = scanner.next();
      System.out.println(unique_1(s));
      System.out.println(unique_2(s));
   }

   /* Hashmap */
   public static boolean unique_1 (String s) {
      HashMap map = new HashMap();
      char[] c = s.toCharArray();
      for (int i = 0; i < c.length; i++) {
         if (map.containsKey(c[i])) {
            return false;
         }
         else {
            map.put(c[i], 1);
         }
      }
      return true;
   }

   /* Sort */
   public static boolean unique_2 (String s) {
      char[] c = s.toCharArray();
      Arrays.sort(c);
      for (int i = 0; i < c.length-1; i++) {
         if (c[i] == c[i+1]) {
            return false;
         }
      }
      return true;
   }
}

