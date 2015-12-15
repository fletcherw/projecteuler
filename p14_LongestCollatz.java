import java.util.Arrays.*;
import java.util.Arrays;


public class Collatz {
   public static void main(String[] args) {
      long highestlength = 0;
      long highestval = 0;
      for (int i=1; i < 1000000; i++) {
         long length = 1;
         long current = i;
         length = length(current);
         if (length > highestlength) {
            highestlength = length;
            highestval = i;
         }
      }
      System.out.printf("Starting number: %d (chain length %d)\n", 
                        highestval, highestlength);
   }
   
   public static int length(long i) {
      int count = 1;
      while (i != 1) {
         count++;// 
         if (i % 2 == 0) {
            i /= 2;
         } else {
            i = (i * 3) + 1;
         }
      }
      return count;
   }
}
