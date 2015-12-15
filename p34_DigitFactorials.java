public class Factorial {
   public static void main(String[] args) {
      int[] facts = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
      int totalSum = 0;
      for (int ii = 3; ii < 10000000; ii++) {
         int sum = 0;
         String num = Integer.toString(ii);
         for (int jj = 0; sum < ii && jj < num.length(); jj++) {
            sum += facts[Integer.parseInt("" + num.charAt(jj))];
         }
         totalSum += sum == ii ? ii : 0;
      }
      System.out.println(totalSum);
   }
}