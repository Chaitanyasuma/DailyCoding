/*Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed 
to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
*/

import java.util.*;
import java.io.*;
class Main {
  public static void main(String[] args) {
    System.out.println("Enter String");
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    int len = s.length();
    int counter = 0;
    for(int i = 0; i < len; i++) {
      if(s.charAt(i) == '(') 
      {
        if(i != len - 1)
        {
          if(s.charAt(i + 1) != ')')
          {
            counter+= 1;
          }
        }
        else
        {
          counter+= 1;
        } 
      }
      else
      {
        if(i == 0)
        {
          counter+= 1;
        }
        else
        {
          if(s.charAt(i - 1) != '(')
          {
            counter+= 1;
          }
        }
      }
    }
    System.out.println(counter);
  }
}
/*Enter String
()((()()(()))(
6*/
