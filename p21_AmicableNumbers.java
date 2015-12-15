public class Amicable {
   public static void main(String[] args) {
   int sum = 0;
      for (int ii = 2; ii < 10000; ii++) {
         if (sumFactors(sumFactors(ii)) == ii && sumFactors(ii) != ii) sum += ii;
      }
      System.out.println(sum);
   }
   
   public static int sumFactors(int num) {
      int sum = 0;
      for (int i = 1; i < num; i++) {
         if (num % i == 0) {
            sum += i;
         }
      }
      return sum;
   }
}