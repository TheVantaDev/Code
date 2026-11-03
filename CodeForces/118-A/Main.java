import java.util.Scanner;

public class Main {
    public static boolean isUppercaseConsonant(char ch) {
        boolean isUppercaseLetter = (ch >= 'A' && ch <= 'Z');
        boolean isVowel = (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' || ch == 'Y');
        return isUppercaseLetter && !isVowel;
    }
    public static boolean f(char ch) {
        boolean isUppercaseLetter = (ch >= 'a' && ch <= 'z');
        boolean isVowel = (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'y');
        return isUppercaseLetter && !isVowel;
    }
    public static void main(String []args) {
        Scanner sc = new Scanner (System.in);
        String s = sc.next();
        StringBuilder sb = new StringBuilder(s);
        // remove all vowels 
        for(int i = 0 ; i < sb.length(); i++){
            char ch = sb.charAt(i);
             if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'y'
        || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' || ch == 'Y') {
        sb.deleteCharAt(i);
        i--;   // stay at same position
    }
        }
        // uppercase consonants to lower case
        for(int i  = 0 ;i < sb.length() ; i++) {
            char ch = sb.charAt(i);
            if(isUppercaseConsonant(ch)) {
            sb.setCharAt(i, (char)(ch + 32));            }
        }
        // put . as a prefix if consnuntis there ?
        StringBuilder ans = new StringBuilder();
        for(int i = 0 ;i < sb.length() ; i++) {
            char ch = sb.charAt(i);
            if(f(ch)){
                ans.append(".");
                ans.append(ch);
            }
            else {
                ans.append(ch);
            }
        }
        System.out.println(ans.toString());

    }

}
