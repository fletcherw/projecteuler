public class NumLetters {
   public static void main(String[] args) {
      int sum = 0;
      for (int ii = 1; ii < 1000; ii++) {
         sum += letters(ii);
      }
      sum += 11; // "one thousand"
      System.out.println(sum);
   }
   
   public static int letters(int ii) {
      int[] underTwenty = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8};
      int[] tensPlace = {0, 0, 6, 6, 5, 5, 5, 7, 6, 6};
      
      if (ii < 100) {
         if ( ii < 20) {
            return underTwenty[ii];
         } else {
            int sum = 0;
            sum += tensPlace[Integer.parseInt(Integer.toString(ii).substring(0,1))];
            sum += underTwenty[Integer.parseInt(Integer.toString(ii).substring(1))];
            return sum;
         }
      } else {
         int sum = 0;
         sum += 7; // "hundred"
         if (ii % 100 != 0) sum += 3; // "and"
         sum += underTwenty[Integer.parseInt(Integer.toString(ii).substring(0,1))];
         ii -= 100 * Integer.parseInt(Integer.toString(ii).substring(0,1));
         if (ii < 20) {
            sum += underTwenty[ii];
         } else {
            sum += tensPlace[Integer.parseInt(Integer.toString(ii).substring(0,1))];
            sum += underTwenty[Integer.parseInt(Integer.toString(ii).substring(1))];
         }
         return sum;
      }
   }
}