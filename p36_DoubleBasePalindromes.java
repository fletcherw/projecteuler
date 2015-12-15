public class Palindrome {
   public static void main(String[] args) {
      int sum = 0;
      for (int ii=0; ii < 1000000; ii++) {
         if (palCheck(ii, 10)) sum += palCheck(ii, 2) ? ii : 0;
      }
      
      System.out.println(sum);
   }
   
   public static boolean palCheck(int value, int radix) {
      String val = Integer.toString(value, radix);
      if (val.length() % 2 == 0) {
         for (int ii = 0; ii < val.length() / 2; ii++) {
            if (val.charAt(ii) != val.charAt(val.length() - ii - 1)) return false;
         }   
      } else {
         for (int ii = 0; ii < (val.length() - 1) / 2; ii++) {
            if (val.charAt(ii) != val.charAt(val.length() - ii - 1)) return false;
         }  
      }
      return true;
   }
}