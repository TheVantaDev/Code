
import java.util.Scanner;

public class Main {
public static void main(String []args){
       Scanner sc = new Scanner (System.in);
       String s = sc.next();
       boolean present [] = new boolean[26];
       for(char ch : s.toCharArray()) {
           present[ch -'a'] = true;
       }
       int cnt = 0;
       for(int i = 0 ; i < 26 ; i++){
          if(present[i]) cnt++;
       } 
       if(cnt % 2 == 0) System.out.println("CHAT WITH HER!");
        else System.out.println("IGNORE HIM!");
  }
}