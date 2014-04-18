import java.math.*;

public class PowerSum {
   public static void main(String[] args) {
      BigInteger total = BigInteger.valueOf(0);
      for (int ii = 1; ii <= 1000; ii++) {
         BigInteger base = BigInteger.valueOf(ii);
         total = total.add(base.pow(ii));
      }
      String num = total.toString();
      System.out.println(num.substring(num.length() - 15));
   }
}