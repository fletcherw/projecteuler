public class Fibonacci {
   public static void main(String[] args) {
      BigInteger prevprev = BigInteger.valueOf(0);
      BigInteger prev = BigInteger.valueOf(1);
      BigInteger fibNum = BigInteger.valueOf(1);
      while(Math.log10(fibNum) < 1000) {
         prevprev = prev;
         prev = fibNum;
         fibNum = fibNum.add(prev);
         fibNum = fibNum.add(prevprev);
      }
      System.out.println(fibNum);
   }
}