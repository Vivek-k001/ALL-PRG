import java.util.*; 
public class RemoveVowels { public
 static void main(String args[]) { 
String str, r; String[] v=
 {"a","e","i","o","u","A","E","I","O","U"};
 Scanner sc=new Scanner(System.in);
 System.out.print("Enter the string : ");
 str=sc.nextLine(); r=str; 
for(int i=0;i<10;i++)
 r=r.replaceAll(v[i],"");
 System.out.println("String after removing vowels : " + r ); } }