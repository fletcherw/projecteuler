public class Triangle {
   public static void main(String[] args) {
      int triIndex = 12159;
      long triNum = 73914561;
      int numFactors = 0;
      while (numFactors <= 500) {
         if (numFactors > 300 ) System.out.println(triIndex + ", " + triNum + ", " + numFactors);
         triNum += triIndex;
         triIndex++;
         numFactors = findFactors(triNum);
      }
      System.out.println(triNum);
   }
   
   public static int findFactors(long triNum) {
      int count = 0;
      for (int i = 1; i <= triNum; i++) {
         if (triNum % i == 0) {
            count ++;
         }
      }
      return count;
   }
}