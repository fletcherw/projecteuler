public class Fact {
   public static void main(String[] args) {
      String num = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000";
      int sum = 0;
      for (int ii = 0; ii < 158; ii++) {
         sum += Integer.parseInt(num.substring(ii,ii+1));
      }
      System.out.println(sum);
   }
}