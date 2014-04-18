public class Sunday {
   public static void main(String[] args) {
      int weekday = 2;
      int year = 1901;
      int month = 1;
      int count = 0;
      
      while (year <= 2000) {
         if (weekday % 7 == 0) count++;
         weekday += 31;
         switch (month) {
            case 2:  weekday -= year % 4 == 0 ? 2 : 3;
                     break;
            case 4:  weekday -= 1;
                     break;
            case 6:  weekday -= 1;
                     break;    
            case 9:  weekday -= 1;
                     break;     
            case 11: weekday -= 1;
                     break;                       
         }
         month++;
         if (month == 13) {
            month -= 12;
            weekday %= 7;
            year++;
         }
      }
      
      System.out.println(count);
   }
}